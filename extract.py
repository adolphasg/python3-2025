import os
from pprint import pprint  # To print in a more readable format
from datetime import datetime

def collect_file_info(path="."):
    """
    Collects information (file name and size) about all files in the specified path.
    This includes files in nested folders (recursively).
    
    Args:
        path (str): The directory path to scan. Defaults to the current directory.

    Returns:
        list: A list of dictionaries with file 'name' and 'size' in bytes.
    """
    file_info_list = []  # This will store dictionaries of file data

    # Walk through the directory tree recursively
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # Construct full file path
            full_path = os.path.join(dirpath, filename)

            try:
                # Get file size
                size = os.path.getsize(full_path)

                # Append dictionary with file info
                file_info_list.append({
                    "path": full_path,
                    "size": size
                })
            except FileNotFoundError:
                # If a file is deleted or moved while iterating, skip it
                continue
            except PermissionError:
                # Skip files we don't have permission to access
                continue

    return file_info_list

# ===== FOUNDATIONAL USAGE =====
# This block runs only if the script is executed directly
if __name__ == "__main__":
    # Call the function without parameters to use the current directory
    files = collect_file_info()

    # Print the list of file information
    print("File information collected:\n")
    for file in files:
        print(file)
