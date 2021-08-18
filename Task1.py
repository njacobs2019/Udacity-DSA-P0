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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers = {}

# iterate over the call log
for call in calls:
	num1 = call[0]
	num2 = call[1]
	if not num1 in numbers:
		numbers[num1]=1
	if not num2 in numbers:
		numbers[num2]=1

# iterate over the text log
for text in texts:
	num1 = text[0]
	num2 = text[1]
	if not num1 in numbers:
		numbers[num1]=1
	if not num2 in numbers:
		numbers[num2]=1

print("There are %d different telephone numbers in the records." % len(numbers))

"""
Note on Complexity (excluding initial reading):

Time complexity:
  - Worst:  O(n)

Space complexity:
  - Worst:  O(n)
"""