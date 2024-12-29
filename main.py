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
    
    # Convert the dictionary to a list of dictionaries for easy sorting
    char_list = []
    for char, count in char_dict.items():
        char_list.append({'char': char, 'num': count})
    
    # Sort the list by number of occurrences in descending order
    char_list.sort(key=lambda x: x['num'], reverse=True)

    return char_list

def main():
    # Open the file
    text_path = "books/frankenstein.txt"
    with open(text_path) as file:
        file_contents = file.read() # Read the file

        # Store a count of strings in a variable
        count = word_count(file_contents)

        # Print the count
        print("--- Begin report of text file ---")
        print("\n")
        print(f"{count} words found in document.")
        print("\n")

        # Get sorted list of character frequencies
        char_list = count_chars(file_contents)

        # Create a sorted report of characters
        print("Character frequency report:")
        print("----------------------------")

        for char_info in char_list:
            print(f"The '{char_info['char']}' character was found {char_info['num']} times.")

main()