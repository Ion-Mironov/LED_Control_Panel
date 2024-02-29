#### Must run this script with `sudo` ####

import time
from rpi_ws281x import PixelStrip, Color


""" Global LED grid (PixelStrip) configuration """
LED_COUNT = 768				# Number of LED pixels.
LED_PIN = 18				# GPIO pin connected to the pixels (This is physical pin 12). GPIO 18 is the default for PWM0.
LED_FREQ_HZ = 800000		# LED signal frequency in Hertz (usually 800kHz).
LED_DMA = 10				# DMA channel to use for generating signal.
LED_INVERT = False			# Set to 'True' to invert the signal (when using NPN transistor level shift).
LED_BRIGHTNESS = 255		# Set to '0' for off and '255' for ultra-brightness. '25' is good for testing purposes.
LED_CHANNEL = 0				# Set to '1' for GPIO 13 (which is physical pin 33).



""" Initialize the LED grid """
grid = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
grid.begin()


""" Set the default state of all animations to 'False' """
animation_running = False



# ===== FUNCTIONS ======================================================================================================================================== #
""" Retrieve the LED index based on row and column and which LED panel to use """

### LED PANEL 1 ###
def get_led_index1(row, col):

	# Converting 2D coordinates into a 1D LED grid index #
	""" 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 """
	lookup_table1 = [
		[0, 15, 16, 31, 32, 47, 48, 63, 64, 79, 80, 95,  96, 111, 112, 127, 128, 143, 144, 159, 160, 175, 176, 191, 192, 207, 208, 223, 224, 239, 240, 255],
		[1, 14, 17, 30, 33, 46, 49, 62, 65, 78, 81, 94,  97, 110, 113, 126, 129, 142, 145, 158, 161, 174, 177, 190, 193, 206, 209, 222, 225, 238, 241, 254],
		[2, 13, 18, 29, 34, 45, 50, 61, 66, 77, 82, 93,  98, 109, 114, 125, 130, 141, 146, 157, 162, 173, 178, 189, 194, 205, 210, 221, 226, 237, 242, 253],
		[3, 12, 19, 28, 35, 44, 51, 60, 67, 76, 83, 92,  99, 108, 115, 124, 131, 140, 147, 156, 163, 172, 179, 188, 195, 204, 211, 220, 227, 236, 243, 252],
		[4, 11, 20, 27, 36, 43, 52, 59, 68, 75, 84, 91, 100, 107, 116, 123, 132, 139, 148, 155, 164, 171, 180, 187, 196, 203, 212, 219, 228, 235, 244, 251],
		[5, 10, 21, 26, 37, 42, 53, 58, 69, 74, 85, 90, 101, 106, 117, 122, 133, 138, 149, 154, 165, 170, 181, 186, 197, 202, 213, 218, 229, 234, 245, 250],
		[6,  9, 22, 25, 38, 41, 54, 57, 70, 73, 86, 89, 102, 105, 118, 121, 134, 137, 150, 153, 166, 169, 182, 185, 198, 201, 214, 217, 230, 233, 246, 249],
		[7,  8, 23, 24, 39, 40, 55, 56, 71, 72, 87, 88, 103, 104, 119, 120, 135, 136, 151, 152, 167, 168, 183, 184, 199, 200, 215, 216, 231, 232, 247, 248]
	]
	return lookup_table1[row][col]

