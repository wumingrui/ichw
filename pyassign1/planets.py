Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> import turtle
>>> import math
>>> def  oval(k,a):
	k.penup()
	k.goto(a,0)
	k.pendown()
	c=50
	b=(a**2-2500)**0.5
	for x in range(1,1000,2):
		t=math.tan(math.radians(x))
		c=math.cos(math.radians(x))
		m=(1/(1/a**2+t**2/b**2))**0.5*(c**2)**0.5/c
		n=t*m
		k.speed(1000/((m-c)**2+n**2)**0.5)
		k.goto(m,n)

>>>a=turtle.Turtle()
>>>b=turtle.Turtle()
>>>c=turtle.Turtle()
>>>d=turtle.Turtle()
>>>e=turtle.Turtle()
>>>f=turtle.Turtle()
>>>g=turtle.Turtle()
>>>a.shape("circle")
>>>b.shape("circle")
>>>c.shape("circle")
>>>d.shape("circle")
>>>e.shape("circle")
>>>f.shape("circle")
>>>g.shape("circle")
>>>b.color("blue")
>>>c.color("green")
>>>d.color("black")
>>>e.color("red")
>>>a.color("yellow")
>>>f.color("orange")
>>>g.color("pink")
>>>a.penup()
>>>a.goto(-50,0)
>>>a.pendown()
>>>oval(b,69)
>>>oval(c,100)
>>>oval(d,115)
>>>oval(e,124)
>>>oval(f,140)
>>>oval(g,170)







