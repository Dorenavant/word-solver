# Small program to solve games like words with friends, word cookies, etc.
def solve():
    for letter in alphabet:
        for result in extending(letter, addable(letter, alphabet)):
            yield result

def addable(letter, current_alphabet):
    new_alphabet = list(letter for letter in current_alphabet)
    new_alphabet.remove(letter)
    return new_alphabet

def extending(prefix, remaining):
    if prefix in words:
        yield prefix
    for letter in remaining:
        prefix1 = prefix + letter
        if prefix1 in prefixes:
            for result in extending(prefix1, addable(letter, remaining)):
                yield result
                
def score(letter_scores, word):
    word_score = 0
    for c in word:
        word_score += letter_scores[c]
    return word_score

import sys
import re
from enum import Enum

LETTER_SCORES = {'a': 1,
                 'b': 4,
                 'c': 4,
                 'd': 2,
                 'e': 1,
                 'f': 4,
                 'g': 3,
                 'h': 3,
                 'i': 1,
                 'j': 10,
                 'k': 5,
                 'l': 2,
                 'm': 4,
                 'n': 2,
                 'o': 1,
                 'p': 4,
                 'q': 10,
                 'r': 1,
                 's': 1,
                 't': 1,
                 'u': 2,
                 'v': 5,
                 'w': 4,
                 'x': 8,
                 'y': 3,
                 'z': 10}

class Mode(Enum):
    ALL = 0
    LENGTH = 1
    POINTS = 2
    LONGEST = 3
    LETTER = 4

mode = Mode.ALL
while True:
    choice = input("Please choose a mode:\n"
                   + "\t\t(0) Find all words\n"
                   + "\t\t(1) Find top 10 longest words\n"
                   + "\t\t(2) Find top 10 words worth the most points\n"
                   + "\t\t(3) Find words of a certain length\n"
                   + "\t\t(4) Find all words with a certain letter in it\n")
    if (choice == "0"): break
    elif (choice == "1"): mode = Mode.LONGEST
    elif (choice == "2"): mode = Mode.POINTS
    elif (choice == "3"): mode = Mode.LENGTH
    elif (choice == "4"): mode = Mode.LETTER
    else:
        print("Invalid choice")
        continue
    break

if (mode == Mode.ALL):
     while True:
        raw_alphabet = input("Please enter the letters to solve for: ")
        if not (raw_alphabet.isalpha()):
            print("Invalid entry")
            continue
        raw_alphabet = raw_alphabet.lower()

        # A dictionary word that could be a solution must use only the grid's
        # letters and have length >= 3. (With a case-insensitive match.)

        alphabet = list(raw_alphabet)
        makeable = re.compile('[' + raw_alphabet + ']{3,}$', re.I).match

        words = set(word.rstrip('\n') for word in open('words.txt') if makeable(word))
        prefixes = set(word[:i] for word in words
                       for i in range(2, len(word)+1))
        solved_words = set()
        for word in solve():
            solved_words.add(word)
        word_list = list(solved_words)
        word_list.sort(key=len, reverse=True)
        for i in range(min(50, len(word_list))): print(word_list[i])

elif (mode == Mode.LONGEST):
    while True:
        raw_alphabet = input("Please enter the letters to solve for: ")
        if not (raw_alphabet.isalpha()):
            print("Invalid entry")
            continue
        
        raw_alphabet = raw_alphabet.lower()

        # A dictionary word that could be a solution must use only the grid's
        # letters and have length >= 3. (With a case-insensitive match.)

        alphabet = list(raw_alphabet)
        makeable = re.compile('[' + raw_alphabet + ']{3,}$', re.I).match

        words = set(word.rstrip('\n') for word in open('words.txt') if makeable(word))
        prefixes = set(word[:i] for word in words
                       for i in range(2, len(word)+1))
        solved_words = set()
        for word in solve():
            solved_words.add(word)
        word_list = list(solved_words)
        word_list.sort(key=len, reverse=True)
        for i in range(min(10, len(word_list))): print(word_list[i])

elif (mode == Mode.POINTS):
    while True:
        raw_alphabet = input("Please enter the letters to solve for: ")
        if not (raw_alphabet.isalpha()):
            print("Invalid entry")
            continue

        raw_alphabet = raw_alphabet.lower()

        # A dictionary word that could be a solution must use only the grid's
        # letters and have length >= 3. (With a case-insensitive match.)

        alphabet = list(raw_alphabet)
        makeable = re.compile('[' + raw_alphabet + ']{3,}$', re.I).match

        words = set(word.rstrip('\n') for word in open('words.txt') if makeable(word))
        prefixes = set(word[:i] for word in words
                       for i in range(2, len(word)+1))
        solved_words = set()
        for word in solve():
            word_score = score(LETTER_SCORES, word)
            solved_words.add(
                (word_score, word))
        word_list = list(solved_words)
        word_list.sort(reverse=True)
        for i in range(min(10, len(word_list))): print(word_list[i])

elif (mode == Mode.LENGTH):
    while True:
        raw_alphabet = input("Please enter the letters to solve for: ")
        if not (raw_alphabet.isalpha()):
            print("Invalid entry")
            continue
        while True:
            length = input("Please enter the length of words you'd like to search for: ")
            if not (length.isdigit()):
                print("Invalid entry")
                continue
            break

        raw_alphabet = raw_alphabet.lower()
        
        # A dictionary word that could be a solution must use only the grid's
        # letters and have length >= 3. (With a case-insensitive match.)

        alphabet = list(raw_alphabet)
        makeable = re.compile('[' + raw_alphabet + ']{' + length + '}$', re.I).match

        words = set(word.rstrip('\n') for word in open('words.txt') if makeable(word))
        prefixes = set(word[:i] for word in words
                       for i in range(2, len(word)+1))
        solved_words = set()
        for word in solve():
            solved_words.add(word)
        word_list = list(solved_words)
        for i in range(min(50, len(word_list))): print(word_list[i])

        


