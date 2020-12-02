from functools import reduce

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    delimiters = '.',',',';','?',' '
    new_split = split(delimiters,text)
    # filtered_split = ' '.join(list(filter(lambda word: word.lower() not in text, new_split)))
    word_split = list(map(lambda word: word.lower(),new_split))
    filtered_split = (list(filter(lambda word: len(word) > 0, word_split)))
    #print(filtered_split)
    return filtered_split
#convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
    
def words_longer_than(length, text):
    text = convert_to_word_list(text)
    filtered_length = list(filter(lambda word : len(word) >= length,text))
    print(filtered_length)
    return filtered_length
    
def words_lengths_map(text):
    word_number = [len(word) for word in convert_to_word_list(text)]
    words_length = {len(word):word_number.count(len(word)) for word in convert_to_word_list(text)}
    print(words_length)
    return words_length
words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?")


def letters_count_map(text):
    letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    word_number = [letters_list[letter] for letter in convert_to_word_list(text) if letter in letters_list ]
    print(word_number)
    # words_length = {letters_list[0]:word_number.count(letter) for letter in letters_list}
    words_length = {letter:text.count(letter) for letter in letters_list}
    print(words_length)
    return words_length
letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?")

def most_used_character(text):
    if text == '':
        return None
    else:
        count_dict = letters_count_map(text)
        letter_count = reduce(lambda x,y : x if count_dict[x] > count_dict[y] else y ,count_dict)
        print(letter_count)
        return letter_count
most_used_character("These are indeed interesting, an obvious understatement, times. What say you?")
