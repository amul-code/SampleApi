def count_extraordinary_substrings(input_str):
    # Create a dictionary to map characters to their digit values
    char_to_digit = {
        'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2, 'f': 3, 'g': 3, 'h': 3,
        'i': 4, 'j': 4, 'k': 4, 'l': 5, 'm': 5, 'n': 5, 'o': 6, 'p': 6,
        'q': 6, 'r': 7, 's': 7, 't': 7, 'u': 8, 'v': 8, 'w': 8, 'x': 9, 'y': 9, 'z': 9
    }

    # Initialize the count of extraordinary substrings
    count = 0

    # Iterate through all possible substrings
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substring = input_str[i:j]
            # Calculate the sum of mapped values for characters in the substring
            mapped_sum = sum(char_to_digit[char] for char in substring)
            # Check if the sum is divisible by the length of the substring
            if mapped_sum % len(substring) == 0:
                count += 1

    return count

# Example usage:
input_str = input()
result = count_extraordinary_substrings(input_str)
print(result)  # Output: 6