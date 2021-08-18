"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers = {}

# Create a dictionary of callers
# key:  phone number
# value:  time spent on calls
for call in calls:
	sending = call[0]
	receiving = call[1]
	length = int(call[3])

	# For person sending call
	if not sending in numbers:
		numbers[sending] = length
	else:
		numbers[sending] += length

	# For person receiving call
	if not receiving in numbers:
		numbers[receiving] = length
	else:
		numbers[receiving] += length

max_duration = None
max_caller = None

for number in numbers:
	if max_duration==None:
		max_caller = number
		max_duration = numbers[number]
	elif numbers[number]>max_duration:
		max_caller = number
		max_duration = numbers[number]

print("%s spent the longest time, %d seconds, on the phone during September 2016." % (max_caller,max_duration))