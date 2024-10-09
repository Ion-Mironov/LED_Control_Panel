import time
import board
import adafruit_dotstar as dotstar

# Number of pixels on the LED strip
num_pixels = 144
pixels = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.5, auto_write=False)



def sequential_light_up(wait):
	# Start with all LEDs off and add a small delay
	pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(0.05)

	# Sequentially turn on all LEDs
	for i in range(num_pixels):
		pixels[i] = (255, 70, 0)    # Set each pixel to amber
		pixels.show()
		time.sleep(wait)            # Wait time between lighting each LED

	# Turn off all LEDs
	pixels.fill((0, 0, 0))
	pixels.show()

# Set the wait time before the next LED lights up (in milliseconds)
wait_time = 0.002

try:
	while True:
		sequential_light_up(wait_time)

except KeyboardInterrupt:
	# When Ctrl + C is pressed, clear all LEDs
	pixels.fill((0, 0, 0))		# Turn off all LEDs
	pixels.show()
	print("LEDs turned off. Exiting program.")
