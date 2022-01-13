from turtle import*

goto(0,300)
up()
left(90)
forward(20)
left(270)
down()

write("Y_axis")

goto(0,-300)
goto(0,0)
goto(-300,0)
goto(300,0)

goto(0,0)
color("yellow")
left(45)
forward(300)

goto(0,0)
left(90)
forward(300)
color("red")
write("|x|=y")


up()
goto(0,0)
down()
a=range(2,10,2)
right(45)
goto(-30,0)
up()
a=[0,2,4,6,8,10]
for n in range(1,10):
	goto(-30,n*50)

	if n<6:
		write(a[n])
b=[0,-2,-4,-6,-8,-10]
for n in range(1,10):
	goto(-30,n*50*-1)

	if n<6:
		write(b[n])

for n in range(1,10):
	goto(n*50*-1,-30)

	if n<6:
		write(b[n])
		
for n in range(1,10):
	goto(n*50,-30)

	if n<6:
		write(a[n])
down()
	
	
done()