from tkinter import *
from random import random
window = Tk()
window.title("Color themer")
#window.geometry('300x610')
def hexadecimal6X(x):
    first = hex(x)
    second = first[2:]
    tooshort = 6-len(second)
    for i in range(tooshort):
        second = "0" + second
    return str(second)
def hexadecimal2X(x):
    first = hex(x)
    second = first[2:]
    tooshort = 2-len(second)
    for i in range(tooshort):
        second = "0" + second
    return str(second)

print(hexadecimal2X(257))

def rgbToHex(r,g,b):
    rr = hexadecimal2X(r)
    gg = hexadecimal2X(g)
    bb = hexadecimal2X(b)
    hexColour = str(rr) + str(gg) + str(bb)
    return hexColour

def rgbToHSL(r,g,b):
    rd = r/255
    gd = g/255
    bd = b/255
    colours = [rd,gd,bd]
    maxrgb = max(colours)
    minrgb = min(colours)
    luminance = (maxrgb+minrgb)/2
    if minrgb == maxrgb:
        saturation = 0
    else:
        if luminance<0.5:
            saturation = (maxrgb-minrgb)/(maxrgb+minrgb)
        else:
            saturation = (maxrgb-minrgb)/(2.0-maxrgb-minrgb)
    if maxrgb == rd:
        hue = (gd-bd)/(maxrgb-minrgb)
    elif maxrgb == gd:
        hue = 2.0 + (bd-rd)/(maxrgb-minrgb)
    else:
        hue = 4.0 + (rd-gd)/(maxrgb-minrgb)
    hue *= 60
    if hue < 0:
        hue += 360
    saturation *= 100
    saturation = int(saturation)
    luminance *= 100
    luminance = int(luminance)
    hsl = [int(hue),saturation,luminance]
    return hsl


def hslToRgb(colors):
	h = colors[0]
	s = colors[1]
	l = colors[2]
	hue = h/360
	saturation = s/100
	lum = l/100
	if saturation == 0:
	    r = g = b = 255*lum
	    return [int(r),int(g),int(b)]
	else:
	    if lum<0.5:
	        temp1 = lum*(1+saturation)
	    else:
	        temp1 = lum+saturation-(lum*saturation)
	    temp2 = (2*lum)-temp1
	tempR = 0.333 + hue
	tempG = hue
	tempB = hue - 0.333
	if tempR<0:
	    tempR+=1
	elif tempR>1:
	    tempR -=1
	if tempG<0:
	    tempG+=1
	elif tempG>1:
	    tempG -=1
	if tempB<0:
	    tempB+=1
	elif tempB>1:
	    tempB -=1


	if 6*tempR < 1:
	    red = temp2+(temp1-temp2)*6*tempR
	elif 2*tempR<1:
	    red = temp1
	elif 3*tempR<2:
	    red = temp2 + (temp1-temp2)*(0.666-tempR)*6
	else:
	    red = temp2

	if 6*tempG < 1:
	    green = temp2+(temp1-temp2)*6*tempG
	elif 2*tempG<1:
	    green = temp1
	elif 3*tempG<2:
	    green = temp2 + (temp1-temp2)*(0.666-tempG)*6
	else:
	    green = temp2

	if 6*tempB < 1:
	    blue = temp2+(temp1-temp2)*6*tempB
	elif 2*tempB<1:
	    blue = temp1
	elif 3*tempR<2:
	    blue = temp2 + (temp1-temp2)*(0.666-tempB)*6
	else:
	    blue = temp2

	red = int(red*255)
	green = int(green*255)
	blue = int(blue*255)

	if red > 255:
		red -= 255
	if green > 255:
		green -= 255
	if blue > 255:
		blue -= 255
	if red<0:
		red += 255
	if green < 0:
		green += 255
	if blue < 0:
		blue += 255

	rgbArr = [red, green, blue]

	return rgbArr

print(hslToRgb([193,67,28]))


#############
#############
#############
#############
####TWEAK####
hueVariation = 30
#############
#############
#############
#############

canvasBoard = Canvas(window, width=300, height=600)
sqr1 = canvasBoard.create_rectangle(0,0,300,200, fill="white", outline="white")
sqr2 = canvasBoard.create_rectangle(0,200,300,400, fill="white", outline="white")
sqr3 = canvasBoard.create_rectangle(0,400,300,600, fill="white", outline="white")

def analogousBoxes():
	randomR = int(random()*255)
	randomG = int(random()*255)
	randomB = int(random()*255)

	ir = randomR
	ig = randomG
	ib = randomB

	color1 = rgbToHSL(ir,ig,ib)
	color2 = [color1[0]+hueVariation, color1[1], color1[2]]
	color3 = [color1[0]-hueVariation, color1[1], color1[2]]
	if color2[0]>360:
		color2[0] -= 360

	if color3[0]>360:
		color3[0]-=360

	analogous = [color1, color2, color3]

	#convert analogous hsl to rgb
	for i in range(3):
		color1RGB = hslToRgb(color1)
		color2RGB = hslToRgb(color2)
		color3RGB = hslToRgb(color3)

	color1r = color1RGB[0]
	color1g = color1RGB[1]
	color1b = color1RGB[2]

	color2r = color2RGB[0]
	color2g = color2RGB[1]
	color2b = color2RGB[2]

	color3r = color3RGB[0]
	color3g = color3RGB[1]
	color3b = color3RGB[2]

	#print(color1r, color1g, color1b)
	colorString1 = "#" + rgbToHex(color1r,color1g,color1b)
	colorString2 = "#" + rgbToHex(color2r, color2g, color2b)
	colorString3 = "#" + rgbToHex(color3r, color3g, color3b)

	sqr1 = canvasBoard.create_rectangle(0,0,300,200, fill=colorString2, outline="white")
	sqr2 = canvasBoard.create_rectangle(0,200,300,400, fill=colorString1, outline="white")
	sqr3 = canvasBoard.create_rectangle(0,400,300,600, fill=colorString3, outline="white")
	colorScheme = [colorString1, colorString2, colorString3]
	print("This color scheme: ", colorScheme)
	window.mainloop()

	return

def newColor():
	canvasBoard.delete(sqr1)
	canvasBoard.delete(sqr2)
	canvasBoard.delete(sqr3)
	analogousBoxes()



b = Button(window, text="Generate", command=newColor)
b.pack()
canvasBoard.pack()

analogousBoxes()

"""
w = Canvas(window, width=300, height=300, background=colorString2)
w.pack()
w2 = Canvas(window, width=300, height=300, background=colorString1)
w2.pack()
w3 = Canvas(window, width=300, height=300, background=colorString3)
w3.pack()
"""
