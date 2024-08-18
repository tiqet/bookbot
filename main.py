def sort_on(d):
    return (-d[1], d[0])

file = "books/frankenstein.txt"
with open(file) as f:
    book = f.read()
    words = book.lower().split()

    # Count occurrences of each letter in the book
    letter_counts = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

    # Print frequencies of each letter in descending order
    print()
    print(f"--- Begin report of {file} ---")
    print(f"{len(words)} words found in the document")
    print()
    sorted_counts = sorted(letter_counts.items(), key=sort_on)
    for letter, count in sorted_counts:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

