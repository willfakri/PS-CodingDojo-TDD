
def isLeapYear(year):
	if(year % 4 == 0 and year % 100 != 0):
		return True
	return year % 400 == 0

##TESTS##
def test_simple_leapYear():
	assert isLeapYear(1996)
	
def test_simple_not_leapYear():
	assert not isLeapYear(2001)
	
def test_different_leapYear():
	assert isLeapYear(2000)
	
def test_different_not_leapYear():
	assert not isLeapYear(1900)