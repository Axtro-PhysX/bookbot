def main():
    # Open the file
    text_path = "books/frankenstein.txt"
    with open(text_path) as f:
        file_contents = f.read() # Read the file

        # Store a count of strings in a variable
        count = word_count(file_contents)

        # Print the count
        print(f"{count}")
    
def word_count(file):
    counted = len(file.split())
    return counted
    
main()