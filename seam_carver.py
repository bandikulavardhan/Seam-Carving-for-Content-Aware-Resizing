from PIL import Image
import math

class SeamCarver:
    def __init__(self, image_path):
        """Loads the image and sets up the class."""
        # Open the image and make sure it is in RGB color mode
        # The underscore means this is a private field
        self._image = Image.open(image_path).convert('RGB')
        self._width = self._image.width
        self._height = self._image.height

    def width(self):
        """Returns the width of the image."""
        return self._width

    def height(self):
        """Returns the height of the image."""
        return self._height

    def energy(self, x, y):
        """Calculates the energy of a single pixel at (x, y)."""
        # Check if the pixel is actually inside the image
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            raise ValueError("Pixel is outside the image bounds.")

        # Border pixels get a fixed high energy of 1000.0
        if x == 0 or x == self._width - 1 or y == 0 or y == self._height - 1:
            return 1000.0

        # Get the RGB colors of the four neighbor pixels
        left_color = self._image.getpixel((x - 1, y))
        right_color = self._image.getpixel((x + 1, y))
        up_color = self._image.getpixel((x, y - 1))
        down_color = self._image.getpixel((x, y + 1))

        # Calculate the X and Y gradient squares
        x_grad_sq = self._calculate_gradient_square(left_color, right_color)
        y_grad_sq = self._calculate_gradient_square(up_color, down_color)

        # The total energy is the square root of the sum
        return math.sqrt(x_grad_sq + y_grad_sq)

    def _calculate_gradient_square(self, color1, color2):
        """Private helper method to do the color math."""
        # color1 and color2 are tuples like (Red, Green, Blue)
        red_diff = color1[0] - color2[0]
        green_diff = color1[1] - color2[1]
        blue_diff = color1[2] - color2[2]

        return (red_diff ** 2) + (green_diff ** 2) + (blue_diff ** 2)