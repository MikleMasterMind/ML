def check(x: str, file: str):
    words = dict()
    x = sorted(x.split())
    for w in x:
        w = w.lower()
        if w in words:
            words[w] += 1
        else:
            words[w] = 1
    with open(file, 'w') as file_out:
        for word, count in words.items():
            print(word, count, file=file_out)

