#data types,Numbers,Operations,Type conversions,f-strings
print(int("123") + int("345"))
#using the str function to convert integers from the len fn into letters 
print("Number of letter in your name:" + str(len(input('what is your name?\n'))))
#fstrings
checker = True
number = 58
print(f"the score is  {number} and this is {checker}")
#challenge: tip calculator
food_bill = input("what is your total bill \n")
tip = input("what percentage of tip would you like to give 12,15,30 \n")
people = input("how many people are you \n")
per_head_cost=(((100 + int(tip))/100)*int(food_bill))/int(people)
print(f"each person should pay: {round(per_head_cost,2)}")