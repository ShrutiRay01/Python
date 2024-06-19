# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

# Example usage:
input_string = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"

# Checking prefix and suffix
starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix_to_check, suffix_to_check)

# Output the results
if starts_with_prefix:
    print(f"The string '{input_string}' starts with the prefix '{prefix_to_check}'.")
else:
    print(f"The string '{input_string}' does not start with the prefix '{prefix_to_check}'.")

if ends_with_suffix:
    print(f"The string '{input_string}' ends with the suffix '{suffix_to_check}'.")
else:
    print(f"The string '{input_string}' does not end with the suffix '{suffix_to_check}'.")