### LED PANEL 2 ###
def get_led_index2(row, col):

	lookup_table2 = [
		[256, 271, 272, 287, 288, 303, 304, 319, 320, 335, 336, 351, 352, 367, 368, 383, 384, 399, 400, 415, 416, 431, 432, 447, 448, 463, 464, 479, 480, 495, 496, 511],
		[257, 270, 273, 286, 289, 302, 305, 318, 321, 334, 337, 350, 353, 366, 369, 382, 385, 398, 401, 414, 417, 430, 433, 446, 449, 462, 465, 478, 481, 494, 497, 510],
		[258, 269, 274, 285, 290, 301, 306, 317, 322, 333, 338, 349, 354, 365, 370, 381, 386, 397, 402, 413, 418, 429, 434, 445, 450, 461, 466, 477, 482, 493, 498, 509],
		[259, 268, 275, 284, 291, 300, 307, 316, 323, 332, 339, 348, 355, 364, 371, 380, 387, 396, 403, 412, 419, 428, 435, 444, 451, 460, 467, 476, 483, 492, 499, 508],
		[260, 267, 276, 283, 292, 299, 308, 315, 324, 331, 340, 347, 356, 363, 372, 379, 388, 395, 404, 411, 420, 427, 436, 443, 452, 459, 468, 475, 484, 491, 500, 507],
		[261, 266, 277, 282, 293, 298, 309, 314, 325, 330, 341, 346, 357, 362, 373, 378, 389, 394, 405, 410, 421, 426, 437, 442, 453, 458, 469, 474, 485, 490, 501, 506],
		[262, 265, 278, 281, 294, 297, 310, 313, 326, 329, 342, 345, 358, 361, 374, 377, 390, 393, 406, 409, 422, 425, 438, 441, 454, 457, 470, 473, 486, 489, 502, 505],
		[263, 264, 279, 280, 295, 296, 311, 312, 327, 328, 343, 344, 359, 360, 375, 376, 391, 392, 407, 408, 423, 424, 439, 440, 455, 456, 471, 472, 487, 488, 503, 504]
	]
	return lookup_table2[row][col]

### LED PANEL 3 ###
def get_led_index3(row, col):

	lookup_table3 = [
		[512, 527, 528, 543, 544, 559, 560, 575, 576, 591, 592, 607, 608, 623, 624, 639, 640, 655, 656, 671, 672, 687, 688, 703, 704, 719, 720, 735, 736, 751, 752, 767],
		[513, 526, 529, 542, 545, 558, 561, 574, 577, 590, 593, 606, 609, 622, 625, 638, 641, 654, 657, 670, 673, 686, 689, 702, 705, 718, 721, 734, 737, 750, 753, 766],
		[514, 525, 530, 541, 546, 557, 562, 573, 578, 589, 594, 605, 610, 621, 626, 637, 642, 653, 658, 669, 674, 685, 690, 701, 706, 717, 722, 733, 738, 749, 754, 765],
		[515, 524, 531, 540, 547, 556, 563, 572, 579, 588, 595, 604, 611, 620, 627, 636, 643, 652, 659, 668, 675, 684, 691, 700, 707, 716, 723, 732, 739, 748, 755, 764],
		[516, 523, 532, 539, 548, 555, 564, 571, 580, 587, 596, 603, 612, 619, 628, 635, 644, 651, 660, 667, 676, 683, 692, 699, 708, 715, 724, 731, 740, 747, 756, 763],
		[517, 522, 533, 538, 549, 554, 565, 570, 581, 586, 597, 602, 613, 618, 629, 634, 645, 650, 661, 666, 677, 682, 693, 698, 709, 714, 725, 730, 741, 746, 757, 762],
		[518, 521, 534, 537, 550, 553, 566, 569, 582, 585, 598, 601, 614, 617, 630, 633, 646, 649, 662, 665, 678, 681, 694, 697, 710, 713, 726, 729, 742, 745, 758, 761],
		[519, 520, 535, 536, 551, 552, 567, 568, 583, 584, 599, 600, 615, 616, 631, 632, 647, 648, 663, 664, 679, 680, 695, 696, 711, 712, 727, 728, 743, 744, 759, 760]
	]
	return lookup_table3[row][col]


""" Set the color of a specified rectangular area within the LED panel """
def pixel_setup1(top_pixel, bottom_pixel, color):
	for row in range(top_pixel[0], bottom_pixel[0] + 1):
		for col in range(top_pixel[1], bottom_pixel[1] + 1):
			index = get_led_index1(row, col)
			grid.setPixelColor(index, color)

