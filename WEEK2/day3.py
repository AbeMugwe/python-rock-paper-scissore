import re

# email='abemwangi17@hotmail.com'

# #^ Start of string
# pattern= r'^(?:[a-z 0-9])+@+(?:gmail|yahoo|hotmail|outlook)+\.(?:com|net|org)'

# #print(re.search(pattern,email))
# print(re.findall(pattern,email))

# phone_number='305 555-1234'

# number_pattern=r'^[0-9]{3}\ +[0-9]{3}+\-+[0-9]{4}'


# if re.match(number_pattern,phone_number):
#     print('Valid Dawg')
# else:
#     print('Invalid Dawg')


shows='I have watched these shows Ted Lasso, Snowfall, One piece, Frieren using these emails abemwangi17@gmail.com and bobbyfelix@outlook.org'
emails_pattern=r'\b[A-Za-z0-9]+@+(?:gmail|outlook)\.(?:com|org)'

print(re.findall(shows_pattern,shows))