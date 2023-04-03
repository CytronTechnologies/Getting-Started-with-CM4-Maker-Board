import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

 
# Connect the CM4 Maker Board grove port pin 2 to SDA OLED Display:
RST=None
SDA = 2

# 128x32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load fonts.
#font = ImageFont.load_default()
font1 = ImageFont.truetype('/usr/share/fonts/truetype/piboto/PibotoCondensed-Italic.ttf', 14)
font2 = ImageFont.truetype('/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf', 12)
font3 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 16)


while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    Day = time.strftime("%A")
    Date = time.strftime("%d/%m/%y")
    Time = time.strftime("%I:%M:%S%p")

    # Write two lines of text.
    draw.text((x, top+0),    str(Day),  font=font1, fill=255)
    draw.text((x, top+22),    str(Date),  font=font2, fill=255)
    draw.text((x, top+42),    str(Time),  font=font3, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)

