#!/usr/bin/python
import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def is_vowels_in_ascending(word):
    vowels_count=[]
    for letter in word:
        if letter.lower() in vowels:
            vowels_count.append(letter.lower())

    if vowels_count == vowels:
            return True
    return False


def is_letters_in_ascending(word):
    letter_ord = []
    word = word.replace("'","")
    for letter in word:
        letter_ord.append(ord(letter.lower()))

    if letter_ord == sorted(letter_ord) and len(letter_ord)>5:
        return True
    return False


def main():
    dict_name = sys.argv[1]
    if not dict_name:
        print 'usage: python dictionary.py words'
        sys.exit(1)

    vowels_in_ascending = []
    letters_in_ascending = []

    with open(dict_name, 'r') as f:
        dictionary = f.readlines()
        dictionary = [x.replace('\n','') for x in dictionary]
        for word in dictionary:
            if is_vowels_in_ascending(word):
                vowels_in_ascending.append(word)
            if is_letters_in_ascending(word):
                letters_in_ascending.append(word.lower())

    print '\n\n'
    print '*'*50
    print 'There are %d  words with all vowels in ascending order  :' % (len(set(vowels_in_ascending)))
    print list(set(vowels_in_ascending))
    print '\n\n'
    print '*'*50
    print 'There are %d  words with all letters in ascending order  :' % (len(set(letters_in_ascending)))
    print list(set(letters_in_ascending))


if __name__ == '__main__':
    main()
