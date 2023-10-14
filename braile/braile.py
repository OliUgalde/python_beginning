# def solution(text):
#     # Define a dictionary to represent English letters and numbers and their Braille equivalents
#     braille_map = {
#         'a': "100000", 'b': "101000", 'c': "110000",
#         'd': "110100", 'e': "100100", 'f': "111000",
#         'g': "111100", 'h': "101100", 'i': "011000",
#         'j': "011100", 'k': "100010", 'l': "101010",
#         'm': "110010", 'n': "110110", 'o': "100110",
#         'p': "111010", 'q': "111110", 'r': "101110",
#         's': "011010", 't': "011110", 'u': "100011",
#         'v': "101011", 'w': "011101", 'x': "110011",
#         'y': "110111", 'z': "100111",
#         '0': "001110", '1': "100000", '2': "110000",
#         '3': "100100", '4': "100110", '5': "100010",
#         '6': "110100", '7': "110110", '8': "110010",
#         '9': "010100"
#     }

#     # Translate English text into Braille
#     result = ''
#     for char in text:
#         char = char.lower()
#         if char in braille_map:
#             result += braille_map[char] + ' '
#         else:
#             # If the character is not recognized, you can handle it accordingly
#             result += '      '  # Six spaces for an unrecognized character

#     return result.strip()  # Remove trailing space

# # Example usage:
# english_text = "The quick brown fox jumps over the lazy dog"
# translated_text = solution(english_text)
# print(translated_text)

# Define a dictionary to represent English letters and numbers and their Braille equivalents
braille_map = {
    'a': "100000", 'b': "101000", 'c': "110000",
    'd': "110100", 'e': "100100", 'f': "111000",
    'g': "111100", 'h': "101100", 'i': "011000",
    'j': "011100", 'k': "100010", 'l': "101010",
    'm': "110010", 'n': "110110", 'o': "100110",
    'p': "111010", 'q': "111110", 'r': "101110",
    's': "011010", 't': "011110", 'u': "100011",
    'v': "101011", 'w': "011101", 'x': "110011",
    'y': "110111", 'z': "100111", ' ': "000000",
    '0': "001110", '1': "100000", '2': "110000",
    '3': "100100", '4': "100110", '5': "100010",
    '6': "110100", '7': "110110", '8': "110010",
    '9': "010100"
}

# Create a lambda function to translate a single character to Braille
translate_char_to_braille = lambda char: braille_map.get(char.lower(), '      ')

# Create a lambda function to translate an entire text to Braille
translate_text_to_braille = lambda text: ' '.join(map(translate_char_to_braille, text))

# Example usage:
english_text = "code"
translated_text = translate_text_to_braille(english_text)
#print(translated_text)

def sort_string_into_columns(input_string, num_columns=3):
    # Initialize empty rows
    rows = [''] * num_columns

    # Iterate through the characters and distribute them into columns
    for index, char in enumerate(input_string):
        current_row = index % num_columns
        rows[current_row] += char

    # Join the rows with newlines to create the sorted output
    sorted_string = '\n'.join(rows)

    return sorted_string

# Example usage:
sorted_columns = sort_string_into_columns(translated_text.replace(" ",""))
print(sorted_columns)

 