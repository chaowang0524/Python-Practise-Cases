import dateutil # convert a formatted timestamp in string back to time

time = dateutil.parser.parse("Aug 28 2015 12:00AM")
print(time)