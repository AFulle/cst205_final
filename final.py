#CST 205 Final Project

#Yulian
#Ahdia
#Lyndsay


# Uses the commands dictionary to print out all the commands and their documentation
def help_message():
    printNow('Usage: [command] [parameters]')
    for cmd_info in commands.items():
        printNow(cmd_info[0] + " - " + str(cmd_info[1]['expected_arguments']) + " arguments - " + cmd_info[1]['help_message'])

### Testing
def do_some_kind_thing(something, something1):
    printNow(str(something) + " --- " + str(something1))
    
# Command Parser uses the commands dictionary to do all of its work, no need to modify this.
def command_parser(command):
    command_list = command.split(" ")
    command = command_list[0]
    
    if len(command_list) > 1:
      args = command_list[1:]
    else:
      args = []
        
    cmd_dict = commands[command]
    
    if cmd_dict['expected_arguments'] != len(args):
      return ('invalid', 'Parameter count does not match.')
    
    if len(args) > 0:
        return tuple([command]) + tuple(args)
    else:
        return tuple([command])
    
### All commands used here need to be defined before this line.
### Blah should be removed when we are done.
### We need a load function of some sort to get the image or sound file.
commands = {
    'help': {
        'help_message': 'This will print out the help message',
        'function': help_message,
        'expected_arguments': 0
    },
    'exit': {
        'help_message': 'Exit this program immediately.',
        'function': sys.exit,
        'expected_arguments': 0
    },
    'blah': {
        'help_message': 'Something something soemthing.',
        'function': do_some_kind_thing,
        'expected_arguments': 2
    }
}

#Testing
while true:
    user_input = requestString("enter command")
    command = command_parser(user_input)

    if command[0] == 'invalid':
        printNow('[ERROR] ' + command[1])
    elif command[0] == 'exit':
        break
    elif len(command) == 1:
        commands[command[0]]['function']()
    else:
        commands[command[0]]['function'](*command[1:])

printNow('Thanks for using the Media Manipulator')