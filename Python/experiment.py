# function to find 10 most common words in a string
def most_common(text,N):
    counts = tokens(text)
    return [x[0] for i, x in enumerate(sorted(counts.items(),key=lambda x: -x[1])) if i<N]