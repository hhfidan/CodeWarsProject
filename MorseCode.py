def decode_morse(morse_code):
    """
    Decodes a Morse code string into English text.
    
    Args:
        morse_code (str): The Morse code string to decode. Words are separated by 3 spaces ("   "), 
                          and letters are separated by 1 space (" ").
                          
    Returns:
        str: The decoded English text.
    """
    # Remove leading and trailing whitespace
    morse_code = morse_code.strip()
    
    # Split the Morse code into words (separated by 3 spaces)
    words = morse_code.split("   ")

    # List to hold decoded words
    decoded_message = []
    
    # Iterate through each word in Morse code
    for word in words:
        # Split the word into individual letters (separated by 1 space)
        letters = word.split()

        # Decode each letter and join them to form a word
        decoded_word = "".join(MORSE_CODE[letter] for letter in letters)

        # Append the decoded word to the result list
        decoded_message.append(decoded_word)
        
    # Join all words with a single space and return the decoded message
    return " ".join(decoded_message)
