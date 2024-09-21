import time
import board
import adafruit_dotstar as dotstar

# Number of pixels on the LED strip
num_pixels = 30
pixels = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.5, auto_write=False)

def sequential_light_up(wait):
    # Turn off all LEDs and add a small delay
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.05)

    # Sequentially turn on all LEDs
    for i in range(num_pixels):
        pixels[i] = (255, 70, 0)    # Set each pixel to red
        pixels.show()
        time.sleep(wait)            # Wait time between lighting each LED

    # Turn off all LEDs
    pixels.fill((0, 0, 0))
    pixels.show()

# Set the wait time in seconds
wait_time = 0.04

while True:
    sequential_light_up(wait_time)
