#Write a Python Program for Fibonacci numbers
Number = int(input("Enter the Range No.: "))
i = 0
value1 = 0
value2 = 1
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = value1 + value2
                      value1 = value2
                      value2 = Next
           print(Next)
           i = i + 1





