ans = input("enter the value you wonna check \n")
if int(ans) % 2  == 0:
    print(f"{ans} is an even number")
else:
    print(f"{ans} is an odd number")
#python pizza place 
bill = 0
size = input("what size of pizza would you like?small,medium or large \n")
pepperoni = input("would you like pepperoni with your pizza? yes or no \n")
extra_cheese = input("would you like extra cheese with your pizza? yes or no \n")
if size == "small":
    bill = 15
    if pepperoni == 'yes':
        bill +=2

if size == "medium":
    bill = 20

if size == "large":
    bill = 25

if size == "medium" or size == "large" and pepperoni == "yes":
    bill += 3

if extra_cheese == "yes":
    bill+=1
print(f"you bill is: {bill}")
bill = 0
