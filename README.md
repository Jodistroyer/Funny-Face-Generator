# Funny-Face-Generator
A simple and funny ASCII face generator using Python

# Overview
This Python script takes a user input, manipulates it in a curious way, and generates a new face based on the manipulated value. The manipulation involves bitwise XOR operation with a magic number and selecting different facial parts based on the manipulated value.

# Usage
- Run the script interested_manipulation.py.
- Enter a number when prompted.
- Observe the result, which includes a new face generated based on the manipulation and the manipulated value.

# Functionality
- The script first converts the user input into an integer.
- It generates a random magic number (0xBEEF) and performs a bitwise XOR operation with the input value.
- Different facial parts (noses, lips, eyes, ears, and hair styles) are predefined in lists.
- Facial parts are selected based on the manipulated value to create a new face.
- The new face is printed along with the manipulated value.

# Notes
- The manipulation is intended for fun and demonstration purposes.
- Feel free to experiment with different input values to see how the generated face changes.
