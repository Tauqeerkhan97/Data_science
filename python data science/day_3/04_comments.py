# print("hello Tauqeer")
# print("hello world")
# print("hey there whats are you doing ")
# print("no today your paper")
# print("you are from  'gpgc mansehra' dept of ai")
# print('''
#       i Am Tauqeer
#      Hello Everyone 
#       we are  present in  iit Mansehra 
# ''')

# print(2+6+90+21+65+9)

# import turtle
# import math

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Heart Shape Pattern")

# # Create a turtle
# heart = turtle.Turtle()
# heart.speed(0)  # Fastest speed
# heart.color("red")
# heart.pensize(2)

# # Function to draw a heart shape
# def draw_heart(size, x, y, color):
#     heart.penup()
#     heart.goto(x, y)
#     heart.pendown()
#     heart.color(color)
    
#     # Draw the heart shape using parametric equations
#     heart.begin_fill()
#     for t in range(0, 628, 5):  # 0 to 2*pi in steps of 0.05
#         t = t / 100
#         # Parametric equations for a heart shape
#         x_point = 16 * (math.sin(t) ** 3)
#         y_point = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
#         heart.goto(x + x_point * size, y + y_point * size)
#     heart.end_fill()

# Draw multiple hearts in a pattern
# colors = ["red", "pink", "lightpink", "hotpink", "deeppink"]

# for i in range(10):
#     size = 2 - i * 0.15
#     color = colors[i % len(colors)]
#     draw_heart(size, 0, -i*10, color)

# # Hide the turtle and display the result
# heart.hideturtle()
# screen.exitonclick()
# import turtle
# import math

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Animated Heart")

# # Create a turtle
# heart = turtle.Turtle()
# heart.speed(5)  # Medium speed for animation
# heart.color("red")
# heart.pensize(2)

# # Function to draw an animated heart
# def draw_animated_heart():
#     heart.penup()
#     heart.goto(0, 0)
#     heart.pendown()
    
#     # Draw the heart shape with animation
#     for t in range(0, 628, 2):  # Smaller steps for smoother animation
#         t = t / 100
#         # Parametric equations for a heart shape
#         x = 16 * (math.sin(t) ** 3)
#         y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
#         heart.goto(x * 10, y * 10)  # Scale up the heart

# # Draw the animated heart
# draw_animated_heart()

# # Hide the turtle and display the result
# heart.hideturtle()
# screen.exitonclick()

#stylish Rainbow

# import turtle
# import colorsys

# Setup screen
# turtle.bgcolor("black")
# turtle.speed(0)
# turtle.hideturtle()
# turtle.colormode(255)

# # Number of colors
# num_colors = 360
# colors = []

# # Generate rainbow colors using HSV
# for i in range(num_colors):
#     hue = i / num_colors
#     r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(hue, 1, 1)]
#     colors.append((r, g, b))

# turtle.pensize(2)

# # Draw the rainbow circular spirograph
# for i in range(720):  # Number of lines
#     turtle.color(colors[i % num_colors])
#     turtle.circle(150)  # Radius of circle
#     turtle.left(5)      # Angle step for rotation

# turtle.done()

