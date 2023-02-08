#%%
# Problem
# - Read text from a file
# - Count the number of times each word occurs in the file
# - Find the N most common or least common words
# %%
# Tools
# Read the text from a file
with open("text.txt") as f:
    text = f.read()
# %%
# Split the text into words
words = text.split()
# %%
# Use a dictionary to count the words
counts = dict()
for x in words:
    if x in counts:
        counts[x] = counts[x]+1
    else:
        counts[x]=0

# %%
# Look at what you found
for x in words:
    print(f"{x}: {counts[x]}")
