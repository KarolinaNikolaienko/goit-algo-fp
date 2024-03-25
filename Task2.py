import matplotlib.pyplot as plt
import matplotlib.patches as patches
import turtle

def tree(t, order, size):
    if order == 0:
        t.color("green")
        t.circle(3)
        t.color("brown")
        return
    else:
        t.forward(size)
        t.left(30)
        tree(t, order - 1, size * 3 / 4)
        t.right(60)
        tree(t, order - 1, size * 3 / 4)
        t.left(30)
        t.backward(size)

def main():
    order = int(input("Введіть рівень рекурсії: "))

    window = turtle.Screen()
    window.title("Pythagoras Tree")
    window.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    #t.hideturtle()
    t.pen(pencolor="brown", fillcolor="lightblue")
    t.left(90)
    t.penup()
    t.backward(200)
    t.pendown()

    tree(t, order, 100)
    
    window.mainloop()

if __name__ == "__main__":
    main() 