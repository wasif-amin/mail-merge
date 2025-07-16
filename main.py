with open("Input/Names/invited_names.txt") as file:
    names = [line.strip() for line in  file.readlines()]



with open("Input/Letters/starting_letter.txt") as letter:
    invite = letter.read()

for invitee in names:
    personal_invite = invite.replace("[name]", invitee)
    print(personal_invite)

