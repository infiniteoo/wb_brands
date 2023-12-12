import os

# Function to combine text files from subfolders into one file
def combine_text_files(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(subdir, file)
                if file_path != output_file:  # Avoid adding the output file to itself
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        output.write(input_file.read())

# Function to filter out duplicate lines from a text file
def filter_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    
    unique_lines = set(lines)  # Use a set to automatically remove duplicates

    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(unique_lines)

# Define the root directory containing subfolders with text files
root_directory = './data'

# Combine text files into one big file
combined_file = 'combined.txt'
combine_text_files(root_directory, combined_file)
print(f'Combined {combined_file}')

# Filter out duplicate lines
filtered_file = 'wb_model.txt'
filter_duplicates(combined_file, filtered_file)
print(f'Filtered {filtered_file}')
