# Code adapted from http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver
# from Python2 to Python3.
def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result

def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result

def neighbors(pos):
    for nx in range(max(0, pos[0]-1), min(pos[0]+2, ncols)):
        for ny in range(max(0, pos[1]-1), min(pos[1]+2, nrows)):
            yield (nx, ny)

def score(letter_scores, word):
    word_score = 0
    for c in word:
        word_score += letter_scores[c]
    return word_score

import sys
import re
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

                 
while True:
    raw_grid = input("Please enter a 16 char string that represents the boggle grid: ")
    if not (raw_grid.isalpha() and len(raw_grid) == 16):
        print("Invalid entry")
        continue
    grid = []
    for i in range(4):
        grid.append(raw_grid[i*4:(i+1)*4].lower())
    nrows, ncols = len(grid), len(grid[0])

    # A dictionary word that could be a solution must use only the grid's
    # letters and have length >= 3. (With a case-insensitive match.)

    alphabet = ''.join(set(''.join(grid)))
    bogglable = re.compile('[' + alphabet + ']{3,}$', re.I).match

    words = set(word.rstrip('\n') for word in open('words.txt') if bogglable(word))
    prefixes = set(word[:i] for word in words
                   for i in range(2, len(word)+1))

    solved_words = set()
    for result in solve():
        word_score = score(LETTER_SCORES, result[0])
        solved_words.add((word_score, result[0]))
    word_list = list(solved_words)
    word_list.sort(reverse=True)
    print()
    for i in range(10):
        print(word_list[i])
    print()


