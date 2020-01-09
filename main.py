import pathlib

in_str = input('Enter words or parts: ')
tokens = in_str.split()

words = pathlib.Path('words.txt').read_text().splitlines()
found = []
for token in tokens:
    for word in words:
        if word.endswith(token) or word.startswith(token):
            found.append(word)

found.sort(key=lambda w: len(w))

print(found)
