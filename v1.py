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
			# we don't need to worry about the other two values, we only care about the first one going forward
	
	return pixels

def printRGB(pixels):  # print rgb values for each pixel in image
	for row in pixels:
		for p in row:
			for i in range(0, 3):
				print(f"i = {i}, pixel = {p[i]}")

"""
need to do edge cases and watch for out of bounds errors in while loops (example: if hp bar not surrounded by outer border, while loop won't stop)

try:
	sldj;falskdf
except IndexError:
	print("entire white border needs to be in the screenshot. please try again.")

"""
def calculateHP(pixels):
	mid = int(len(pixels) / 2)  # truncated index of middle row of pixels in image
	bar = pixels[mid]  # using the middle row in image to calculate hp percent
	offset = 0  # offset from left where hp bar border starts
	hp = 0  # starting index, index of first pixel of border
	missing = 0  # missing hp index start
	end = 0  # width of end border

	while(bar[offset][0] == 0):  # will stop once we get to first pixel of border
		offset += 1
	while(bar[offset + hp][0] != 0):  # will stop once we get to next empty/outside pixel
		hp += 1
	if(bar[offset + hp][0] != 255):  # if last pixel was not edge border
		while(bar[offset + hp + missing][0] != 255):
			missing += 1
		while(bar[offset + hp + missing + end][0] != 0):
			end += 1
	# at this point, we have the offset from the left, hp pixels, the missing hp pixels, and the width of the end border
	
	return (hp / (hp + missing + end))

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
# print(f"\n\n***{int(len(pixels)/2)}***\n\n")

# new = Image.fromarray(bwr(pixels))
# new.show()

