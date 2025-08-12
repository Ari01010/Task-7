import os
from PIL import Image

# Define the input and output folders
input_folder = 'original_images'
output_folder = 'resized_images'

# Define the desired new size
new_size = (800, 600)  # (width, height)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
files = os.listdir(input_folder)

# Loop through each file in the input folder
for filename in files:
    # Construct the full file path
    input_path = os.path.join(input_folder, filename)

    # Check if the file is an image (you can add more extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        try:
            # Open the image using Pillow
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize(new_size)

                # Construct the output file path
                output_path = os.path.join(output_folder, filename)

                # Save the resized image
                resized_img.save(output_path)
                print(f"Successfully resized {filename} and saved to {output_folder}")
        except Exception as e:
            print(f"Could not resize {filename}: {e}")
# After the script finishes, you will find all the resized images in the resized_images folder.
print("\nBatch image resizing complete.")
