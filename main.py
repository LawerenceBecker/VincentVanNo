import vanGogh
import turtle
from PIL import Image

image = Image.open("racoon_friend.jpeg", "r")

screen = turtle.Screen()
screen.colormode(255)

width, height = image.size

vanGogh.Gogh.spawn_turtle(image, width, height)