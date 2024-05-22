import turtle
import math


def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return

    # Draw the trunk
    t.forward(branch_length)
    position = t.position()
    heading = t.heading()

    # Draw the right branch
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)


    t.setposition(position)
    t.setheading(heading)

    # Draw the left branch
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    t.setposition(position)
    t.setheading(heading)

def main():
    # Setup turtle
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")

    # Position the turtle
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    # Get recursion level and angle from user
    recursion_level = int(screen.textinput("Recursion Level", "Enter the level of recursion (e.g., 5): "))
   
    # Initial branch length
    initial_branch_length = 120

    # Draw the tree
    draw_pythagoras_tree(t, initial_branch_length, recursion_level)

    # Hide turtle and finish
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

