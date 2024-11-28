import turtle

def drawSpiral(turtle, lineLength):
    if lineLength > 0:
        turtle.forward(lineLength)
        turtle.right(90)
        drawSpiral(turtle, lineLength - 5)

def drawTree(branchLength, turtle):
    if branchLength > 5:
        turtle.forward(branchLength)
        turtle.right(20)
        drawTree(branchLength-15, turtle)
        turtle.left(40)
        drawTree(branchLength-15, turtle)
        turtle.right(20)
        turtle.backward(branchLength)



if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()
    myTurtle.pencolor('green')
    myTurtle.fillcolor('green')
    turtle.begin_fill()
    #myTurtle.shapesize(5,5,5)
    #drawSpiral(myTurtle, 100)
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    drawTree(90, myTurtle)

    myScreen.exitonclick()

