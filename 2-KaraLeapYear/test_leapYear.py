
def isLeapYear(year):
	return year % 4 == 0;

def test_simple_leapYear():
	assert isLeapYear(1996)