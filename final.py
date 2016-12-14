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

# loads image or sound
def load():
    option = requestString("Do you want to load an image or audio?")
    if option == "image":
        pic = makePicture(pickAFile())
        return pic
    elif option == "audio":
        sound = makeSound(pickAFile())
        return sound
    else:
        option = requestString("Invalid input. Do you want to load an image or audio?")

#changes picture to artsy
def artify(pic):
  mypic = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range(0, getWidth(mypic)):
    for y in range(0, getHeight(mypic)):
      p = getPixel(pic, x, y)
      r = getRed(p)
      b = getBlue(p)
      g = getGreen(p)
      pn = getPixel(mypic, x, y)
      if r < 63:
        setRed(pn, 31)
      elif r > 62 and r < 128:
        setRed(pn, 95)
      elif r > 127 and r < 192:
        setRed(pn, 159)
      else:
        setRed(pn, 223)
      if g < 63:
        setGreen(pn, 31)
      elif g > 62 and g < 128:
        setGreen(pn, 95)
      elif g > 127 and g < 192:
        setGreen(pn, 159)
      else:
        setGreen(pn, 223)
      if b < 63:
        setBlue(pn, 31)
      elif b > 62 and b < 128:
        setBlue(pn, 95)
      elif b > 127 and b < 192:
        setBlue(pn, 159)
      else:
        setBlue(pn, 223)
  show(mypic)
  
# only for sepia and lineDrawing, not an actual option
def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = r*0.299 + g*0.587 + b*0.114
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  repaint(pic)
  return(pic)

#changes picture to a line drawing
def lineDrawing(pic):
  pix = getPixels(pic)
  pic = betterBnW(pic)
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
def sepia(pic):
  bnwpic = betterBnW(pic)
  mypic = makeEmptyPicture(getWidth(bnwpic), getHeight(bnwpic))
  for x in range(0, getWidth(mypic)):
    for y in range(0, getHeight(mypic)):
      p = getPixel(bnwpic, x, y)
      r = getRed(p)
      b = getBlue(p)
      g = getGreen(p)
      pn = getPixel(mypic, x, y)
      if r < 63:
        setColor(pn, makeColor(r*1.1,g,b*0.9))
      elif r > 62 and r < 192:
        setColor(pn, makeColor(r*1.16,g,b*0.84))  
      else:
        setColor(pn, makeColor(min(r*1.08, 255), g, b*0.93))
  show(mypic)

#blends an amount of white with the picture
def whiteBlend(pic):
  pix = getPixels(pic)
  amount = requestNumber("How much white do you want to blend? Use decimals, ex: 20% = 0.20")
  for p in pix:
    newRed = 255*amount + getRed(p)*(1-amount)
    newGreen = 255*amount + getGreen(p)*(1-amount)
    newBlue = 255*amount + getBlue(p)*(1-amount)
    c = makeColor(newRed, newGreen, newBlue)
    setColor(p, c)
  show(pic)

def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  play(sound)
  return(sound)

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 0.5)
  play(sound)
  return(sound)

def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if (value > 0):
      setSampleValue(sample, 32767)
    if (value < 0):
      setSampleValue(sample, -32768)
  play(sound)
  return(sound)

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
        'help_message': 'Temp!',
        'function': artify,
        'expected_arguments': 1
    },
    'bnw': {
        'help_message': 'Temp',
        'function': betterBnW,
        'expected_arguments': 1
    },
    'sepia': {
        'help_message': 'Temp',
        'function': sepia,
        'expected_arguments': 1
    },
    'blend': {
        'help_message': 'Temp',
        'function': whiteBlend,
        'expected_arguments': 1
    },
     'increase': {
        'help_message': 'Temp',
        'function': increaseVolume,
        'expected_arguments': 1
    },
     'decrease': {
        'help_message': 'Temp',
        'function': decreaseVolume,
        'expected_arguments': 1
    },
     'eleven': {
        'help_message': 'Temp',
        'function': goToEleven,
        'expected_arguments': 1
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
                                          