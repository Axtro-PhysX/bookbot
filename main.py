def main():
    # Open a file relative to your local environment
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()