# imports
import numpy as np
from PIL import Image, ImageGrab

# functions

def getPixelValues(img):
	return np.asarray(img)

def bwr(pixels):  # black, white, red: makes all pixels either black (unimportant), white (border of hp bar), or red (health color)
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

	try:
		while(bar[offset][0] != 255):  # find offset of border
			offset += 1
		while(bar[offset + width][0] != 100):  # find offset of hp
			width += 1
		while(bar[offset + width + hp][0] != 0):  # find number of pixels of hp
			hp += 1
		while(bar[offset + width + hp + missing][0] == 0):  # stop at end border of hp bar (equals zero because of color smoothing)
			missing += 1
	except IndexError:
		print("entire white border needs to be in the screenshot. please try again.")

	return (hp / (hp + missing))

def production():
	return 0

def main():
	production()

# execute

main()

pixels = getPixelValues(Image.open('hp_reader/88_89.png'))

new = bwr(pixels)
pct = calculateHP(new)
print(pct)
