from turtle import *
for i in range(3, 7):
    goc_bu = 360/i 
    if i % 2 == 0:
        color("red")
    else:
        color("blue")
    for j in range(1, i+1):
        forward(100)
        left(goc_bu)
mainloop()
