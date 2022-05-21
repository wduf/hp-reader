# .pyw so it opens without the console

# imports
import tkinter as tk
from numpy import asarray
from PIL import ImageGrab

# functions

def fromClipboard():
	try:
		img = ImageGrab.grabclipboard()
	except:
		print("empty clipboard. please save a screenshot to your clipboard.")

	return img

def getPixelValues(img):
	return asarray(img)

def recolor(pixels):  # change pixel rgb values (really only the r value) so that i can read them moving forward
	for row in pixels:
		for p in row:
			border = ((p[0] > 180) and (p[1] > 180) and (p[2] > 180))
			empty = ((p[0] < 120) and (p[1] < 120) and (p[2] < 120))
			if(border):
				p[0] = 255  # outer (white) border of hp bar
			elif(empty):
				p[0] = 0  # missing hp in bar or outside border
			else:
				p[0] = 100  # current hp in bar
			# this is for debugging
			p[1] = 0
			p[2] = 0
	
	return pixels

def printRGB(pixels):  # print rgb values for each pixel in image
	for row in pixels:
		for p in row:
			for i in range(0, 3):
				print(f"i = {i}, pixel = {p[i]}")

def calculateHP(pixels):
	mid = int(len(pixels) / 2)  # truncated index of middle row of pixels in image
	bar = pixels[mid]  # using the middle row in image to calculate hp percent
	offset = 0  # offset from left of hp border
	width = 0  # width of hp border
	hp = 0  # index of beginning of hp, need this because color smoothing breaks this
	missing = 0  # index of beginning of missing hp

	while(bar[offset][0] != 255):  # find offset of border
		offset += 1
	while(bar[offset + width][0] == 255):  # find offset of hp
		width += 1
	while(bar[offset + width + hp][0] == 100):  # find number of pixels of hp
		hp += 1
	while(bar[offset + width + hp + missing][0] == 0):  # stop at end border of hp bar (equals zero because of color smoothing)
		missing += 1

	return (hp / (hp + missing))

def production():
	pct = 0
	img = fromClipboard()

	try:
		pixels = getPixelValues(img)
		new = recolor(pixels)
		pct = calculateHP(new)
		pct = (int(pct * 10000) / 100)

		return f"{pct}%"	
	except:
		return "error. try again."

def main():
	R = production()
	pct.configure(text = R)

# gui

window = tk.Tk()

title = tk.Label(window, text = "pokemon hp bar reader", font = "Arial 24")
title.pack()

button = tk.Button(window, text = "get percent", command = main)
button.pack()

pct = tk.Label(window, font = "Arial 48")
pct.pack()

# execute

window.mainloop()
