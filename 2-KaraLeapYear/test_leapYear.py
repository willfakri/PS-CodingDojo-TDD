
def isLeapYear(year):
	return year % 4 == 0;

def test_simple_leapYear():
	assert isLeapYear(1996)
	
def test_simple_not_leapYear():
	assert not isLeapYear(2001)