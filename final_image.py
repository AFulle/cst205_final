def artify():
  pic = makePicture(pickAFile())
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
  
def lineDrawing():
  pic = makePicture(pickAFile())
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
  
def sepia():
  pic = makePicture(pickAFile())
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

def whiteBlend():
  pic = makePicture(pickAFile())
  pix = getPixels(pic)
  amount = requestNumber("How much white do you want to blend? Use decimals, ex: 20% = 0.20")
  for p in pix:
    newRed = 255*amount + getRed(p)*(1-amount)
    newGreen = 255*amount + getGreen(p)*(1-amount)
    newBlue = 255*amount + getBlue(p)*(1-amount)
    c = makeColor(newRed, newGreen, newBlue)
    setColor(p, c)
  show(pic)
    
