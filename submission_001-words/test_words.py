import word_processor
import unittest
from functools import reduce

class TestWord(unittest.TestCase):

    def test_word_split(self):
        words = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertTrue(word_processor.convert_to_word_list(words),True)
    
    def test_words_longer_than(self):
        words = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertTrue(word_processor.words_longer_than(4,"words"),True)
    
    def test_words_length_map(self):
        words = "These are indeed interesting, an obvious understatement, times. What say you?"
        self.assertTrue(word_processor.words_lengths_map('word'),True)

    def test_count_letters(self):
        word = "These are indeed interesting, an obvious understatement, times. What say you?"
        letters_count = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 7, 'u': 3, 'v': 1, 'w': 0, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(letters_count,word_processor.letters_count_map(word))

    def test_most_used_letters(self):
        text = "These are indeed interesting, an obvious understatement, times. What say you?"
        letters_count = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 7, 'u': 3, 'v': 1, 'w': 0, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual('e',word_processor.most_used_character(text))

if __name__ == '__main__': 
    unittest.main() 