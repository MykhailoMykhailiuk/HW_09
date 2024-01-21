import sys

contacts = {}
commands = {'hello': 'Greetings in return',
            'add': 'Bot saves the new contact',
            'change': 'Bot saves the new phone number of the existing contact',
            'phone': 'Bot displays the phone number for the given name',
            'show all': 'Bot displays all saved contacts',
            'good bye, close, exit': 'Bot completes its work'}

help = ''
for key, value in commands.items():
    help += '{:<25} | {:<70}\n'.format(key, value)


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Contact not found'
        except ValueError:
            return f'Please follow the commands list {help}'
        except IndexError:
            return 'Please input command, name and/or phone'
    return inner


def greeting():
    return "How can I help you?"


@input_error
def add(user_input):
    line = user_input.split(' ')
    name = line[1]
    number = line[2]
    if name not in contacts:
        contacts[name] = number
        return 'New contact added!'
    else:
        return 'Contact already exist'


@input_error
def change(user_input):
    line = user_input.split(' ')
    name = line[1]
    number = line[2]
    if name in contacts:
        contacts[name] = number
        return 'Contact updated!'
    else:
        raise KeyError


@input_error
def phone(user_input):
    line = user_input.split(' ')
    name = line[1]
    return f'{name} | {contacts[name]}'


def show_all():
    if not contacts:
        return 'You have no any contacts saved'
    else:
        s = ''
        for key, value in contacts.items():
            s += f'{key} | {value}\n'
        return s


def exit(user_input):
    if user_input.lower() in ['good bye', 'close', 'exit']:
        sys.exit()


def main():  
   while True:
        user_input = input('>> ')
        if user_input.lower() in ['good bye', 'close', 'exit']:
            print('Good bye!')
            exit(user_input)
        line = user_input.split(' ')
        if line[0].lower() == 'hello':
            print(greeting())
        elif line[0].lower() == 'add':
            print(add(user_input))
        elif line[0].lower() == 'change':
            print(change(user_input))
        elif line[0].lower() == 'phone':
            print(phone(user_input))
        elif line[0].lower() == 'show':
            print(show_all())
        else:
            print(f'Please follow the commands list:\n{help}')


if __name__ == '__main__':
    main()
