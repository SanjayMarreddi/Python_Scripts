
def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):

    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    
    d = {}
    for line in open(filename):
        word = line.strip()
        t = signature(word)
                            # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]   #d[t] is a list of words.
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
    d: map from words to list of their anagrams
    """
                        # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()
    b=t[::-1]
    # print the sorted list
    for x in b:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res



anagram_map = all_anagrams('words2.txt')
print_anagram_sets_in_order(anagram_map)

eight_letters = filter_length(anagram_map, 8)
print_anagram_sets_in_order(eight_letters)
    
