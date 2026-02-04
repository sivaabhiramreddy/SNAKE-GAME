# # # import random
# # #
# # # random_number = random.randint( 1 , 10)
# # #
# # # print(random_number)
# #
# # # states = ["new york", "nevada"]
# # #
# # # print(states[0])
# #
# #
# # # student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# # #
# # # max_score = 0
# # #
# # # for score in student_scores:
# # #     if(score > max_score):
# # #         max_score = score
# # #
# # # print(max_score)
# #
# #
# # # sum = 0
# # # for num in range(1,101):
# # #     sum += num
# # #
# # # print(sum)
# #
# #
# # import random
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# #
# # print("Welcome to the PyPassword Generator!")
# # nr_letters = int(input("How many letters would you like in your password?\n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))
# #
# # password_list = []
# #
# # for char in range(0 , nr_letters):
# #     password_list.append(random.choice(letters))
# # for chat in range(0 , nr_symbols):
# #     password_list.append(random.choice(symbols))
# # for char in range(0 , nr_numbers):
# #     password_list.append(random.choice(numbers))
# #
# # # print(password_list)
# # random.shuffle(password_list)
# #
# # password = ""
# # for char in password_list:
# #     password += char
# #
# # print(password)
# #
# #
# #
# import random
# # def my_function():
# #     print("Hello")
# #     print("Bye")
# #
# #
# # my_function(9)
#
#
# # a = input("enter name ")
# # display =""
# # # Loop through the list to get the word
# # for word in a:
# #     # Loop through every letter in the word "hello"
# #     for letter in word:
# #         # 1. ord(letter): Convert letter to number
# #         # 2. + 6: Add 6 to that number
# #         # 3. chr(...): Convert the new number back to a letter
# #         shifted_char = chr(ord(letter) + 6)
# #
# #         display += shifted_char
# #
# # print(display)
#
# # from turtle import Turtle, Screen
# # import turtle
# # turtle.colormode(255)
# #
# # timmy_the_turtle = Turtle()
# # timmy_the_turtle.shape("turtle")
#
# # colours = ["red", "green", "blue", "orange" , "yellow" ,"pink", "brown", "grey"]
# # direction = [0 , 90 , 180 , 270]
# # # timmy_the_turtle.pensize(15)
# # timmy_the_turtle.speed(500)
# # def draw_shape(num_side):
# #     angle = 360 / num_side
# #     for _ in range(num_side):
# #         timmy_the_turtle.forward(100)
# #         timmy_the_turtle.right(angle)
# #
# # for side in range(3,11):
# #     timmy_the_turtle.color(random.choice(colours))
# #     draw_shape(side)
#
#
# # for _ in range(200):
# #     timmy_the_turtle.color(random.choice(colours))
# #     timmy_the_turtle.forward(30)
# #     timmy_the_turtle.setheading(random.choice(direction))
#
# # timmy_the_turtle.speed("fastest")
# # def random_color():
# #     r = random.randint(0 , 255)
# #     g = random.randint(0 , 255)
# #     b = random.randint(0 , 255)
# #     color = (r,g,b)
# #     return color
# #
# #
# # def draw_spirograph(gap):
# #     for _ in range(int(360 / gap)):
# #         timmy_the_turtle.color(random_color())
# #         timmy_the_turtle.circle(100)
# #         timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap)
# #
# # draw_spirograph(5)
#
# # screen = Screen()
# # screen.exitonclick()
#
#
#
# from turtle import Turtle, Screen
# import turtle
# screen = Screen()
#
# timmy_the_turtle = Turtle()
#
# def move_forwards():
#     timmy_the_turtle.forward(10)
#
# def move_backwards():
#     timmy_the_turtle.backward(10)
#
# def turn_left():
#     new_heading = timmy_the_turtle.heading() + 10
#     timmy_the_turtle.setheading(new_heading)
#
# def turn_right():
#     new_heading = timmy_the_turtle.heading() - 10
#     timmy_the_turtle.setheading(new_heading)
#
# def clear():
#     timmy_the_turtle.clear()
#     timmy_the_turtle.penup()
#     timmy_the_turtle.home()
#     timmy_the_turtle.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards , "w")
# screen.onkey(move_backwards , "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right , "d")
# screen.onkey(clear , "c")
#
# screen.exitonclick()



from turtle import Screen, Turtle
from snakecreation import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)
# starting_position = [(0 ,0), (-20, 0) , (-40, 0)]

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on= False
        scoreboard.game_over()

    #detect collision with tail

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()