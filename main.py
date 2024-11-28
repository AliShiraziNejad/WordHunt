from utils import *


def main():
    input_string = input("Enter the 16 letters of the grid (e.g., ABCDEFGHIJKLMNOP): ").strip().upper()
    if len(input_string) != 16 or not input_string.isalpha():
        print("Please enter exactly 16 alphabetic characters.")
        return
    grid = create_grid(input_string)

    dictionary = load_dictionary('Collins Scrabble Words (2019).txt')
    trie_root = build_trie(dictionary)

    found_words = find_words_with_trie(grid, trie_root)

    sorted_words = sort_words(found_words)

    print("\nWords found:")
    for word in sorted_words:
        print(word)
    print(f"\nTotal words found: {len(sorted_words)}")


if __name__ == "__main__":
    main()
