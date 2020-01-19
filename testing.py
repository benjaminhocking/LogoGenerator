from tkinter import *
from random import random
window = Tk()
window.title("Logo creator")
window.geometry('400x400')
randomN = random()*16777216
randomN = int(randomN)
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

def rgbToHex(r,g,b):
    rr = hexadecimal2X(r)
    gg = hexadecimal2X(g)
    bb = hexadecimal2X(b)
    hexColour = rr + gg + bb
    return hexColour

def rgbToHSL(r,g,b):
    rd = r/255
    gd = g/255
    bd = b/255
    colours = [rd,gd,bd]
    maxrgb = max(colours)
    minrgb = min(colours)
    print(maxrgb, " ", minrgb)
    luminance = (maxrgb+minrgb)/2
    if minrgb == maxrgb:
        saturation = 0
        print("Saturation = 0")
    else:
        if luminance<0.5:
            saturation = (maxrgb-minrgb)/(maxrgb+minrgb)
            print(saturation, " luminance<0.5")
        else:
            saturation = (maxrgb-minrgb)/(2.0-maxrgb-minrgb)
            print(saturation, " luminance>0.5")
    saturation *= 100
    saturation = int(saturation)
    if maxrgb == rd:
        hue = (gd-bd)/(maxrgb-minrgb)
    elif maxrgb == gd:
        hue = 2.0 + (bd-rd)/(maxrgb-minrgb)
    else:
        hue = 4.0 + (rd-gd)/(maxrgb-minrgb)
    hue *= 60
    if hue < 0:
        hue += 360
    luminance *= 100
    luminance = int(luminance)
    hsl = [int(hue),saturation,luminance]
    return hsl

def hslToRgb(h, s, l):
    lum = l/100
    if s == 0:
        r = g = b = 255*lum
    else:
        if lum<0.5:
            temp1 = lum*(1+s)
        else:
            temp1 = lum+s-(lum*s)
        temp2 = (2*lum)-temp1
    hue = h/360
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

    #red *= 255
    #green *= 255
    #blue *= 255

    red = int(red)
    green = int(green)
    blue = int(blue)

    rgbArr = [red, green, blue]

    return rgbArr

print("HSL to rgb: ", hslToRgb(115, 53,62))


print(rgbToHSL(70,120,105))
hueVariation = 12

color1 = rgbToHSL(110,214,100)
color2 = [color1[0]+hueVariation, color1[1], color1[2]]
color3 = [color1[0]-hueVariation, color1[1], color1[2]]

analogous = [color1, color2, color3]
print(analogous)

print(rgbToHex(208, 178, 79))
randomNStr = hexadecimal6X(randomN)
colorString = "#" + randomNStr
#w = Canvas(window, width=300, height=300, background=(208,178,79))
#w.pack()
window.mainloop()
