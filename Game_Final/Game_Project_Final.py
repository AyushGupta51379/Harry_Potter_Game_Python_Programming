'''
STUDENT NAME: GUPTA, AYUSH

ASSIGNMENT 2, COMP 1021
GAME THEME ON 0 (HARRY POTTER, MAGIC)
'''

import turtle

# Pygame for music

import pygame
file = 'HPT_No_Copyright_Music.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.

#Turtle graphics for graphics

# General parameters
window_height = 600
window_width = 600
window_margin = 50
update_interval = 25    # The screen update interval in ms, which is the
                        # interval of running the updatescreen function

# Player's parameters
player_size = 50        # The size of the player image plus margin
player_init_x = 0
player_init_y = -window_height / 2 + window_margin
player_speed = 10       # The speed the player moves left or right

# Enemy's parameters
enemy_number = 17        # The number of enemies in the game

enemy_size = 50         # The size of the enemy image plus margin
enemy_init_x = -window_width / 2 + window_margin
enemy_init_y = window_height / 2 - window_margin - 40
enemy_min_x = enemy_init_x
enemy_max_x = window_width / 2 - enemy_size * 7
    # The maximum x coordinate of the first enemy, which will be used
    # to restrict the x coordinates of all other enemies
enemy_kill_player_distance = 3
    # The player will lose the game if the vertical
    # distance between the enemy and the player is smaller
    # than this value

# Enemy movement parameters
enemy_speed = 2
enemy_speed_increment = 1
    # The increase in speed every time the enemies move
    # across the window and back
enemy_direction = 1
    # The current direction the enemies are moving:
    #     1 means from left to right and
    #     -1 means from right to left

# The list of enemies
enemies = []

# Laser parameter
laser_width = 2
laser_height = 15
laser_speed = 25
laser_kill_enemy_distance = 25
    # The laser will destory an enemy if the distance
    # between the laser and the enemy is smaller than
    # this value

# Gameover parameter, 0 means lost, 1 means won
final = 0

"""
    Handle the player movement
"""

# This function is run when the "Left" key is pressed. The function moves the
# player to the left when the player is within the window area
def playermoveleft():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range
    if x - player_speed > -window_width / 2 + window_margin:
        player.goto(x - player_speed, y)


# This function is run when the "Right" key is pressed. The function moves the
# player to the right when the player is within the window area
def playermoveright():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range
    if x + player_speed < window_width / 2 - window_margin:
        player.goto(x + player_speed, y)

def cheatmode():
    global cheat, chc2
    cheat += 1
    chc2 +=1

"""
    Handle the screen update and enemy movement
"""

