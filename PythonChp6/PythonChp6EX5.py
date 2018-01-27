########################################
#Chapter 6 Exercise 5
#Morgan Gates
#Exercise 5: Take the following Python code that stores a string:`
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the colon character 
#and then use the float function to convert the extracted string into a floating point number.
########################################

str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
end = len(str)

number = str[start+1:end]

fnumber = float(number)

print (number)
print (fnumber)