#----------------------------------------------------------------------------------------------------------------------------------------------------------
import time
#----------------------------------------------------------------------------------------------------------------------------------------------------------

print(time.ctime(0))                                            # convert a time expressed in seconds since epoch (to a readable string)
#                                                                 epoch = a date and time from which a computer measures the system time
print(time.ctime(time.time()))                                  # will retun the current time
print(time.time())                                              # will return current seconds since epoch

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# time_object = time.gmtime()                                   # UTC time
# time_object = time.localtime()                                # local time
# time.strftime(format, time_object)                            # formats a time_object to a string
# time.strptime(strinng, format)                                # parse a string representing a time/date according to a format
# time.asctime(time)                                            # accepts a time_object or a tuple representation of a relative time 
# time.mktime(time)                                             # converts the given date/time into seconds since epoch

#----------------------------------------------------------------------------------------------------------------------------------------------------------

time_object = time.gmtime()                                     # UTC time
utc_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(utc_time) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------

time_object = time.localtime()                                  # local time
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)     # These directives are available on Python's Documentations at it's official website
print(local_time)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

time_string = "7 April, 2004"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# (year, month, day, hours, minutes, seconds, #day of the week, #day of the year, daylight saving time(dst))

time_tuple = (2022, 4, 7, 1, 25, 0, 5, 125, -1)
time_string = time.asctime(time_tuple)
print(time_string)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# (year, month, day, hours, minutes, seconds, #day of the week, #day of the year, daylight saving time(dst))

time_tuple = (2022, 4, 7, 1, 25, 0, 5, 125, -1)
time_string = time.mktime(time_tuple) # converts the given date/time into seconds since epoch
print(time_string)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# %B = Locale's full month name
# %d = Day of  the moonth as a deccimal number
# %Y = Year with century as a decimal number
# %H = Hour(24-hour-clock) as a decimal number
# %M = Minutes as a decimal number
# %S = Seconds as a decimal number
# colon ":" is used as to seperate hours,minutes and seconds 
# UTC  = Coordinated Universal Time