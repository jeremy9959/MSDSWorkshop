#%% The Counter Class
from collections import Counter

#%%
with open("text.txt") as f:
    text = f.read()
words=text.split()

#%%
counts = Counter(words)

#%%
for x in words:
    print(f"{x}: {counts[x]}")
# %%

print("The most common words are")
print(counts.most_common(5))
for x in counts.most_common(5):
    print(f"{x[0]} occurs {x[1]} times")
# %%
# keys, values items
print(counts.keys())
print(counts.values())
# %%
print(counts.items())
# %%
