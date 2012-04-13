# Write Python code that prints out the number of hours in 7 weeks.
# DO NOT USE IMPORT

print 7*7*24

##############################

# Write Python code that stores the distance in meters that light travels in one nanosecond in the variables, nanodistance.
# DO NOT USE IMPORT

speed_of_light = 299800000. #meters per second
nano_per_sec = 1000000000. #1 Billion


nano_distance = speed_of_light / nano_per_sec
print nano_distance

##############################

# Write Python code that prints out udacious without using any quote characters in your code.
s = 'udacity'
t = 'bodacious'

print s[:3] + t[4:]

##############################

# Write Python code that prints out the position of the first occurence of 'hoo' in the value of the text, or -1 if it does not occur at all.

text = 'first hoo'

print text.find('hoo')

##############################

# Write Python code that prints out the position of the second occurence of 'zip' in the value of the text, or -1 if it does not occur at least twice.

text = "all zip files are zipped"

first_position = text.find('zip')
print text.find('zip',first_position + 3)

##############################

# Write Python code that prints out the nearest whole number to x.
# x =3.14159 -> 3 (not 3.0)

x = 3.14159

print int(round(x))

##############################



