# %%

from collections import Counter
import re

# load text from file

# %%
with open("text.txt") as f:
    text = f.read()
+
# %%
words = text.split()
print(words[:10])

# %%
counts = Counter(words)
for x in counts:
    print(f"{x}: {counts[x]}")


# %%
# Issues/critiques
print(f"Not very reusable in current form")
print(f"Case matters: \"the\" occurs {counts['the']} times and \"The\" occurs {counts['The']} times")
print(f"Sometimes we seem to include punctuation:   \"use,\" occurs {counts['use,']} times and \"use\" occurs {counts['use']} times")
print(f"Some of our words are really numbers like 9 or 43")
print(f"Some of our words are symbols like /\\\\s{{1}}/.")

# %%
# Second approximation
# Make this a function for reusability
# Select our words more carefully: what is a word?
# Allow case sensitivity to be an option.
# Exclude things that aren't "words"



# %%
def tokens(text):
    """
    Count occurrences of each word in a string and return a dictionary
    with words as keys and counts as values
    """
    words = text.split()
    counts = Counter(words)
    return counts
    
# %%
counts = tokens(text)

# %% 
# Keys and Items of a dictionary

# %%
print(counts.keys())
# %%
print(list(counts.values()))
# %%
print(counts.items())
# %%
words = counts.keys()

# %%
print(sorted(words))
# %%
sorted(list(counts.items()))
# %%
sorted(counts.items(),key=lambda x: x[1])
# %%
sorted(counts.items(),key=lambda x: -x[1])
# %%
[x[0] for x in sorted(counts.items(),key=lambda x: -x[1])]
# %%
[x[0] for i,x in enumerate(sorted(counts.items(),key=lambda x: -x[1])) if i<10 ]
# %%
def most_common(text,N):
    counts = tokens(text)
    return [x[0] for i, x in enumerate(sorted(counts.items(),key=lambda x: -x[1])) if i<N]
# %%
most_common(text,20)
# %%
def least_common(text,N):
    counts = tokens(text)
    return [x[0] for i,x in enumerate(sorted(counts.items())) if i<N]
# %%
least_common(text,10)
# %%

class Splitter:
    """
    A simple string tokenizer.

    ...
    Attributes
    ----------
    text : the text being analyzed
    counts : a python dictionary with keys the words in the text and values as the counts

    Methods
    ----------
    words() : a list of the words ocurring in the text
    n()     : the total number of distinct words in the text
    top(N)  : list of the N most frequently occurring words
    bottom(N) : list of the N least frequently occurring words
  
   
    """
    def __init__(self, text):
        """
        Initialize the object and store the counts dictionary
        """
        self.text = text
        self.counts = self.__tokens(text)
        return

    def __tokens(text):
        """
        split the text and compute the counts (private method)
        """
        words = text.split()
        counts = Counter(words)
        return counts

    def words(self):
        """
        return the words occurring in the text
        """
        return list(self.counts.keys())

    def n(self):
        """
        return the number of distinct words in the text
        """
        return len(self.counts)

    def top(self,N):
        """
        return a list of the N most common words
        """
        return [x[0] for i,x in enumerate(sorted(counts.items(),key=lambda x: -x[1])) if i<N]

    def bottom(self,N):
        """
        return a list of the N least common words
        """
        return [x[0] for i,x in enumerate(sorted(counts.items())) if i<N]

  
# %%
S = Splitter()
# %%
S.tokens(text)
# %%
S=Splitter(text)
# %%
S.text
# %%
S.counts
# %%
S.words()
# %%
S.n()
# %%
S.top(10)
# %%
S.bottom(20)
# %%
help(Splitter)
# %%
help(Splitter)
# %%
dir(Splitter)
# %%
help(Splitter)
# %%
help(tokens)
# %%
