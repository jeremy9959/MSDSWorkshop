#%% Variations
# Multiline strings
text="""
This is an example of a long,
multiline string, such as a paragraph,
entered as a string constant into a Python
program.
"""
# %%
# Sorting 
words = text.split()
print(words)
sorted_words = sorted(words)
print(sorted(words))
# %%
# Variations on sorting
sorted_words_rev = sorted(words, reverse=True)
print(sorted_words_rev)
# %%
# The counter class
from collections import Counter
counts = Counter(words)
print(counts)
# %%
# keys, values, and items
print(counts.keys())

# %%
print(counts.items())
# %%
print(counts.values())
# %%
#%%
# Reporting the counts
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
sorted_counts = sorted(counts.items(),key=lambda x: x[1])

# Extracting the 10  most common words
[x[0] for x in sorted_counts[:10]]
# %%
counts.most_common(10)
# %%