def pixel_setup2(top_pixel, bottom_pixel, color):
	for row in range(top_pixel[0], bottom_pixel[0] + 1):
		for col in range(top_pixel[1], bottom_pixel[1] + 1):
			index = get_led_index2(row, col)
			grid.setPixelColor(index, color)

def pixel_setup3(top_pixel, bottom_pixel, color):
	for row in range(top_pixel[0], bottom_pixel[0] + 1):
		for col in range(top_pixel[1], bottom_pixel[1] + 1):
			index = get_led_index3(row, col)
			grid.setPixelColor(index, color)


""" Brightness control """
def set_brightness(value):
	grid.setBrightness(value)


""" Turn off all LEDs """
def clear_grid():
	pixels_off = Color(0, 0, 0)
	top_pixel = (0, 0)
	bottom_pixel = (7, 31)

	# Clear each panel
	pixel_setup1(top_pixel, bottom_pixel, pixels_off)
	pixel_setup2(top_pixel, bottom_pixel, pixels_off)
	pixel_setup3(top_pixel, bottom_pixel, pixels_off)


""" Stop current animation gracefully """
def stop_animation():
	global animation_running												# Utilize the 'animation_running' variable.
	animation_running = False												# Stop the animation by setting its running state to 'False'.
	clear_grid()															# Ensure the grid is cleared when the animation stops.
	grid.show()																# Show a cleared grid


""" Ensure animation will stop when 'Off' button is pressed or another animation is selected """
def check_and_clear():
		if not animation_running:
			clear_grid()
			grid.show()
			return True
		return False



# ======================================================================================================================================================== #
# ===== LED ANIMATIONS =================================================================================================================================== #

# Sequential left turn signal #
def left_turn_signal(grid):
	global animation_running												# Utilize the 'animation_running' variable.
	animation_running = True												# Start the animation.

	set_brightness(30)														# Set brightness to an acceptable testing level.
	pixel_color = Color(255, 70, 0)											# Define the color. (Orange)

	while animation_running:
		for col_start in range(31, -1, -1):									# Iterating over top-half of each column right to left (← ← ←).
			if check_and_clear(): return									# Check if animation was instructed to stop.
			top_pixel = (0, col_start)										# Start at row 0, column 0.
			bottom_pixel = (3, col_start)									# End at row 3, column 0.
			pixel_setup1(top_pixel, bottom_pixel, pixel_color)				# Set and display color of area defined by `top_pixel` & `bottom_pixel` coordinates.
			grid.show()														# Display LEDs.
			time.sleep(0.015)												# How fast the columns light up (in milliseconds).

		if check_and_clear(): return
		time.sleep(0.2)														# How long the LEDs stay ON before turning off.
		clear_grid()														# Clear the grid before starting the sequence again.
		grid.show()															# Display the cleared grid.
		if check_and_clear(): return
		time.sleep(0.25)													# How long the LEDs stay OFF before starting sequence again.

	if check_and_clear(): return
	clear_grid()															# Ensure the grid is cleared when the animation stops
	grid.show()



# ======================================================================================================================================================== #
# Sequential right turn signal #
def right_turn_signal(grid):
	global animation_running
	animation_running = True

	set_brightness(30)
	pixel_color = Color(255, 70, 0)

	while animation_running:
		for col_start in range(0, 32):										# Iterating left to right (→ → →)
			if check_and_clear(): return
			top_pixel = (0, col_start)
			bottom_pixel = (3, col_start)
			pixel_setup3(top_pixel, bottom_pixel, pixel_color)
			grid.show()
			time.sleep(0.015)

		if check_and_clear(): return
		time.sleep(0.2)
		clear_grid()
		grid.show()
		time.sleep(0.25)

	if check_and_clear(): return
	clear_grid()
	grid.show()



