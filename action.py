import note

list_of_commands = [note.add_new_note, note.delete_note, note.show_all_notes, note.update_note]

def start():
    while True:
        print("Что Вы хотите сделать?")
        available_commands = []
        for i, command in enumerate(list_of_commands):
            print(f"{i}: {command.__name__}")
            available_commands.append(i)
        num_command = input()
        if num_command.isdigit() and int(num_command) in available_commands:
            list_of_commands[int(num_command)]()
            break