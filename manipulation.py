#Request the user to input a sentence
str_manip = input("Write a sentence:")

#Finding the number of characters in the sentence
length = len(str_manip) #Using the len() command to find the length of a sentence
print(length) #Printing the output

#Replacing the last letter with the @
last_letter = str_manip[-1] #finding the last letter of the sentence
replace_letter = str_manip.replace(last_letter,"@") #replacing the all the characters with last letter with @
print(replace_letter) #Printing the output

#Writing the last three letters backwards
three_backwards = str_manip[-3:] #Finding the last three letters of the sentence
rev_three = three_backwards[::-1] #Using split to reverse the last three letters
print(rev_three) #Printing the output

#Writing a five letter word using first three letters and last two letters of the sentence
five_letter_word = str_manip[:3] + str_manip[-2:] #Finding the first three letters and the last two letters 
print(five_letter_word) #Printing the output
