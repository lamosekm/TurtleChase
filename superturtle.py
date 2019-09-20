from turtle import Turtle
from random import randint, choice

def rancolor():
  """ This method returns a string from a list of colors available to Turtle's .color() method """
  colors = ["brown", "darkorange", "maroon", "crimson", "navy", "salmon", "tomato", "khaki", "gold", "hotpink", "springgreen", "blue", "cyan", "purple", "green", "red", "yellow", "teal"]
  return choice(colors)

class SuperTurtle(Turtle):
    """
    Our wrapper class of the turtle.Turtle object
    """

    def __init__(self, shape='turtle'):
        """
        This is the turtle's constructor with a default shape of "turtle"
        """
        Turtle.__init__(self)
        self.color(rancolor())
        self.shape(shape)
        self.penup()
        self.speed(9999)
        self.goto_random()

    def goto_random(self):
        """
        Simple function that sends a turtle to a random location on
        a 400x400 canvas
        """
        self.goto(randint(-200,200), randint(-200,200))

    def triangle(self, length=50):
        """
        Draws an equilateral triangle with a default length of 50
        """
        self.pendown()
        self.forward(length)
        self.left(120)
        self.forward(length)
        self.left(120)
        self.forward(length)

    def square(self, length=120):
        """
        Draws a square with a default length of 120
        """
        self.pendown()
        for x in range(4):
            self.forward(length)
            self.left(90)

    def home(self):
        """
        Returns to center position
        """
        self.goto(0,0)

    def turn_right(self):
        """
        Rotate right 
        """
        self.right(45) # this is a magic number, it's a fixed value that requires manual change

    def turn_left(self):
        """
        rotate left
        """
        self.left(45) # this is a magic number, it's a fixed value that requires manual change

    def move_forward(self):
        """
        move forward a bit
        """
        self.forward(40)


    def star(self):
        """
        Draws a 5-point star with a fixed length of 140
        """
        self.pendown()
        for x in range(5):
            self.forward(140)
            self.left(145)