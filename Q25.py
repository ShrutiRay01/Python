# Write a program that copies the contents of one text file to another.

def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as f_source:
            # Read all content from the source file
            content = f_source.read()
            
            # Open the destination file for writing
            with open(destination_file, 'w') as f_dest:
                # Write the content to the destination file
                f_dest.write(content)
        
        print(f"Successfully copied content from '{source_file}' to '{destination_file}'.")
    
    except FileNotFoundError:
        print("Error: One or both files not found.")

# Example usage:
source_file = 'source.txt'        # Replace with your source file path
destination_file = 'destination.txt'  # Replace with your destination file path

# Call the function to copy contents from source to destination file
copy_file(source_file, destination_file)
