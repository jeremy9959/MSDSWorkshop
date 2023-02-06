#%%
with open("text.txt") as f:
    text = f.read()
# Regular Expressions
import re
# Letters; Numbers; Ranges; +; \w; \W; \b
# %%

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
from collections import Counter

# %%
wordlist=re.findall(r"\w+",text.lower())
# %%
words=Counter(wordlist)
# %%
for w in words:
    print(f"{w}: {words[w]}")
# %%
def tokens(text):
    words = re.findall(r"\w+",text)
    counts = Counter(words)
    return(counts)

counts = tokens(text)
for w in counts:
    print(f"{w}: {counts[w]}")
# %%
