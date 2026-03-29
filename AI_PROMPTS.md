# AI Prompts

This file is used to track the usage of AI tools throughout the project. It logs the specific prompts provided and the context of those interactions to ensure transparency, accountability, and project documentation standards.

## Prompts Log

| Date | AI Tool Used | Specific Prompt | Context & Outcome |
| :--- | :--- | :--- | :--- |
| 2026-03-29 | Antigravity (Gemini) | "Create the required file for tracking AI use: AI_PROMPTS.md" | Initial creation of the AI usage tracking document. |

Problem: We were stuck on how to implement the Dynamic Programming algorithm to find the shortest vertical path.
Prompt: "Write a Python method using Dynamic Programming to find the vertical seam. It must use the self.energy(x, y) method Student A wrote and return a list of x-coordinates.".
Modifications: I checked the AI's math to make sure it handles the left and right edges correctly so it doesn't crash when looking for top-left or top-right pixels. I integrated it directly into our SeamCarver class.

Problem: The seam_carver.py file only had standalone functions missing imports and a class structure, so the code could not execute.

Prompt: "help format these inside a class SeamCarver:, add the missing module imports, and write a quick test script so we can actually see it run and process an image?".

Modifications: I reviewed the wrapped SeamCarver class and the new test_seam_carver.py script to ensure it correctly initializes the image state and runs the vertical seam removal without errors.