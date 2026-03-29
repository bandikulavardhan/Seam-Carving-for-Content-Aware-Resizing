def find_vertical_seam(self):
        """Finds the lowest energy vertical path from top to bottom."""
        # Create a 2D grid to store the minimum cost to reach each pixel
        # and another grid to remember the path (which pixel we came from)
        cost = [[0.0] * self._width for _ in range(self._height)]
        edge_to = [[0] * self._width for _ in range(self._height)]

        # The first row's cost is just the energy of those pixels
        for x in range(self._width):
            cost[0][x] = self.energy(x, 0)

        # Fill the cost table row by row from top to bottom
        for y in range(1, self._height):
            for x in range(self._width):
                # Check the 3 pixels directly above this one
                best_prev_x = x
                min_prev_cost = cost[y - 1][x]

                # Check top-left
                if x > 0 and cost[y - 1][x - 1] < min_prev_cost:
                    min_prev_cost = cost[y - 1][x - 1]
                    best_prev_x = x - 1

                # Check top-right
                if x < self._width - 1 and cost[y - 1][x + 1] < min_prev_cost:
                    min_prev_cost = cost[y - 1][x + 1]
                    best_prev_x = x + 1

                # Add this pixel's energy to the best path cost so far
                cost[y][x] = self.energy(x, y) + min_prev_cost
                # Remember how we got here so we can trace back later
                edge_to[y][x] = best_prev_x

        # Find the pixel in the bottom row with the lowest total cost
        min_bottom_cost = float('inf')
        best_bottom_x = 0
        for x in range(self._width):
            if cost[self._height - 1][x] < min_bottom_cost:
                min_bottom_cost = cost[self._height - 1][x]
                best_bottom_x = x

        # Trace the path back from bottom to top
        seam = [0] * self._height
        current_x = best_bottom_x
        for y in range(self._height - 1, -1, -1):
            seam[y] = current_x
            current_x = edge_to[y][current_x]

        return seam

def find_horizontal_seam(self):
        """Finds the lowest energy horizontal path from left to right."""
        # Create a 2D grid for costs and a grid to remember the path
        cost = [[0.0] * self._width for _ in range(self._height)]
        edge_to = [[0] * self._width for _ in range(self._height)]

        # The first column's cost is just the energy of those pixels
        for y in range(self._height):
            cost[y][0] = self.energy(0, y)

        # Fill the table column by column from left to right
        for x in range(1, self._width):
            for y in range(self._height):
                # Check the 3 pixels directly to the left of this one
                best_prev_y = y
                min_prev_cost = cost[y][x - 1]

                # Check top-left
                if y > 0 and cost[y - 1][x - 1] < min_prev_cost:
                    min_prev_cost = cost[y - 1][x - 1]
                    best_prev_y = y - 1

                # Check bottom-left
                if y < self._height - 1 and cost[y + 1][x - 1] < min_prev_cost:
                    min_prev_cost = cost[y + 1][x - 1]
                    best_prev_y = y + 1

                # Add energy and remember the path
                cost[y][x] = self.energy(x, y) + min_prev_cost
                edge_to[y][x] = best_prev_y

        # Find the pixel in the rightmost column with the lowest cost
        min_right_cost = float('inf')
        best_right_y = 0
        for y in range(self._height):
            if cost[y][self._width - 1] < min_right_cost:
                min_right_cost = cost[y][self._width - 1]
                best_right_y = y

        # Trace the path back from right to left
        seam = [0] * self._width
        current_y = best_right_y
        for x in range(self._width - 1, -1, -1):
            seam[x] = current_y
            current_y = edge_to[current_y][x]

        return seam

def remove_vertical_seam(self, seam):
        """Removes a vertical seam from the image and updates its size."""
        # Check to make sure the seam array is the right size
        if len(seam) != self._height:
            raise ValueError("Seam length must match the image height.")

        # Create a new blank image that is 1 pixel narrower
        new_width = self._width - 1
        new_image = Image.new('RGB', (new_width, self._height))

        # Loop through every row (y) and column (x)
        for y in range(self._height):
            seam_x = seam[y]  # The pixel we need to skip in this row
            for x in range(self._width):
                if x < seam_x:
                    # Copy pixels that are to the left of the seam
                    pixel_color = self._image.getpixel((x, y))
                    new_image.putpixel((x, y), pixel_color)
                elif x > seam_x:
                    # Copy pixels that are to the right of the seam
                    # We shift them left by 1 (x - 1) to close the gap
                    pixel_color = self._image.getpixel((x, y))
                    new_image.putpixel((x - 1, y), pixel_color)

        # Replace the old image and width with the new ones
        self._image = new_image
        self._width = new_width

def remove_horizontal_seam(self, seam):
        """Removes a horizontal seam from the image and updates its size."""
        if len(seam) != self._width:
            raise ValueError("Seam length must match the image width.")

        # Create a new blank image that is 1 pixel shorter
        new_height = self._height - 1
        new_image = Image.new('RGB', (self._width, new_height))

        # Loop through every column (x) and row (y)
        for x in range(self._width):
            seam_y = seam[x]  # The pixel we need to skip in this column
            for y in range(self._height):
                if y < seam_y:
                    # Copy pixels above the seam
                    pixel_color = self._image.getpixel((x, y))
                    new_image.putpixel((x, y), pixel_color)
                elif y > seam_y:
                    # Copy pixels below the seam, shifted up by 1 (y - 1)
                    pixel_color = self._image.getpixel((x, y))
                    new_image.putpixel((x, y - 1), pixel_color)

        # Replace the old image and height with the new ones
        self._image = new_image
        self._height = new_height