"""
Find the longest duplicated substring in a below given string.
isthebananaofthegreatfruitlikepapayabutfruitofbraziliansoftheworldisineastwestnorthsouththegreatindiasealikn
"""

import collections

def main():
    string = 'isthebananaofthegreatfruitlikepapayabutfruitofbraziliansoftheworldisineastwestnorthsouththegreatindiasealikn'
    str_len = len(string)
    words = [string[i:j+1] for i in range(str_len) for j in range(i+1, str_len)]
    words_count = collections.Counter(words)

    #get only words which are repeating
    dup_words = [word for word in words_count if words_count[word] > 1]
    dup_words_length = [len(word) for word in dup_words]

    max_length = max(dup_words_length)
    dup_words_zip = zip(dup_words, dup_words_length)
    longest_repeating_words = [ word for word,length in dup_words_zip if length==max_length]
    print '*'*50
    print 'LONGEST REPEATING WORDS'
    print '*'*50
    for word in longest_repeating_words:
        print word

if __name__ == '__main__':
    main()

