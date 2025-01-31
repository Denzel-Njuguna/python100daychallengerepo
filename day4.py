import random
#random.randint and .randrange will give me values that are whole between the range specified while .random gives me floating values and .uniform will give between and including the number between the range
# rand_num = random.randint(1,7)
# print(rand_num)
toss_number = random.randint(0,9)
toss_number = toss_number%2
if toss_number !=0:
    print("heads")
else:
    print("tails")
#lists
names_list = ["Denzel","jacob","christopher","kumbavu"]
names_list.remove("christopher")
print(names_list)

#who will pay the bill game
# the_list = []
# users_name = input("enter the users name\n")
# names = users_name.split(",")
# the_list.extend(names)
# user_total =len(the_list)
# unlucky_bastard = the_list[random.randint(0,user_total-1)]
# print(f"the one to pay the bill is {unlucky_bastard}")
#rock paper scissors game
the_title = '''


██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
'''


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper= '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
ascii_list = [rock,scissors,paper]
users_input = input(f"this is a game of {the_title} \n rock,scissors and paper\n please enter your choice \n").lower()
choices = ["rock","scissors","paper"]
comp_choice_index =random.randint(0,2)
ascii_index = choices.index(users_input)
print(f"user's choice is {ascii_list[ascii_index]}")
print(f"the computer choice is:{ascii_list[comp_choice_index]}")
comp_choice = choices[comp_choice_index]
if str(comp_choice) == str(users_input):
    print("It's a tie!")
elif (str(comp_choice) == "rock" and str(users_input) == "scissors") or \
     (str(comp_choice) == "scissors" and str(users_input) == "paper") or \
     (str(comp_choice) == "paper" and str(users_input) == "rock"):
    print("Computer wins!")
else:
    print("You win!")
