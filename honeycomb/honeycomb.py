from turtle import Turtle
tor = Turtle()
tor.reset()
for honeycomb in range(1):
    for iterations in range(6):
        print(f'hexagon#{iterations} side# - pos{tor.pos()}')
        for comb in range(6):
            tor.forward(60)
            tor.right(60)
            print(f'hexagon#{iterations} side#{comb} pos{tor.pos()}')
        tor.forward(60)
        tor.left(60)
    tor.forward(60)
    tor.right(60)
    tor.forward(60)
    tor.left(60)
print(tor.position())