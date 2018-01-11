"""
Muneeb Ansari
PyCheats - Scrabble
"""
import re


def output(the_word, score):
    return "You can play '{}' for a total of {} base points.".format(the_word,
                                                                     score)


def valid_words(words_lst, the_rack):
    result = []
    for word in range(len(words_lst)):
        letter_in_rack, letter_count = True, True
        for letter in words_lst[word]:
            if letter not in rack:
                letter_in_rack = False
            if words_lst[word].count(letter) > the_rack.count(letter):
                letter_count = False
        if letter_count and letter_in_rack:
            result.append(words_lst[word])
    return result


def word_points(word_lst, points_dict):
    points_lst = []
    for word in range(len(word_lst)):
        points = 0
        for letter in word_lst[word]:
            if letter in letters_to_points:
                points += points_dict[letter]

        points_lst.append(points)
    return points_lst


def quick_sggst():
    p_max = 'Max points: ' + str(word_score_sorted[-1])
    p_min = ' Min points: ' + str(word_score_sorted[0])
    return 'Quick Suggestion ->  {} | {}'.format(p_max, p_min)


if __name__ == '__main__':

    # Enter letters in rack
    input_rack = ''
    letters_only = True
    while not len(input_rack) == 7:
        input_rack = input('input rack: ').lower()
        letters_only = re.match(r'^[A-Za-z ]*$', input_rack)

    if not letters_only:
        print('Invalid letters!')
    else:
        with open('words.txt', 'r') as scrabble_words:
            rack = list(input_rack)
            word_list = scrabble_words.readlines()
            word_list_clean = [x.strip() for x in word_list]
            letters_to_points = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                                 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                                 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10,
                                 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4,
                                 'x': 8, 'y': 4, 'z': 10}

            # Get possible words based on letters from rack
            valid_words_lst = valid_words(word_list_clean, rack)

            # Allocate points to word based on points of individual letters
            points_list = word_points(valid_words_lst, letters_to_points)

            zipped = zip(points_list, valid_words_lst)
            word_score = list(zipped)
            word_score_sorted = sorted(word_score)

            # Display all the words that can be made from letters in rack
            # along with their respective point total

            print(quick_sggst())
            for x in reversed(word_score_sorted):
                print('\n' + output(x[1], x[0]))
