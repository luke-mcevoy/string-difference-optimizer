'''
Created on 10/4/18
@author:   Luke McEvoy
Pledge:    I pledge my honor I have abided by the Stevens Honor Code

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10


def fastED(S1, S2):
    memo = {}
    def helper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        elif S1 == '':
            answer = len(S2)
        elif S2 == '':
            answer = len(S1)
        elif S1[0] == S2[0]:
            answer = helper(S1[1:], S2[1:],memo)
        else:
            sub = 1 + helper(S1[1:], S2[1:], memo)
            dele = 1 + helper(S1[1:], S2, memo)
            insert = 1 + helper(S1, S2[1:], memo)
            answer = min(sub, dele, insert)
        memo[(S1, S2)] = answer
        return answer
    return helper(S1, S2, memo)

def getSuggestions(user_input):
    return map(lambda x: (fastED(user_input,x),x),words)

    '''
    -Find the distance of the user_input to words in library
    For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    # pass  # TODO

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
