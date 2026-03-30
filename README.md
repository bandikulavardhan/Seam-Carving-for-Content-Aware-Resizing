# Seam Carving for Content-Aware Resizing

## Project Description
This project is an image resizing tool written in Python. Standard image resizing simply crops or squashes a picture. This program uses a "content-aware" algorithm to resize images. It calculates the energy of each pixel and uses Dynamic Programming to find and remove the least noticeable paths of pixels (called seams) from the top to the bottom, or from the left to the right.

This was built as a collaborative pair-programming project for our Object-Oriented Programming & Data Structures course.

## Core Features
* **Dual-Gradient Energy Calculation:** Determines the visual importance of every pixel based on the color differences of its neighbors.
* **Vertical and Horizontal Seam Finding:** Uses Dynamic Programming on a Directed Acyclic Graph (DAG) to find the shortest path of low-energy pixels.
* **Content-Aware Resizing:** Safely removes the targeted seams and creates a new, correctly sized image object without stretching the important parts of the picture.

## Project Files
* `seam_carver.py`: The main Object-Oriented class containing the image data and all the core algorithms.
* `test_seam_carver.py`: A script to test the tool. It creates a sample image, removes 20 vertical seams, and saves the new image.
* `AI_PROMPTS.md`: A log file that tracks all of our AI tool usage, including the problems we faced, the prompts we used, and how we modified the code.
