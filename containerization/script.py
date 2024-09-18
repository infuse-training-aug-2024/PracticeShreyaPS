import sys
import os
import numpy as np
from PIL import Image, ImageOps

# Function to manipulate a numpy array
def manipulate_array(arr):
    return np.sqrt(arr)  # Example operation: square root of elements

# Function to resize an image using Pillow
def process_image(image_path, output_path, size):
    img = Image.open(image_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)
    print(f"Image saved to {output_path} with size {size}")

# Main function to handle arguments, environment variables, and operations
def main():
    # Retrieve environment variable (for example, a default image size)
    default_size = os.getenv('IMAGE_SIZE', '200x200')  # Example: 200x200
    default_size = tuple(map(int, default_size.split('x')))

    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <array_length> <image_path> <output_image_path>")
        sys.exit(1)

    array_length = int(sys.argv[1])
    image_path = sys.argv[2]
    output_image_path = sys.argv[3]

    # Create a random numpy array and manipulate it
    arr = np.random.rand(array_length)
    print(f"Original array:\n{arr}")
    manipulated_array = manipulate_array(arr)
    print(f"Manipulated array (square roots):\n{manipulated_array}")

    # Process the image: resize to default or specified size
    process_image(image_path, output_image_path, default_size)

if __name__ == "__main__":
    main()
