"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#########
## Part A

# Function to extract area code from phone number
# Input:  string
# Output: string
def area(number):
	if number[0]=="(":             # case: fixed line
		upper = number.find(")")+1
		return number[0:upper]
	elif number.find(" ") != -1:   # case: mobile number
		return number[0:4]
	else:                          # case: telemarketer
		return  "tele"

bangalore_dict = {}
# keys are area codes that have been called by Bangalore
# values are number of times that key has been called

# Fills the dictionary
for call in calls:
	caller = area(call[0])
	called = area(call[1])

	if caller=="(080)":
		if called in bangalore_dict:
			bangalore_dict[called]+=1
		else:
			bangalore_dict[called]=1

# Turns the keys of the dictionary into a list and sorts them
my_list = list(bangalore_dict.keys())
my_list.sort()

# Prints the list
print("The numbers called by people in Bangalore have codes:")
for item in my_list:
	print(item)


#########
## Part B

sum = 0   # number of outgoing calls from Bangalore
for key in bangalore_dict:
	sum += bangalore_dict[key]

in_bangalore = bangalore_dict["(080)"]

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % (in_bangalore/sum*100))