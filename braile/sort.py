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
input_string = "abcdefghijklmnopqrstuvwxyz"
sorted_columns = sort_string_into_columns(input_string)
print(sorted_columns)
