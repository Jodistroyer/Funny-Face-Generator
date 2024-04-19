def interested_manipulation(input_value):
    
    # Convert input to integer
    value = int(input_value)
    
    # Generate a random magic number
    magic_number = 0xBEEF
    
    # Perform a bitwise XOR operation with the magic number
    manipulated_value = value ^ magic_number
    
    # Define different facial parts
    noses = ["  ^  ", "  o  ", "  -  ", " /\\ ", "  v  "]
    lips = ["_____", "----", "\__/", " 👄 ", "----"]
    eyes = ["o   o", "-   -", ".   .", "*   *", "@   @"]
    ears = [" (@) ", " /\\ ", " /\\ ", " oO ", " < > "]
    hair_styles = ["~~~~~", "|||||", "/////"]
    
    # Select facial parts based on the manipulated value
    nose = noses[manipulated_value % len(noses)]
    lip = lips[(manipulated_value // 5) % len(lips)]
    eye = eyes[(manipulated_value // 25) % len(eyes)]
    ear = ears[(manipulated_value // 125) % len(ears)]
    hair = hair_styles[(manipulated_value // 625) % len(hair_styles)]
    
    # Print the manipulated value with a curious message
    print(f"\nHmm, let me see what happens when I manipulate this number...")
        
    # Combine facial parts to create a new face
    new_face = f"""
            {hair}
       {ear} {eye} {ear}
            {nose}
            {lip}
    """
    
    # Print the new face
    print("\nThe result of my curious manipulation is:")
    print(new_face)
    print(f"\nValue: {manipulated_value}")


# Get user input
user_input = input("\nHey there! Give me a number to play with: ")

# Call the function with user input
interested_manipulation(user_input)

