def word_count(file):
    counted = len(file.split())
    return counted

def count_chars(file):
    # Create empty dictionary to store char count
    # Convert text to lowercase, so that 'A' and 'a' are counted the same
    lowered = file.lower()
    char_dict = {}

    # Loop through each char in the file contents
    for c in lowered:
        # Only count the character if it's a letter in the alphabet
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
        # If it's a new character, add it to the dictionary with +1 count
            else:
                char_dict[c] = 1    
    
    return char_dict

def main():
    # Open the file
    text_path = "books/frankenstein.txt"
    with open(text_path) as file:
        file_contents = file.read() # Read the file

        # Store a count of strings in a variable
        count = word_count(file_contents)

        # Print the count
        print("--- Begin report of text file ---")
        print(f"{count} words found in document.")
        print("\n") # Newline for clarity

        # Get character dictionary
        counted_chars = count_chars(file_contents)

        # Create a sorted report of characters
        print("Character frequency report:")
        # Convert dictionary items to a list of tuples (char, count)
        # Sort by count in descending order


main()