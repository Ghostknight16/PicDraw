import turtle
from PIL import Image

# Load the image
image = Image.open(r"C:\Users\Ghost\pic_draw\vegeta1.jpg")
image = image.convert('RGB')

# Set up turtle screen
screen = turtle.Screen()
screen.setup(width=image.width, height=image.height)
turtle_screen = turtle.Turtle()
turtle_screen.penup()
turtle_screen.hideturtle()

# Set the turtle speed
# turtle_screen.speed(0)  # Set to the fastest speed (no animation)

# Turn off animation
turtle.tracer(0)

# Set the step size for drawing squares
step = 10

# Loop through each pixel of the image
for x in range(0, image.width, step):
    for y in range(0, image.height, step):
        # Get the RGB values of the pixel
        r, g, b = image.getpixel((x, y))

        # Set the turtle color based on RGB values
        turtle_screen.color((r / 255, g / 255, b / 255))

        # Lift the pen and move to the new position
        turtle_screen.penup()
        turtle_screen.goto(x - image.width // 2, image.height // 2 - y)

        # Put the pen down to start drawing
        turtle_screen.pendown()

        # Draw a square
        turtle_screen.begin_fill()
        for _ in range(4):
            turtle_screen.forward(step)
            turtle_screen.right(90)
        turtle_screen.end_fill()

# Keep the turtle window open
turtle.done()
