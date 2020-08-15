'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC

    #count = 0

    if len(word) < 2:
        #print('0,1,2 case')
        return 0
    else:
        if word[-2:] == 'th':
            # print('th')
            return count_th(word[:(len(word)-1)]) + 1
        else:
            return count_th(word[:len(word)-1])


# word.count('th')
print(count_th('jakthsldtkhthth'))
