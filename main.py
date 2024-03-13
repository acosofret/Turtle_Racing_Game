# INCOMPLETE: My method required multiprocessing and I couldn't make it work (run turtles simultaneous)
# The instructor took a very different method, as steps below:
# generate multiple turtles with for loop (using colors list)
# save them in a all_turtles list
# set a while game is on condition triggered by user input
# run a while game is on loop, where each turtle moves a randomly number between 1 and 10
# NOTE: the speed is controlled by distance, not by actually speed like I tried
# add a stopping condition as if the turtle x coord is greater than 230: print turtle color, and stop while loop
# the adding user win loss conditions

import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "yellow", "blue", "black", "green"]
speeds = [1.0, 2.1, 3.2, 4.3, 5.4]

tim_red = Turtle()
tim_red.shape("turtle")
tim_red.color(colors[0])
tim_yellow = Turtle()
tim_yellow.shape("turtle")
tim_yellow.color(colors[1])
tim_blue = Turtle()
tim_blue.shape("turtle")
tim_blue.color(colors[2])
tim_black = Turtle()
tim_black.shape("turtle")
tim_black.color(colors[3])
tim_green = Turtle()
tim_green.shape("turtle")
tim_green.color(colors[4])


user_bet = screen.textinput("Ready to bet?", "Who will win the race?\n(RED, YELLOW, BLUE, BLACK or GREEN)")


def turtle_ready():
	random.shuffle(speeds)
	tim_red.penup()
	tim_red.goto(-230, -100)
	tim_red.speed(speeds[0])

	tim_yellow.penup()
	tim_yellow.goto(-230, -50)
	tim_yellow.speed(speeds[1])

	tim_blue.penup()
	tim_blue.goto(-230, 0)
	tim_blue.speed(speeds[2])

	tim_black.penup()
	tim_black.goto(-230, 50)
	tim_black.speed(speeds[3])

	tim_green.penup()
	tim_green.goto(-230, 100)
	tim_green.speed(speeds[4])


def turtle_go():
	tim_red.forward(400)
	tim_yellow.forward(400)
	tim_blue.forward(400)
	tim_black.forward(400)
	tim_green.forward(400)


def return_winner():
	max_speed = max(speeds)
	if speeds[0] == max_speed:
		winner = "red"
	elif speeds[1] == max_speed:
		winner = "yellow"
	elif speeds[2] == max_speed:
		winner = "blue"
	elif speeds[3] == max_speed:
		winner = "black"
	elif speeds[4] == max_speed:
		winner = "green"
	else:
		winner = "Something's wrong. We're experiencing an error."
	if winner == user_bet:
		print("CONGRATULATIONS! You won !")
	else:
		print("Unfortunately you lost. Maybe another time...")
	print(f"The {winner} Turtle won the race.")


turtle_ready()
tim_red.speed(speeds[0])
tim_yellow.speed(speeds[1])
tim_blue.speed(speeds[2])
tim_black.speed(speeds[3])
tim_green.speed(speeds[4])
turtle_go()
return_winner()

print(speeds)


screen.exitonclick()

# _______________________________________________________________________________

# import random
# import time
# import multiprocessing
# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(width=500, height=400)
# colors = ["red", "yellow", "blue", "black", "green"]
# speeds = [1.0, 2.1, 3.2, 4.3, 5.4]
#
# tim_red = Turtle()
# tim_red.color(colors[0])
# tim_yellow = Turtle()
# tim_yellow.color(colors[1])
# tim_blue = Turtle()
# tim_blue.color(colors[2])
# tim_black = Turtle()
# tim_black.color(colors[3])
# tim_green = Turtle()
# tim_green.color(colors[4])
#
#
# user_bet = screen.textinput("Ready to bet?", "Who will win the race?\n(RED, YELLOW, BLUE, BLACK or GREEN)")
#
#
# def turtle_ready():
# 	random.shuffle(speeds)
# 	tim_red.penup()
# 	tim_red.goto(-230, -100)
# 	tim_red.speed(speeds[0])
#
# 	tim_yellow.penup()
# 	tim_yellow.goto(-230, -50)
# 	tim_yellow.speed(speeds[1])
#
# 	tim_blue.penup()
# 	tim_blue.goto(-230, 0)
# 	tim_blue.speed(speeds[2])
#
# 	tim_black.penup()
# 	tim_black.goto(-230, 50)
# 	tim_black.speed(speeds[3])
#
# 	tim_green.penup()
# 	tim_green.goto(-230, 100)
# 	tim_green.speed(speeds[4])
#
#
# # def turtle_go():
# # 	p1 = multiprocessing.Process(target = tim_red.forward(400))
# # 	p2 = multiprocessing.Process(target = tim_yellow.forward(400))
# # 	p3 = multiprocessing.Process(target = tim_blue.forward(400))
# # 	p4 = multiprocessing.Process(target = tim_black.forward(400))
# # 	p5 = multiprocessing.Process(target = tim_green.forward(400))
# #
# # 	if __name__ == '__main__':
# # 		p1.start()
# # 		p2.start()
# # 		p3.start()
# # 		p4.start()
# # 		p5.start()
#
#
# def return_winner():
# 	max_speed = max(speeds)
# 	if speeds[0] == max_speed:
# 		winner = "red"
# 	elif speeds[1] == max_speed:
# 		winner = "yellow"
# 	elif speeds[2] == max_speed:
# 		winner = "blue"
# 	elif speeds[3] == max_speed:
# 		winner = "black"
# 	elif speeds[4] == max_speed:
# 		winner = "green"
# 	else:
# 		winner = "Something's wrong. We're experiencing an error."
# 	if winner == user_bet:
# 		print("CONGRATULATIONS! You won !")
# 	else:
# 		print("Unfortunately you lost. Maybe another time...")
# 	print(f"The {winner} Turtle won the race.")
#
#
# turtle_ready()
# tim_red.speed(speeds[0])
# tim_yellow.speed(speeds[1])
# tim_blue.speed(speeds[2])
# tim_black.speed(speeds[3])
# tim_green.speed(speeds[4])
# # turtle_go()
# p1 = multiprocessing.Process(target=tim_red.forward(400))
# p2 = multiprocessing.Process(target=tim_yellow.forward(400))
# p3 = multiprocessing.Process(target=tim_blue.forward(400))
# p4 = multiprocessing.Process(target=tim_black.forward(400))
# p5 = multiprocessing.Process(target=tim_green.forward(400))
#
# if __name__ == '__main__':
# 	p1.start()
# 	p2.start()
# 	p3.start()
# 	p4.start()
# 	p5.start()
#
# return_winner()
#
# print(speeds)
#
#
# screen.exitonclick()
