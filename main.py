

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt",mode="r") as file:

    with open("./Input/Names/invited_names.txt") as receiver:

        name_list = [s.strip() for s in receiver.readlines()]
        # alternative name_list = list(map(str.strip, receiver.readlines()))
        sender = input("Input Sender Name: ")

        for name in name_list:
            print (name)
            text = file.readlines()
            print(text)
            text[0] = text[0].replace("[name]", name)
            text[-1] = sender
            print(text)

            with open ("./Output/ReadyToSend/Letter_for_"+name+".txt", mode="a") as output:
                for line in text:
                    output.write(line)
                    print(line)

# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt

# TODO: Save the letters in the folder "ReadyToSend".