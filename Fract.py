import turtle

turtle.title('Fractal')
screen = turtle.Screen()
screen.setup(width= 1.0, height= 1.0)
screen.bgcolor(1,.5,.7)
t = turtle.Turtle()
t.shape('turtle')
t.speed(0)

def tree(size, thick, levels, angle, bark, leaf):
    if levels == 0:
        t.color(leaf)
        t.dot(thick*thick)
        t.color(bark)
        return        
    t.pensize(thick)
    t.forward(size)
    t.right(angle)
    tree(size * 0.8, thick, levels - 1, angle, bark, leaf)
    t.left(angle * 2)
    tree(size * 0.8, thick, levels - 1, angle, bark, leaf)
    t.right(angle)
    t.backward(size)


def snowflake_side(length, levels):
	if levels == 0:
		t.forward(length)
		return
	length /= 3.0
	snowflake_side(length, levels - 1)
	t.left(60)
	snowflake_side(length, levels - 1)
	t.right(120)
	snowflake_side(length, levels - 1)
	t.left(60)
	snowflake_side(length, levels - 1)


def create_snowflake(sides, length):
	colors = ["green", "blue", "orange", "purple", "red", "yellow"]
	for i in range(sides):
		t.color(colors[i])
		snowflake_side(length, sides)
		t.right(360 / sides)

# t.color('white')
# t.goto(-200, 150)
# create_snowflake(5, 300)

t.left(90)
tree(50, 5, 8, 22, 'purple', 'red')

turtle.mainloop()