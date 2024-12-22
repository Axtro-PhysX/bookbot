def word_count(file):
    counted = len(file.split())
    return counted

def count_chars(file):
    # We need to add code here
    pass

def main():
    # Open the file
    text_path = "books/frankenstein.txt"
    with open(text_path) as f:
        file_contents = f.read() # Read the file

        # Store a count of strings in a variable
        count = word_count(file_contents)

        # Print the count
        print(f"{count} words found in document.")

main()