book_path = "books/frankenstein.txt"


def main():
    content = read_text(book_path)
    word_count = count_words(content)
    char_count = count_chars(content)
    filtered = {k: v for k, v in char_count.items() if k.isalpha()}
    ordered = dict(sorted(filtered.items(), key=lambda item: item[1], reverse=True))
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in ordered.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def read_text(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    words = content.split()
    return(len(words))

def count_chars(content):
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



    # Inefficient solution

    # charac = {
    #     "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
    #     "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
    #     "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
    #     "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    #     "y": 0, "z": 0
    # }
#   for c in lowered_content:
#     for key, value in charac.items():
#         if c == key:
#             charac[key] = value + 1

main()
