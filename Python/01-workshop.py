# %%

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
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)

# %%
# Look at what you found
for x in words:
    print(f"{x}: {counts[x]}")


# %%
def count_words(file):
    "returns a dictionary counting words in the file"
    count = {}
    with open(file) as f:
        text = f.read()
    words = text.split()
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count


# %%
answer = count_words("text.txt")
# %%
answer
# %%
