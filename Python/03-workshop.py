#%%
# Regular Expressions
from collections import Counter
import re

#%%
with open("text.txt") as f:
    text = f.read()

# 
# Letters, Numbers match themselves
# + means one or more of the preceeding
# * means 0 or more of the preceding
# [] groups things ([A-Z]+ matches a sequence of one or more capital letters);
#  \w matches "word" characters
# \W matches non-word characters
# \b matches boundaries (end or start of string)
# {5} matches 5 times
# \s matches whitespace
# \S matches non-whitespace

#%% 
astrings = re.findall(r"a\w+",text)
print(astrings)

awords = re.findall(r"\ba\w+\b",text)
print(awords)

#%%
re.findall(r"\w+",text)
# %%
re.findall(r"\w+",text.lower())
# %%
# %%

# %%
# finditer
# match objects
# x a match object: x[0] returns the match; x.span() returns (start, end) of the match
for x in re.finditer(r"\w+",text):
    print(x[0])

#%%
words = re.findall(r"\b\w\w+\b",text.lower())
counts = Counter(words)
sorted_words = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


# %%
sorted_words
# %%
