#to accept a filename from the user and print the extension of that
FileName= input("Enter Filename: ")
F = FileName.split(".")
print ("Extension of the file is : " + F[-1])

#to print area of a circle
Name = float(input("Input the radius of the circle(in cms): "))
Area = 3.14*(Name*Name)
print("The area of the circle with radius is: ", Area)


