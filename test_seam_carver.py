import os
from PIL import Image, ImageDraw
from seam_carver import SeamCarver

def create_test_image(filename, width=100, height=100):
    """Creates a basic test image with some patterns."""
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    # Draw a simple rectangle in the middle
    draw.rectangle([width//4, height//4, width*3//4, height*3//4], fill='blue')
    # Draw a line
    draw.line([0, 0, width, height], fill='red', width=2)
    img.save(filename)
    print(f"Created test image: {filename} ({width}x{height})")
    return img

def main():
    input_file = "test_input.jpg"
    output_file = "test_output.jpg"
    
    # 1. Create a test image
    if not os.path.exists(input_file):
        create_test_image(input_file, 100, 100)
    
    # 2. Load image and initialize SeamCarver
    print("Loading image and initializing Seam Carver...")
    original_image = Image.open(input_file)
    carver = SeamCarver(original_image)
    
    print(f"Original size: {carver._width}x{carver._height}")
    
    # 3. Remove some vertical seams
    seams_to_remove = 20
    print(f"Removing {seams_to_remove} vertical seams...")
    for i in range(seams_to_remove):
        seam = carver.find_vertical_seam()
        carver.remove_vertical_seam(seam)
        if (i+1) % 5 == 0:
            print(f"  Removed {i+1} seams...")

    print(f"New size: {carver._width}x{carver._height}")
    
    # 4. Save the result
    carver._image.save(output_file)
    print(f"Saved processed image to: {output_file}")

if __name__ == "__main__":
    main()
