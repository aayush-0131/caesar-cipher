# cipher.py (Updated Version)

def process_text(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text (str): The input string to process.
        shift (int): The number of positions to shift letters.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The processed (encrypted or decrypted) string.
    """
    if mode == 'decrypt':
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char
            
    return result

def main():
    """Main function to run the command-line interface."""
    print("--- Caesar Cipher Tool ---")
    
    while True:
        print("\nWhat would you like to do?")
        raw_choice = input("Choose (e)ncrypt, (d)ecrypt, or (q)uit: ").lower().strip()

        if raw_choice.startswith('q'):
            print("Goodbye!")
            break
        
        mode = None
        if raw_choice.startswith('e'):
            mode = 'encrypt'
        elif raw_choice.startswith('d'):
            mode = 'decrypt'
        else:
            print("Invalid choice. Please try again.")
            continue

        # Get user input for the message
        message = input("Enter your message: ")

        # Get and validate the shift key
        while True:
            try:
                shift_key = int(input("Enter the shift key (a number): "))
                break
            except ValueError:
                print("Invalid shift key. Please enter a whole number.")

        # Process the text using the determined mode
        processed_message = process_text(message, shift_key, mode)
        
        # Capitalize the result type for display
        result_type = mode.capitalize()
        print(f"\n{result_type}ed Message: {processed_message}")

if __name__ == "__main__":
    main()