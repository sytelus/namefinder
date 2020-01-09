import pathlib

in_str = input('Enter words or parts: ')
tokens = in_str.split()

words = set(pathlib.Path('words.txt').read_text().splitlines())
found = []
for token in tokens:
    for word in words:
        if len(word)>2 and (word.endswith(token) or word.startswith(token)):
            found.append((word, len(word)))

found.sort(key=lambda t: t[1])
for f in found:
    print(f)
