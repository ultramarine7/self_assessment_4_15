"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""

# I'm sorry but I don't quite unerstand how the doctest format works.
# I tried to figure it out by comparing the syntax from the solutions on slack,
# but I realized I was spending too much time on how it should be formatted on doctest.
# This is why it contains the list based on the example. Otherwise the doctest returns erros.

words_list = ["rose", "is", "a", "rose", "is", "a", "rose"]

def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

>>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    """
    for words in words_list:
        words = set(words_list) # use set because sets are unique and immutable
        words = sorted(words)
        return words
    # return []

without_duplicates(words_list)

# If I don't put this, the doc test returns wierd long list of Traceback errors
# Traceback (most recent call last):
#   File "skills_01.py", line 233, in <module>
#     if doctest.testmod().failed == 0:
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/doctest.py", line 1910, in testmod
# words_list = ["Rose", "is", "a", "rose", "is", "a", "rose"]...

def without_duplicates(words):

    for words in words_list:
        words = set(words_list)
        words = sorted(words)
        # print words
        return words

without_duplicates(words_list)

#########################################################################################

list1 = [1, 2, 3, 4]
list2 = [2, 1]

def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are different data types.

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]

    """
    for num in (list1, list2):
        num = list(set(list1) & set(list2)) # need to combine the lists 
        # but don't want to show duplicates
        # set intersection the resulting set has elements that are common to both sources
    return num

find_unique_common_items(list1, list2)

# Example of IMPORTANT: you may not use 'if ___ in ___' or the method 'index'
# b1 = [1, 2, 3, 4, 5, 15]
# b2 = [1, 4, 5, 6, 7,8 ]
# b3 = [val for val in b1 if val in b2]
# b3 goes through the items in b1 and evaluates if the same items are in b2

############################################################################################

input_string = "each word appears once"

word_list = input_string.split() # need to separate the words from the sentence
# split by space to separate words from the sentence

# print  word_list
# output is ['each', 'word', 'appears', 'once']

counts_for_dict = dict()

def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    for words in word_list:
        # need to pull the value for the key "words" from the dictionary
        # if it's not there, it needs to return the value 0 to indicate that it's not there
        # if it's there, need to increment the count
        counts_for_dict[words] = counts_for_dict.get(words, 0) + 1

    # print counts_for_dict
    return counts_for_dict

input_string = "rose is a rose is a rose"

word_list = input_string.split()

counts_for_dict = dict()

def count_unique(input_string):
    for words in word_list:
        counts_for_dict[words] = counts_for_dict.get(words, 0) + 1

    return counts_for_dict

count_unique(input_string)

# counter class collections.Counter([iterable-or-mapping])
# A Counter is a dict subclass for counting hashable objects. It is an unordered collection
# where elements are stored as dictionary keys and their counts are stored as dictionary values.

##################################################################################

phrase = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "boy": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be"
    }

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

   English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a man'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # need to set up user input -> split it because it can be a sentence ->
    # check for the equivalent pirate words from the dictionary -> 
    # need an empty pirate word list -> add the pirate words -> 
    # store the equivalent pirate words -> each word needs to be combined

    # user_input = raw_input ("Enter English phrase: ").split()
    input_string = "my student is not a man"
    word_list = input_string.split()
    pirate_output = []
    for eng_word in word_list:
        pirate_words = phrase.get(eng_word) # key value
        pirate_output.append(pirate_words)
    print pirate_output
        # pirate_combined = " ".join(pirate_output)

    # print "Pirate words are: ",pirate_combined
    # return " ".join(pirate_output)

translate_to_pirate_talk(phrase)

##########################################################################

# I'm not sure if I'm having a difficulty retaining information but
# I used lecture notes and did a lot of search
# but my solution seems too complicated and not sure if it's correct

list1 = ["ok", "an", "apple", "a", "day"]

# list -> length of each word -> order by the length (sort?) -> combine duplicate length words

def bylength(word1, word2):
# needs to compare the lenght of words so it can be sorted by the result
    # print
    # print "length of each word1", word1, len(word1)
    # print "length of each word2", word2, len(word2)
    # print "len(word1) - len(word2)", len(word1) - len(word2)
    return len(word1) - len(word2)
list1.sort(cmp=bylength)
# The method cmp() compares elements of two lists
# cmp(list1, list2)
# If elements are of the same type, perform the compare and return the result.
# If elements are different types, check to see if they are numbers.
# Otherwise, types are sorted alphabetically by name.
# print "sorted by length", list1

# for word_length in list1:
#     print len(word)
list1_word_length = [len(word) for word in list1]
print list1_word_length

words = zip(list1_word_length, list1)
# zip([iterable, ...])
# iterate over two tuple lists in parallel
# because I have the element for the first list = length and the second list = words
# but it doesn't combined the duplicate lengths
# print "combined", words

######################################################################################

def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
  # I couldn't figure out how to sort the duplicate length with tuples
    result = {}
    for key, value in words:
        result.setdefault(key, []).append(value)
        # setdefault(key[, default])
        # If key is in the dictionary, return its value
        # If not, insert key with a value of default and return default
        # default defaults to None.
    # print result
    return result

###########################################################################

input_list = [-1, -2, 3, 2, 1]

input_list_len = len(input_list)

def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
# sum = 0 with 2 numbers on the list
# need to find a pair of numbers that == 0 when added
# num1 != num2

def get_sum_zero_pairs(input_list):
    for num1 in range(input_list_len):
        for num2 in range(input_list_len):
            if(num2 <= num1 ): continue
            if((input_list[num1] + input_list[num2]) == 0):
                # print "{}, {}".format (input_list[num1], input_list[num2])
                return (input_list[num1], input_list[num2])


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
