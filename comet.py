import time
import board
import adafruit_dotstar as dotstar

# Number of pixels on the LED strip
num_pixels = 288
pixels = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.5, auto_write=False)



def comet_trail(color, tail_length, wait):
	# Start by having all LEDs off
	pixels.fill((0, 0, 0))
	pixels.show()

	for i in range(num_pixels + tail_length):				# Iterate through all LEDs + tail length for the trailing effect
		# Turn off all LEDs before lighting the next comet frame
		pixels.fill((0, 0, 0))

		# Create the comet effect by lighting up each pixel and applying a fade to the tail
		for j in range(tail_length):
			if i - j < num_pixels and i - j >= 0:			# Check that it's not out of bounds
				# Calculate the brightness factor for the tail (gradually fade from full brightness to dim)
				brightness_factor = 1 - (j / tail_length)
				faded_color = (
					int(color[0] * brightness_factor),
					int(color[1] * brightness_factor),
					int(color[2] * brightness_factor)
				)
				pixels[i - j] = faded_color					# Set the color for the current pixel in the tail

		pixels.show()
		time.sleep(wait)

# Define the comet color, tail length, and wait time between steps
color = (255, 0, 0)			# Comet color (Purple = 47, 1, 77) (Amber = 255, 77, 0)
tail_length = 50			# The length of the comet's tail (how many LEDs fade behind it)
wait = 0.002				# 200 milliseconds between lighting each step of the comet

try:
	while True:
		comet_trail(color, tail_length, wait)

except KeyboardInterrupt:
	# Ensure all LEDs are turned off when stopping the animation
	pixels.fill((0, 0, 0))
	pixels.show()
	print("Comet animation stopped and LEDs turned off.")
