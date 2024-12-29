def word_count(file):
    counted = len(file.split())
    return counted

def count_chars(file):
    # Create empty dictionary to store char count
    lowered = file.lower()
    char_dict = {}

    # Loop through each char in the file contents
    for c in lowered:
        # If char was seen before, increment count by 1
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
        print(f"{count} words found in document.")

        # Print a new line for clarity
        print("\n")

        # Return character dictionary
        counted_chars = count_chars(file_contents)
        print(f"List of characters: {counted_chars}")

main()