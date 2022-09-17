import random

# for the script to work you need xclip n xsel
import pyperclip # copy the result to clipboard

# establish if a point (x, y) is inside the ellipse
def ellipse (x, y, h, k, a, b):
	# with 0.8 instead of 1 we can leave space near the border
	return pow((x - h), 2) / pow(a, 2) + pow((y - k), 2) / pow(b, 2) < 0.8

# ellipse parameters
center_x = 10
center_y = 0
a = 3.0
b = 1.5

# number of points that we want
total = 10
l = []

while total > 0:

	# generate the point
	x = random.uniform(center_x - a, center_x + a)
	y = random.uniform(center_y - b, center_y + b)

	# check if it is inside the ellipse
	if (ellipse(x, y, center_x, center_y, a, b)):
		l.append((x, y))
		total -= 1

index = ord('K')
text = ""
for elem in l:
	# print("\\node [circle, fill=black, scale=0.3] (", chr(index), ") at ", elem, "{};")
	text += "\\node [circle, fill=black, scale=0.3] (" + str(chr(index)) + ") at " + str(elem) + "{};\n"
	index += 1

print(text)

pyperclip.copy(text)
# spam = pyperclip.paste()
