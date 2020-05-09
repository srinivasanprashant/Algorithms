# The goal of this function is to take two strings and return whether they are anagrams.


def anagram_checker(word1,word2):
    sorted_word1 = list(word1)
    sorted_word2 = list(word2)

    # Sort the lists so we can compare. Sorting can be done in O(n log n) complexity.
    sorted_word1.sort()
    sorted_word2.sort()

    if sorted_word1 == sorted_word2:
        matches = True
    else:
        matches = False

    return matches


if __name__ == "__main__":
    string1 = 'eartha'
    string2 = 'hearts'
    print("Are " + string1 + " and " + string2 + " anagrams?")
    print(anagram_checker(string1, string2))
