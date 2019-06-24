    
from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in colors:
    color(i)
    begin_fill()
    for j in range(2):
        fd(50)
        left(90)
        fd(100)
        left(90)
    fd(50)
    end_fill()
mainloop()