# The goal of this function is to take two strings and return whether they are anagrams.

def anagram_checker(word1,word2):
    sorted_word1 = list(word1)
    sorted_word2 = list(word2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches