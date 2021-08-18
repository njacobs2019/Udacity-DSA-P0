"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


my_dict = {}

# 1. Traverse call log and fill dict with unique outgoing calls
for call in calls:
	my_dict[call[0]]=1

# 2. Traverse call log and remove numbers from dict that receive calls
for call in calls:
	called = call[1]
	if called in my_dict:
		del my_dict[called]

# 3. Traverse text log and remove numbers from dict that send or receive calls
for text in texts:
	num1 = text[0]
	num2 = text[1]

	if num1 in my_dict:
		del my_dict[num1]

	if num2 in my_dict:
		del my_dict[num2]

# 4. Convert keys to a list
my_list = list(my_dict.keys())
my_list.sort()

# 5. Print output
print("These numbers could be telemarketers:")
for num in my_list:
	print(num)