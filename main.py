with open("./Input/Names/invited_names.txt") as receiver:
    name_list = [s.strip() for s in receiver.readlines()]
    sender = input("Input Sender Name: ")

    for name in name_list:

        with open("./Input/Letters/starting_letter.txt", mode="r") as file:
            text = file.readlines()
            text[0] = text[0].replace("[name]", name)
            text[-1] = sender

            with open("./Output/ReadyToSend/Letter_for_" + name + ".txt", mode="a") as output:
                for line in text:
                    output.write(line)
                    print(line)
