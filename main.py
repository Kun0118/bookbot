import sys
from stats import count_words
from stats import count_chars
from stats import letter_sort

def get_book_text(filePath):
    with open(filePath, "r") as file:
        file_contents=file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # Count words
    words = count_words(text)
    word_count = len(words)

    # Count characters
    char_counts = count_chars(text)

    # Sort characters
    sorted_chars = letter_sort(char_counts)

    # Print report
    print("=== Book Report ===")
    print(f"Analyzing book found at {book_path}\n")

    print("--- Word Count ---")
    print(f"Found {word_count} total words\n")

    print("--- Character Count ---")
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():     # safeguard
            print(f"{ch}: {num}")

    print("\n=== End of Report ===")



if __name__ == "__main__":
    main()
