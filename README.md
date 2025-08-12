# Task-7
Image resizer tool using python,pillow
Explanation of the Code
import os and from PIL import Image: These lines import the necessary libraries. os is used for interacting with the file system, like creating directories and joining paths. Image from the Pillow library (PIL) provides the functionality for opening, resizing, and saving images.

input_folder, output_folder, new_size: These variables define the paths for your source and destination folders and the target dimensions for resizing.

os.makedirs(output_folder, exist_ok=True): This function creates the output directory if it doesn't already exist. exist_ok=True prevents an error from being raised if the directory already exists.
os.listdir(input_folder): This function returns a list of all files and directories in the specified folder.

for filename in files:: This loop iterates through each file found in the input folder.
os.path.join(input_folder, filename): This is the recommended way to create a full file path that works across different operating systems.
if filename.lower().endswith(...): This check ensures that the script only attempts to process files with common image extensions, preventing errors from trying to open non-image files.

with Image.open(input_path) as img:: This opens the image file. Using a with statement ensures that the file is properly closed even if errors occur.
resized_img = img.resize(new_size): This is the core resizing command. It creates a new Image object with the specified dimensions.[2][5][6] The resize() method returns a new resized image.
resized_img.save(output_path): This saves the newly resized image to the specified path in the output folder.[2][5] Pillow automatically determines the image format based on the file extension.

try...except block: This is used for error handling. If Pillow encounters a problem with a file (e.g., it's corrupted or not a valid image), it will print an error message and continue to the next file instead of crashing the script.
