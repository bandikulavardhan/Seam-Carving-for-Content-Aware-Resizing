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