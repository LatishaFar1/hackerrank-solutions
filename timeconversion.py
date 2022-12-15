# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


# Example

# s = '12:01:00PM'
# Return '12:01:00'.
# s = '12:01:00AM'
# Return '00:01:00'.

def timeConversion(s):
#grab the last two characters (PM or AM)
    lastTwo = s[-2:]
# if the last two chars is equal to PM AND the first two doesn't equal 12
    if lastTwo == "PM" and s[:2] != "12":
# add 12 to the first two chars (after making it into a num), then convert it back to a string
#  add PM to the end after making it a string.
        s = str(12 + int(s[:2])) + s[2:]
# if the last two chars is equal to AM AND the first two equals 12
    if lastTwo == "AM" and s[:2] == "12":
#put 00 at the beginning of the string and add the rest of the string
        s = "00" + s[2:]
    return s[:-2]