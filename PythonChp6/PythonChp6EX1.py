#####################################
#Chapter 6 Exercise 1
#Morgan Gates
#Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
#printing each letter on a separate line, except backwards.
#####################################
word = "lolipop"

index = len(word) - 1

rword = ""

while index >=0:
	load = word[index]
	index = index - 1
	rword= rword + load
	
print (rword)