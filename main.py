

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt",mode="r") as file:
    text = file.readlines()
    print(text)

# TODO: Replace the [name] placeholder with "Name.txt" and put it into the ./Output/ReadyToSend

# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt

# TODO: Save the letters in the folder "ReadyToSend".