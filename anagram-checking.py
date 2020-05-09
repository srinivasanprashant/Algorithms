# The goal of this function is to take two strings and return whether they are anagrams.


def anagram_checker(word1,word2):
    sorted_word1 = list(word1)
    sorted_word2 = list(word2)

    # Sort the lists so we can compare. Sorting can be done in O(nlogn) complexity.
    sorted_word1.sort()
    sorted_word2.sort()

    pos = 0
    matches = True

    while pos < len(word1) and matches:
        if sorted_word1[pos] == sorted_word2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


if __name__ == "__main__":
    print(anagram_checker('abcde1', 'edcba'))
