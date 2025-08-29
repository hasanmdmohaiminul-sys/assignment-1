x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))
if x>0:
    if y>0:
        print("1st quadrant")
    else:
        print("4th quardant")
elif y>0:
    print("2nd quadrant")
else:
    print("3rd quadrant")
