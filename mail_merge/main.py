with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    starting_text = file.read()

for name in names:
    name = name.strip()
    new_text = starting_text.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(new_text)


