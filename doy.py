
def isDateValid(rawDate):

	bValid = False
	dateParts = rawDate.split("/")

	try:
		# validate parts are, you know, valid. 
		monthPart = int(dateParts[0])
		dayPart = int(dateParts[1])
		yearPart = int(dateParts[2])

		# check range of values provided 
		if monthPart > 12 or monthPart < 1 \
		   or yearPart > 2250 or yearPart < 1776 \
		   or dayPart > 31 or dayPart < 1:
		   raise Exception("part of date out of range")
	   
		# do more precise dayPart checking
		if (monthPart <= 7):
			if (monthPart % 2 == 0):
				maxDaysInMonth = 30
			else:
				maxDaysInMonth = 31
		else: 
			if (monthPart % 2 == 0):
				maxDaysInMonth = 31
			else:
				maxDaysInMonth = 30
	
		if (monthPart == 2):
			maxDaysInMonth = 28
	
			if (yearPart % 4 == 0):
				maxDaysInMonth = 29
				if (yearPart % 100 == 0) and (yearPart % 400 != 0):
					maxDaysInMonth = 28
				
		# if we made it this far only 1 more check for validity
		if dayPart <= maxDaysInMonth:
			bValid = True
		
	except: 
		bValid = False

	return bValid

def countDaysToDate(rawDate):
	print("countDaysToDate not yet implemented")

rawDate = input("Enter Date mm/dd/yyyy: ")
if (isDateValid(rawDate)):
	countDaysToDate(rawDate)
else:
	print("Unable to interpret date provided.")
	