#%% Sorting
# Multiline strings
text="""
This is an example of a long,
multiline string, such as a paragraph,
entered as a string constant into a Python
program.
"""
# %%
from collections import Counter

words = text.split()
print(words)

# Sorting 
sorted_words = sorted(words)
print(sorted(words))
# %%
# Variations on sorting
sorted_words_rev = sorted(words, reverse=True)
print(sorted_words_rev)
# %%
counts = Counter(words)

for x in counts:
    print(f"{x}: {counts[x]}")
# %%
# Sorting by counts
sorted_counts = sorted(counts.items())
print(sorted_counts)
# %%
# Sorting keys
def key_fn(x):
    return x[1]

sorted_counts = sorted(counts.items(),key=key_fn)
print(sorted_counts)

# %%
#
sorted_counts = sorted(counts.items(),key=key_fn,reverse=True)
print(sorted_counts)
# %%
# lambda functions
sorted_counts = sorted(counts.items(),key=lambda x: x[1],reverse=True)

# Extracting the 10  most common words
[x[0] for x in sorted_counts[:10]]
# %%
counts.most_common(10)
# %%
# Building a sorted dictionary
sorted_dict = dict(sorted_counts)
sorted_dict = {x[0]:x[1] for x in sorted_counts}
# %%
sorted_dict

# %%
