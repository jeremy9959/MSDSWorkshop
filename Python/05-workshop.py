#%%
import numpy as np
import re
from collections import Counter


#%%
# Building a feature matrix for sentiment analysis
# Given a bunch of texts, construct a term frequency matrix
def build_matrix(texts):
    samples = {}
    vocab = {}
    for n, text in enumerate(texts):
        freqs = Counter()
        for word_match in re.finditer(r"\b\w\w+\b", text.lower()):
            word = word_match[0]
            if word in vocab:
                freqs[word] += 1
            else:
                vocab[word] = len(vocab)
                freqs[word] = 1
        samples[n] = freqs

    X = np.zeros(shape=(len(samples), len(vocab)))
    for row, row_freqs in samples.items():
        for word, freq in row_freqs.items():
            X[row, vocab[word]] = freq
    return X, vocab


# %%


# %%
def main():
    text1 = (
        "This is a sample piece of text for the first example and is a short sentence."
    )
    text2 = "This is another sample piece of text for the second example and is another example sentence."
    text3 = "Finally, this is a third sample piece of text for the last example."
    X, vocab = build_matrix([text1, text2, text3])
    print("Input Texts")
    for x in [text1, text2, text3]:
        print("\t", x)
    print("Vocabulary")
    print("\t", vocab)
    print("Matrix")
    print(X)


if __name__ == "__main__":
    main()

# %%

# %%

# %%
