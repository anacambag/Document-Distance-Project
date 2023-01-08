# Name: Ana Camba Gomes


# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    text_to_list = input_text.split() #turns a string of words into a list
    return text_to_list


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    
    frequencies = {}
    
    for i in input_iterable:
        if i not in frequencies: #evaluates if the word or letter is already in the new dictionary.
            frequencies[i] = 1 #if the word or letter not in dictionary it adds one to the frequency
        else:
            frequencies[i] += 1 #if it already exists adds one to existence frequency
    return frequencies
             
### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    #good to use previous function 
    
    return get_frequencies(word) #counts how many  times a letter occurs in a string



### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    

   
    difference = 0
    difference_total = 0
    
    for key1 in freq_dict1: #we evaluate the word in both dictionaries and implement the parameters.
        if key1 in freq_dict2:
            difference = abs(freq_dict1[key1]-freq_dict2[key1])
            difference_total += difference
            
        elif key1 not in freq_dict2:
            difference = freq_dict1[key1] #if only in first dictionary the frequency is the first value on the first dictionary
            difference_total += difference
            
    for key2 in freq_dict2:
        if key2 not in freq_dict1:
            difference = freq_dict2[key2]
            difference_total += difference
    
            
    
    
    all_ = 0
    all_total = 0
    for key1 in freq_dict1:
        if key1 in freq_dict2:
            all_ = freq_dict1[key1]+freq_dict2[key1]
           
            all_total += all_
            
        elif key1 not in freq_dict2:
            all_ = freq_dict1[key1]
            all_total += all_
            
    for key2 in freq_dict2: 
        if key2 not in freq_dict1: #since we had previously evaluated the other dictionary, in this one we set it as the first time we see the letter.
            all_ = freq_dict2[key2]
            all_total += all_
            
    
    
    frequency_total = 1-(difference_total/all_total) #calculating the frequency total
    return round(frequency_total,2) #returning answer with only 2 decimals places.
            
        
        

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    new_dict = {} #new dictionary in which add the words with the most frequencies in both dictionaries.
    frequent_words = []
    
    for key,value in freq_dict1.items():
        if key not in new_dict:
            new_dict[key] = value
        else:
            new_dict[key] = new_dict[key] + value #we keep the value that the key had and add the new one to increase frequency.
            
    for key1,value1 in freq_dict2.items():
        if key1 not in new_dict:
            new_dict[key1] = value1
        else:
            new_dict[key1] = new_dict[key1] + value1
    
    highest = max(new_dict.values()) #we evaluate the highets value in our new dict with all the words combined
    
    for key2,value2 in new_dict.items():
        if value2 == highest:
            frequent_words.append(key2) #we add the words that match the highest to our list of frequent words
            
    frequent_words.sort() #alphabetical order
            
    return frequent_words
            
    



### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    file_content = load_file(file_path) #first we load the file
    
    list_content = text_to_list(file_content) #pass it from string to list
    
    dict_frequency = get_frequencies(list_content) #form a dictionary of frequencies with the previous list
    
    tf_dict = {}
    
    for key,value in dict_frequency.items():
        tf_dict[key] = value/sum(dict_frequency.values()) #values is the frequency of the word in the document so our numerator, and sum of values in the list gives the total number of words.
    return tf_dict
        
    
    

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    docs = file_paths
    num_docs = len(docs) #get the total amount of documents
    new_dict = {}
    idf_dict = {}
    
    for i in docs:
        file_content = load_file(i)
        list_content = text_to_list(file_content)
        dict_list = get_frequencies(list_content)
        
        for key,value in dict_list.items(): #evaluates content in both documents and creates only one dictionary off of that
            if key not in new_dict:
                new_dict[key] = 1 #if first time the word appears in a document it counts one
            else:
                new_dict[key] += 1 #if appears in another document
    
    for key,value in new_dict.items():
        idf_dict[key] = math.log10(num_docs/value) #the value is the amount of documents the word appeared on
    
    return idf_dict
       
    
    

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tfidf_dict = {}
    dict_tf = get_tf(tf_file_path)
    dict_idf = get_idf(idf_file_paths)
    
    for key in dict_tf.keys(): #we used keys in dict_tf because is the ones that we want to evaluate
        tfidf_dict[key] = dict_idf[key] * dict_tf[key] #we create a new dictionary with the values from the dictionary of tf values and idf values.
    keys_value_list = list(tfidf_dict.items()) #list of tuples of the key and value
    keys_value_list.sort(key = lambda a:a [0]) #sort by alphabetical order, important to do this to meet the second parameter when scores are the same the order has to be alphabetical for those values
    keys_value_list.sort(key = lambda a:a [1]) #lastly sort by score
    return keys_value_list
            
        
        
        
    


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    # Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    #print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    #print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    #print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
