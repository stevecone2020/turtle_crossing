import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

scrolling_speed = 1 / (scoreboard.score / 0.1)

game_is_on = True
while game_is_on:
    time.sleep(scrolling_speed)
    screen.update()
    car_manager.new_car()
    car_manager.car_move()
    scoreboard.show_score()

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect turtle making it to the other side!
    if player.ycor() == 300:
        player.reset()
        scoreboard.level_up()










screen.exitonclick()