# ======================================================================================================================================================== #
# Sequential brake lights #
def sequential_brake_lights(grid):
	global animation_running
	animation_running = True

	set_brightness(30)
	pixel_color = Color(255, 0, 0)

	if check_and_clear(): return
	for col in range(32):

		# Left panel: iterate from right to left (← ← ←)
		for row in range(8):
			left_index = get_led_index1(row, 31 - col)
			grid.setPixelColor(left_index, pixel_color)
			if check_and_clear(): return
		
		# Right panel: iterate from left to right (→ → →)
		for row in range(8):
			right_index = get_led_index3(row, col)
			grid.setPixelColor(right_index, pixel_color)
			if check_and_clear(): return
		
		if check_and_clear(): return
		grid.show()
		time.sleep(0.005)

# ======================================================================================================================================================== #
# Third brake light [3-3-1 flash] #
def third_brake_light(grid):
	global animation_running
	animation_running = True

	set_brightness(30)
	pixel_color = Color(255, 0, 0)

	# -- Flash rapidly 3 times -- #
	for _ in range(3):														# The underscore is a throwaway variable and is used for iterating/looping.
		if check_and_clear(): return
		pixel_setup2((0, 0), (7, 31), pixel_color)							# Alternate way to set pixel layout.
		grid.show()
		time.sleep(0.1)														# How long LEDs are on during flashing sequence.
		if check_and_clear(): return
		clear_grid()
		grid.show()
		time.sleep(0.1)														# How long LEDs are off during flashing sequence.
		if check_and_clear(): return

	# -- Flash normally 3 times -- #
	for _ in range(3):
		if check_and_clear(): return
		pixel_setup2((0, 0), (7, 31), pixel_color)
		grid.show()
		time.sleep(0.3)
		if check_and_clear(): return
		clear_grid()
		grid.show()
		time.sleep(0.3)
		if check_and_clear(): return

	# -- Remain constantly lit -- #
	if check_and_clear(): return
	pixel_setup1((0, 0), (7, 31), pixel_color)
	grid.show()



# ======================================================================================================================================================== #
# Front Parking lights #
def front_parking_lights(grid):
	global animation_running
	animation_running = True

	set_brightness(10)
	pixel_color = Color(255, 100, 0)
	pixel_setup1((0, 0), (7, 31), pixel_color)
	pixel_setup3((0, 0), (7, 31), pixel_color)
	grid.show()



# ======================================================================================================================================================== #
# Rear Parking lights #
def rear_parking_lights(grid):
	global animation_running
	animation_running = True

	set_brightness(10)
	pixel_color = Color(255, 0, 0)
	pixel_setup1((0, 0), (7, 31), pixel_color)
	grid.show()



# ======================================================================================================================================================== #
# Emergency lights #
def emergency_lights(grid):
	global animation_running
	animation_running = True

	set_brightness(30)

	BLUE = Color(0, 0, 255)
	RED = Color(255, 0, 0)

	left_half = (0, 15)														# Columns 0 through 15 for the left half.
	right_half = (16, 31)													# Columns 16 through 31 for the right half.

	try:
		while animation_running:
			# Flash the left half blue
			for _ in range(3):												# Flash 3 times.
				for row in range(8):										# 8 rows.
					for col in range(left_half[0], left_half[1] + 1):		# Left half columns.
						index = get_led_index1(row, col)
						grid.setPixelColor(index, BLUE)
				grid.show()
				time.sleep(0.08)											# Flash duration.

				clear_grid()
				grid.show()
				time.sleep(0.08)											# Pause between flashes.

			# Flash the right half red
			for _ in range(3):												# Flash 3 times.
				for row in range(8):
					for col in range(right_half[0], right_half[1] + 1):		# Right half columns.
						index = get_led_index1(row, col)
						grid.setPixelColor(index, RED)
				grid.show()
				time.sleep(0.08)

				clear_grid()
				grid.show()
				time.sleep(0.08)

	finally:
		clear_grid()
		grid.show()

	stop_animation()
