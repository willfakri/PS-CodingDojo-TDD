def isLeapYear(year):
	if(isDivisibleBy4(year)):		
		return True
	return isDivisibleBy400(year)
	
def isDivisibleBy4(year):
	return year % 4 == 0 and year % 100 != 0
	
def isDivisibleBy400(year):
	return year % 400 == 0


	
# # # TESTS # # #	
def test_simple_leapYear():
	assert isLeapYear(1996)
	
def test_simple_not_leapYear():
	assert not isLeapYear(2001)
	
def test_divisible_by_100():
	assert isLeapYear(2000)
	
def test_divisible_by_400():
	assert not isLeapYear(1900)