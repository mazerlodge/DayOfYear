
# Global vars
DAY_IDX = 0
MONTH_IDX = 1
YEAR_IDX = 2
dateParts = []


def getDaysInMonth(monthNum, yearNum):
	# Return number of days in month provided.  
	
	maxDaysInMonth = 0
	
	if (monthNum <= 7):
		if (monthNum % 2 == 0):
			maxDaysInMonth = 30
		else:
			maxDaysInMonth = 31
	else: 
		if (monthNum % 2 == 0):
			maxDaysInMonth = 31
		else:
			maxDaysInMonth = 30

	if (monthNum == 2):
		maxDaysInMonth = 28

		if (yearNum % 4 == 0):
			maxDaysInMonth = 29
			if (yearNum % 100 == 0) and (yearNum % 400 != 0):
				maxDaysInMonth = 28
					
	return maxDaysInMonth
	

def isDateValid(rawDate):
	# Returns true if the date specified is in mm/dd/yyyy format

	bValid = False
	rawDateParts = rawDate.split("/")

	try:
		# validate parts are, you know, valid. 
		monthPart = int(rawDateParts[0])
		dayPart = int(rawDateParts[1])
		yearPart = int(rawDateParts[2])

		# check range of values provided 
		if monthPart > 12 or monthPart < 1 \
		   or yearPart > 2250 or yearPart < 1776 \
		   or dayPart > 31 or dayPart < 1:
		   raise Exception("part of date out of range")
		   
		# make dur dayPart is within range of number of days in month.
		maxDaysInMonth = getDaysInMonth(monthPart, yearPart)
		if dayPart <= maxDaysInMonth:
			dateParts.append(dayPart)
			dateParts.append(monthPart)
			dateParts.append(yearPart)
			bValid = True
		
	except: 
		bValid = False

	return bValid


def countDaysToDate(rawDate):
	# Return number of days between Jan 1 and date specified, inclusive.
	
	dayCount = 0 
	
	# add days for full months up to the month specified
	for x in range(1,dateParts[MONTH_IDX]):
		dayCount = dayCount + getDaysInMonth(x, dateParts[YEAR_IDX])

	# add days for date specified up to (and including) day in date
	dayCount = dayCount + dateParts[DAY_IDX]

	return dayCount	


# Main execution starts here.
rawDate = input("Enter Date mm/dd/yyyy: ")
if (isDateValid(rawDate)):
	dayCount = countDaysToDate(rawDate)
	print(f"Number of days (aka Julian Day) to {rawDate} is {dayCount}")
else:
	print(f"Unable to interpret date {rawDate} provided.")
	