# This function is run in a fixed interval. It updates the position of all
# elements on the screen, including the player and the enemies. It also checks
# for the end of game conditions.
def updatescreen():
    # Use the global variables here because we will change them inside this
    # function
    global enemy_direction, enemy_speed, count, count1, count2, count3, score, chc1, ch2, exc1, exc2, exs1, exs2

    # Move the enemies depending on the moving direction

    # The enemies can only move within an area, which is determined by the
    # position of enemy at the top left corner, enemy_min_x and enemy_max_x
    # x and y displacements for all enemies
    dx = enemy_speed * enemy_direction
    dy = 0

    # Part 3.3
    # Perform several actions if the enemies hit the window border
    x0 = enemies[0].xcor()
    if x0 + dx > enemy_max_x or x0 + dx < enemy_min_x:
        # Switch the moving direction
        enemy_direction = -enemy_direction
        dx = enemy_speed * enemy_direction
        
        # Bring the enemies closer to the player

        dy = -enemy_size / 2
        if enemy_direction == 1:
            enemy_speed = enemy_speed + enemy_speed_increment

        # Increase the speed when the direction switches to right again

    # Move the enemies according to the dx and dy values determined above
    for enemy in enemies:
        x, y = enemy.position()
        if cheat % 2 == 0:
            enemy.goto(x + dx, y + dy)
            if (x // 20) % 2 == 0:
                enemy.shape("e1.gif")
            else:
                enemy.shape("e2.gif")

    if bonus.isvisible():
        x, y = bonus.position()
        if x < -300:
            bonus.hideturtle()
            exs2 +=1
        
        elif cheat % 2 == 0:
            bonus.goto(x - 3, y)

    # Part 4.3 - Moving the laser
    # Perform several actions if the laser is visible
    
    if laser.isvisible():
        # Move the laser        
        laser.forward(laser_speed)
        if laser.ycor() >= window_height / 2:
            # Hide the laser turtle
            laser.hideturtle()

        # Check the laser against every enemy using a for loop
        for enemy in enemies:
            # If the laser hits a visible enemy, hide both of them
            # If the enemy is visible AND the laser is very close to the enemy...
            if enemy.isvisible() and laser.distance(enemy) <= laser_kill_enemy_distance :
                # Remove the enemy and the laser
                laser.hideturtle()
                enemy.hideturtle()
                
                # Stop if some enemy has been hit
                break
        if bonus.isvisible() and laser.distance(bonus) <= laser_kill_enemy_distance:
            count2 += 1
            if cheat % 2 == 0:
                exc2 += 1
            laser.hideturtle()
            bonus.hideturtle()

    if count > count1 or count2 > count3:
        score = count*20 + count2*100
        score2.clear()
        score2.goto(-220, 275)
        score2.write(score, font=("Arial", 10, "bold"))

    count1 = count  
    count3 = count2

    if exs2 > exs1:
        turtle.ontimer(bonus_enemy, 7000)
    elif exc2 > exc1 and (cheat % 2) == 0:
        turtle.ontimer(bonus_enemy, 7000)
    elif chc2 > chc1 and (cheat % 2) == 0:
        turtle.ontimer(bonus_enemy, 7000)
        
    exs1 = exs2
    exc1 = exc2
    chc1 = chc2

    # update the screen
    turtle.update()

    # Part 5.1 - Gameover when one of the enemies is close to the player
    
    
    # If one of the enemies is very close to the player, the game will be over
    for enemy in enemies:
        if enemy.ycor()- 0.85*player.ycor() < enemy_kill_player_distance and enemy.isvisible():
            # Show a message
            gameover("You lose!", score, 0)

            # Return and do not run updatescreen() again
            turtle.done()
            return

    # Part 5.2 - Gameover when you have killed all enemies
    count = 0
    for enemy in enemies:
                
        if not enemy.isvisible():
            
            # Increase count
            count += 1

        if count == enemy_number:
            
            score = count*20 + count2*100
            score2.clear()
            score2.goto(-220, 275)
            score2.write(score, font=("Arial", 10, "bold"))
            gameover("You win!", score, 1)
            turtle.done()
            
            return
          
    turtle.update()

    # Part 3.2 - Controlling animation using the timer event


    # Schedule the next screen update
    turtle.ontimer(updatescreen, update_interval)

bonus = turtle.Turtle()
turtle.addshape("b4.gif")
bonus.shape("b4.gif")
bonus.up()
bonus.hideturtle()   

def bonus_enemy():
    if not bonus.isvisible() and (cheat % 2) == 0:    
        bonus.goto(285, 260)
        bonus.showturtle()

"""
    Shoot the spell
"""

# This function is run when the player presses the spacebar. It shoots a laser
# by putting the laser in the player's current position. Only one laser can
# be shot at any one time.
def shootlaser():

    # Part 4.2 - the shooting function
    # Shoot the laser only if it is not visible
    # When the laser is available
    if not laser.isvisible():
        # Make the laser to become visible
        laser.showturtle()

        # Move the laser to the position of the player
        laser.goto(player.position())

"""
    Game start
"""
# This function contains things that have to be done when the game starts.
def gamestart(x, y):

    # Use the global variables here because we will change them inside this
    # function
    global player, laser

    start_button.clear()
    start_button.hideturtle()
    name.clear()
    instruction.clear()
    labels.clear()
    left.hideturtle()
    right.hideturtle()
    enemy_number_text.clear()
    ### Player turtle ###

    # Add the spaceship picture
    turtle.addshape("p7.gif")
    
    # Create the player turtle and move it to the initial position
    player = turtle.Turtle()
    player.shape("p7.gif")
    player.up()
    player.goto(player_init_x, player_init_y)

    # Part 2.1
    # Map player movement handlers to key press events
    turtle.onkeypress(playermoveleft, "Left")
    turtle.onkeypress(playermoveright, "Right")
    turtle.onkeypress(cheatmode, "c")
    turtle.listen()    

    ### Enemy turtles ###

    # Add the enemy pictures
    turtle.addshape("e1.gif")
    turtle.addshape("e2.gif")
    turtle.addshape("l4.gif")

    for i in range(enemy_number):
        # Create the turtle for the enemy
        enemy = turtle.Turtle()
        enemy.shape("e1.gif")
        enemy.up()

        # Move to a proper position counting from the almost top left corner
        enemy.goto(enemy_init_x + enemy_size * (i % 7), enemy_init_y - enemy_size * (i // 7))
        # Add the enemy to the end of the enemies list
        enemies.append(enemy)

    ### Laser turtle ###

    # Create the laser turtle using the square turtle shape
    laser = turtle.Turtle()
    laser.shape("l4.gif")
    # laser.color("white")

    # Change the size of the turtle and change the orientation of the turtle
    # laser.shapesize(laser_width / 20, laser_height / 20)
    laser.left(90)
    laser.up()

    # Hide the laser turtle
    laser.hideturtle()

    # Part 4.2 - Mapping the shooting function to key press event
    turtle.onkeypress(shootlaser, "space")

    score2.color('white')
    score2.up()
    score2.goto(-220, 275)
    score2.write(score, font=("Arial", 10, "bold"))

    score1.color('white')
    score1.up()
    score1.goto(-285, 275)
    score1.write("Score:", font=("Arial", 10, "bold"))

    turtle.bgpic("s1.gif")



    turtle.update()

    # Part 3.2 - Controlling animation using the timer event
    # Start the game by running updatescreen()
    turtle.ontimer(updatescreen, update_interval)
    
"""
    Game over
"""

# This function shows the game over message.
def gameover(message, score, fin):

    # Part 5.3 - Improving the gameover() function
    over = turtle.Turtle()
    over.hideturtle()

    over.pencolor("Red")
    if (fin==0):
        over.write(message+"\nFinal Score: "+str(score)+"\nKill all enemies next time!", align="center", font=("Times New Roman", 40, "bold"))
    else:
        if(score<100):
            over.write(message+"\nFinal Score: "+str(score)+"\nAlright!"+"\nYou can do better!", align="center", font=("Times New Roman", 50, "bold"))
        elif(score<200):
            over.write(message+"\nFinal Score: "+str(score)+"\nNice!", align="center", font=("Times New Roman", 55, "bold"))
        elif(score<300):
            over.write(message+"\nFinal Score: "+str(score)+"\nWell Done!", align="center", font=("Times New Roman", 55, "bold"))
        elif(score<400):
            over.write(message+"\nFinal Score: "+str(score)+"\nExcellent!", align="center", font=("Times New Roman", 55, "bold"))
        elif(score<700):
            over.write(message+"\nFinal Score: "+str(score)+"\nAll Records broken!", align="center", font=("Times New Roman", 50, "bold"))
        elif(score<1000):
            over.write(message+"\nFinal Score: "+str(score)+"\nNew World Record!!!", align="center", font=("Times New Roman", 40, "bold"))
        else:
            over.write(message+"\nFinal Score: "+str(score)+"\nDid You cheat?", align="center", font=("Times New Roman", 40, "bold"))
            
    turtle.update()
    
    
"""
    Set up main Turtle parameters
"""

def decrease_enemy_number(x, y):
    # Declare enemy_number as global
    global enemy_number
    if enemy_number > 1 :
        # decrease number of enemies by 1
        enemy_number -= 1
        # tell the turtle 'enemy_number_text' to clear what it has written
        enemy_number_text.clear()
        # tell the turtle 'enemy_number_text' to display the new value
        enemy_number_text.goto(80, 0)
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")

def increase_enemy_number(x, y):
    # Declare enemy_number as global
    global enemy_number
    if enemy_number < 49:
        # increase number of enemies by 1
        enemy_number += 1
        # tell the turtle 'enemy_number_text' to clear what it has written
        enemy_number_text.clear()
        # tell the turtle 'enemy_number_text' to display the new value
        enemy_number_text.goto(80, 0)
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
        
# Set up the turtle window
turtle.setup(window_width, window_height)
# no turtle.bgcolor("red")
turtle.bgpic("h1.gif")
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Set up the start_button

start_button = turtle.Turtle()
start_button.up()
start_button.goto(-40, -40)
start_button.color("white", "DarkGray")
start_button.begin_fill()
for _ in range(2):
    start_button.forward(80)
    start_button.left(90)
    start_button.forward(25)
    start_button.left(90)
start_button.end_fill()
start_button.shape("square")
start_button.color("white")

start_button.up()
start_button.goto(0, -35)
start_button.write("Start", font=("System", 12, "bold"), align="center")
start_button.goto(0, -28)
start_button.shapesize(1.25, 4)
start_button.color("")

# Set up other controls
name = turtle.Turtle()
name.hideturtle()
name.color('white')
name.up()
name.goto(-180, 200)
name.write("Magical Harry Game", font=("Arial", 23, "bold"))

# More in Display screen
instruction = turtle.Turtle()
instruction.hideturtle()
instruction.color('white')
instruction.up()
instruction.goto(-130, 160)
instruction.write("Control Harry Potter", font=("System", 13, "bold"))
instruction.goto(-130, 140)
instruction.write("using the arrow keys", font=("System", 13, "bold"))
instruction.goto(-130, 120)
instruction.write("and spacebar to cast christmas spell", font=("System", 13, "bold"))
instruction.goto(-130, 100)
instruction.write("and kill all ghosts to win!", font=("System", 13, "bold"))
instruction.goto(-130, 70)
instruction.write("20 points for killing ghosts", font=("System", 13, "bold"))
instruction.goto(-130, 50)
instruction.write("100 points for killing voldemort(s)", font=("System", 13, "bold"))
instruction.goto(-130, 30)
instruction.write("[Turn cheat mode on/off by pressing \'c\']", font=("System", 13, "bold"))


# Some global variables
score = 0
score1 = turtle.Turtle()
score1.hideturtle()

score2 = turtle.Turtle()
score2.hideturtle()

count3 = 0
count2 = 0
count1 = 0
count = 0
cheat = 0
chc1 = 0
chc2 = 0
exc1 = 0
exc2 = 0
exs1 = 0
exs2 = 1

labels = turtle.Turtle()
labels.hideturtle()
labels.color('white')
labels.up()
labels.goto(-120, 0) # Put the text next to the spinner control
labels.write("Number of ghosts:", font=("System", 12, "bold"))
enemy_number_text = turtle.Turtle()
enemy_number_text.hideturtle()
enemy_number_text.color("white")
enemy_number_text.up()
enemy_number_text.goto(80, 0)
enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
left = turtle.Turtle()
left.shape("arrow")
left.color("white")
left.up()
left.shapesize(0.5, 1)
left.left(180)
left.goto(60, 8)
left.onclick(decrease_enemy_number)
right = turtle.Turtle()
right.shape("arrow")
right.color("white")
right.up()
right.shapesize(0.5, 1)
right.goto(100, 8)
right.onclick(increase_enemy_number)

start_button.onclick(gamestart)
turtle.update()

# Switch focus to turtle graphics window
turtle.done()

'''
STUDENT NAME: GUPTA, AYUSH
ASSIGNMENT 2, COMP 1021
'''

