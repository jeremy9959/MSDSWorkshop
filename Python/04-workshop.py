#%%
# Class unifies data and algorithms
# First pass:
#    data is a string
#    we want to get a count of how many times each word occurs
#    we want to know the most and least common sets of N words
#    we want to be able to configure our code with options:
#       - what is a word?
#       - case sensitive or not?

import re
from collections import Counter


class Vectorizer:
    """
    A class for counting occurrences of a pattern in a string.

    Options:
        word_pattern: a regular expression defining the words to be counted
        case_sensitive: true/false
        stop_words: words to be ignored

    Attributes:
        text: the text being analyzed
        counts: a dictionary giving the count

    Methods:
        vocabulary: returns the counted words as a list in descending order of frequency
        most_common: returns the first N elements of the vocabulary
        least_common: returns the last N elements of the vocabulary

    """

    def __init__(
        self, text, word_pattern=r"\b\w\w+\b", case_sensitive=False, stop_words=[]
    ):
        """
        Constructor for Vectorizer Class
            - text: string to be analyzed
            - word_pattern: regular expression defining a word (default = \b\w\w+\b, matching words of length at least 2)
            - case_sensitive: default = False
            - stop_words: list of words to ignore (default empty)
        """
        self.text = text
        if case_sensitive:
            words = re.findall(word_pattern, text)
        else:
            words = re.findall(word_pattern, text.lower())
        self.counts = dict(
            sorted(Counter(words).items(), reverse=True, key=lambda x: x[1])
        )
        for stopword in stop_words:
            if case_sensitive:
                self.counts.pop(stopword, None)
            else:
                self.counts.pop(stopword.lower(), None)

    def vocabulary(self):
        "Returns a list of the words that were found in descending order of frequency"
        return list(self.counts.keys())

    def most_common(self, N=5):
        "Return first N words in the vocabulary"
        return list(self.counts.keys())[:N]

    def least_common(self, N=5):
        "Return last N vocabulary words"
        return list(self.counts.keys())[-N:]


# %%
X=Vectorizer("this is a string which has the word this in it several times")
# %%
X.vocabulary()
# %%
X.most_common(3)
# %%
X.least_common(2)
# %%
X.counts
# %%
Y=Vectorizer("another example, with the word is in it repeated as many times as it is.",stop_words=["is"])
# %%
Y.vocabulary()
# %%
Y.most_common(3)
# %%
Y.text

# %%
X.text
# %%
X.counts
# %%
X.text
# %%
