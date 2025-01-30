hello = "Denzel"
print("hello " + hello)

#input function 
name = input("what is your name ? ")
#using the capitalize function to capitalize the first letter 
name = name.capitalize()
#using len() to find the number of values in a string 
length = len(name)
print(length)
print("hello " + name + "!")

#band name generator
print('welcome to the band name generator')
city_name = input("what is the name of the city you grew up in \n")
pet_name = input("what's your pet's name\n")

print('your band name could be '+city_name.capitalize()+" "+pet_name.capitalize())