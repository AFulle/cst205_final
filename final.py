#CST 205 Final Project

#Yulian
#Ahdia
#Lyndsay

loaded_files = {
  'image': '',
  'audio': '',
}

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

# loads image or sound
def load():
    option = requestString("Do you want to load an image or audio?")
    if option == "image":
        loaded_files['image'] = makePicture(pickAFile())
    elif option == "audio":
        loaded_files['audio'] = makeSound(pickAFile())
    else:
        option = requestString("Invalid input. Try again.")
        
        
def save():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    option = requestString("Do you want to save an image or audio?")
    if option == "image":
        writePictureTo(loaded_files['image'], current_dir + "/output_image.png")
        showInformation("Successfully saved image to " + current_dir + "/output_image.png")
    elif option == "audio":
        writePictureTo(loaded_files['audio'], current_dir + "/output_audio.wav")
        showInformation("Successfully saved audio to " + current_dir + "/output_audio.wav")
    else:
        showInformation("Invalid input. Try again.")

#changes picture to artsy
def artify():
  mypic = loaded_files['image']
  for x in range(0, getWidth(mypic)):
    for y in range(0, getHeight(mypic)):
      p = getPixel(mypic, x, y)
      r = getRed(p)
      b = getBlue(p)
      g = getGreen(p)
      if r < 63:
        setRed(p, 31)
      elif r > 62 and r < 128:
        setRed(p, 95)
      elif r > 127 and r < 192:
        setRed(p, 159)
      else:
        setRed(p, 223)
      if g < 63:
        setGreen(p, 31)
      elif g > 62 and g < 128:
        setGreen(p, 95)
      elif g > 127 and g < 192:
        setGreen(p, 159)
      else:
        setGreen(p, 223)
      if b < 63:
        setBlue(p, 31)
      elif b > 62 and b < 128:
        setBlue(p, 95)
      elif b > 127 and b < 192:
        setBlue(p, 159)
      else:
        setBlue(p, 223)
  repaint(mypic)
  
# only for sepia and lineDrawing, not an actual option
def betterBnW(showPreview=True):
  pixels = getPixels(loaded_files['image'])
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = r*0.299 + g*0.587 + b*0.114
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  if showPreview:
    repaint(loaded_files['image'])
    
#changes picture to a line drawing
def lineDrawing():
  betterBnW(False)
  pic = loaded_files['image']
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      if x + 1 < getWidth(pic) and y + 1 < getHeight(pic):
        p = getPixel(pic, x, y)
        r1 = getRed(p)
        right = getPixel(pic, x + 1, y)
        r2 = getRed(right)
        bottom = getPixel(pic, x, y + 1)
        r3 = getRed(bottom)
        if abs(r1 - r2) > 5 and abs(r1 - r3) > 5:
          setRed(p, 0)
          setBlue(p, 0)
          setGreen(p, 0)
        else:
          setRed(p, 255)
          setBlue(p, 255)
          setGreen(p, 255)
      else:
        setRed(p, 255)
        setBlue(p, 255)
        setGreen(p, 255)
  repaint(pic)

#makes picture sepia
def sepia():
  betterBnW(False)
  mypic = loaded_files['image']
  for x in range(0, getWidth(mypic)):
    for y in range(0, getHeight(mypic)):
      p = getPixel(mypic, x, y)
      r = getRed(p)
      b = getBlue(p)
      g = getGreen(p)
      if r < 63:
        setColor(p, makeColor(r*1.1,g,b*0.9))
      elif r > 62 and r < 192:
        setColor(p, makeColor(r*1.16,g,b*0.84))  
      else:
        setColor(p, makeColor(min(r*1.08, 255), g, b*0.93))
  repaint(mypic)

#blends an amount of white with the picture
def whiteBlend():
  pix = getPixels(loaded_files['image'])
  amount = requestNumber("How much white do you want to blend? Use decimals, ex: 20% = 0.20")
  for p in pix:
    newRed = 255*amount + getRed(p)*(1-amount)
    newGreen = 255*amount + getGreen(p)*(1-amount)
    newBlue = 255*amount + getBlue(p)*(1-amount)
    c = makeColor(newRed, newGreen, newBlue)
    setColor(p, c)
  repaint(loaded_files['image'])

def increaseVolume():
  for sample in getSamples(loaded_files['audio']):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  play(loaded_files['audio'])

def decreaseVolume():
  for sample in getSamples(loaded_files['audio']):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 0.5)
  play(loaded_files['audio'])

def goToEleven():
  for sample in getSamples(loaded_files['audio']):
    value = getSampleValue(sample)
    if (value > 0):
      setSampleValue(sample, 32767)
    if (value < 0):
      setSampleValue(sample, -32768)
  play(loaded_files['audio'])

### All commands used here need to be defined before this line.
### Blah should be removed when we are done.
### We need a load function of some sort to get the image or sound file.
commands = {
    'help': {
        'help_message': 'This will print out the help message',
        'function': help_message,
        'expected_arguments': 0
    },
    'load': {
        'help_message': 'This will let you select a image or audio file to load',
        'function': load,
        'expected_arguments': 0
    },
    'artify': {
        'help_message': 'Makes the image look drawn or arty.',
        'function': artify,
        'expected_arguments': 0
    },
    'bnw': {
        'help_message': 'Makes the picture black and white.',
        'function': betterBnW,
        'expected_arguments': 0
    },
    'sepia': {
        'help_message': 'Provides a sepia effect to the image.',
        'function': sepia,
        'expected_arguments': 0
    },
    'blend': {
        'help_message': 'Blends a percentage of white into the image provided by the user.',
        'function': whiteBlend,
        'expected_arguments': 0
    },
     'increase': {
        'help_message': 'Doubles the volume of the sound.',
        'function': increaseVolume,
        'expected_arguments': 0
    },
     'decrease': {
        'help_message': 'Halves the volume of the sound',
        'function': decreaseVolume,
        'expected_arguments': 0
    },
     'eleven': {
        'help_message': 'Cranks up the volume to maximum!',
        'function': goToEleven,
        'expected_arguments': 0
    },
    'save': {
        'help_message': 'Saves the image or sound to a file.',
        'function': save,
        'expected_arguments': 0
    },
    'exit': {
        'help_message': 'Exit this program immediately.',
        'function': sys.exit,
        'expected_arguments': 0
    }
}

# Main code
showInformation("""Welcome to the Bitspice Media Manipulator!
Using this tool you can manipulate images and sounds with the predefined commands.

If you need a list of commands, please type 'help'.
If the command expects arguments, make sure to include them in the command when you use it.

You need to use the 'load' command first to load your appropriate file to manipulate.
The commands won't work without a file loaded.

If you need to restart, or clear out your changes, use the load command and reload the file.
Changes should be cummulative.
""")

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
                                                                                          