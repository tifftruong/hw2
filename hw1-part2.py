#### Part 2
s = "This is a test string for hw1."
lst = [1, 2, 3, 4, 5, 6]

print("=1=")
# 1: iterated operation over list

# Write code that iterates over each element of lst using a for loop, printing
# each element on a new line

print("=2=")
# 2: summing values of a list
# Write code that adds up all the elements of lst
# using a for loop, then prints out the sum. (hint: you will need to add to the
# variable total at every step of the for loop)
#
# Note: this is the example I used to teach you the accumulation pattern in
# lecture. Try to reconstruct the code here without looking at that code.
# You'll be glad for working through it here when you get to part III of
# this HW and have to use the accumulation pattern in a more creative way.

total = 0
# fill in the rest here

print("=3=")
# 3: splitting strings
# Write code that splits s into a list separate words
# (where each word is defined to be any series of characters separated by a
# whitespace). Print out the list using a for loop (as in (1)), one word per line.

print("=4=")
# 4: replacing an element of a list
# Replace the element of lst whose value is four with the value 'four' and
# then print lst (you can do this with indexing if you like)

print("=5=")
# 5: print out a file, verbatim
# Read and print each line contained in 'test.txt'.  Your program should
# output the text exactly as it is in test.txt.
# (Hint: you may need to use rstrip() to remove the newline character at the end
# of each line, to avoid getting an extra blank line between each real line.)

fname = "test.txt"
# fill in the rest here

print("=6=")
# 6: The next three exercises are about printing only 
# certain items from a list and/or string.
# (see instructions for parts 6a, 6b, 6c)

dogList = ["Akita","Alaskan Malamute","Australian shepherd","Australian cattle dog","Basset hound","Beagle","Boston terrier","Bulldog","Chihuahua","Cocker Spaniel","Collie","French Bulldog","Golden Retriever","Great Dane","Poodle","Russell Terrier","Scottish Terrier","Siberian Husky","Skye terrier","Smooth Fox terrier","Terrier","Whippet"]

print("==6a==")
# 6a iterate over dogList. 
# If the list item contains "terrier" or "Terrier", print out the 
# character number where the string "Terrier" or "terrier" starts
# For example, "Boston Terrier" should result in:
# 7
# However, if the line does not contain "terrier" or "Terrier", 
# your code should print "-1"
# hint: use find() (see supplement two)


print("==6b==")
#6b:
binList = [0,1,1,0,1,1,0]

# Iterate over binList. If the current item equals 1
# print "One". Otherwise, don't print anything.


print("==6c==")
# 6c
# Now, iterate over dogList. print out only the items that contain the string Bulldog.
# Case does not matter, you should match bulldog or Bulldog
# hint: You will need to use if. Also, find() may help.
