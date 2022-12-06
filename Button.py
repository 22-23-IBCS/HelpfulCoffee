from graphics import*
from Button import*

def main():

    win = GraphWin("Character Creation", 800, 600)

    B1 = Button(win, Point(650, 50), Point(750, 125), "salmon", "Face")

    B2 = Button(win, Point(650, 150), Point(750, 225), "salmon", "Big Eyes")
    B3 = Button(win, Point(650, 250), Point(750, 325), "salmon", "Small Eyes")

    Face = Oval(Point(150, 50), Point(550, 550))
    #Face.draw(win)
    bigEye1 = Circle(Point(350, 250), 40)
    #bigEye1.draw(win)
    bigEye2 = Circle(Point(450, 250), 40)
    #bigEye2.draw(win)
    smallEye1 = Circle(Point(350, 250), 20)
    smallEye2 = Circle(Point(450, 250), 20)

    Q = QuitButton(win, Point(650, 500), Point(750, 575))

    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            smallEye1.draw(win)
            smallEye2.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
