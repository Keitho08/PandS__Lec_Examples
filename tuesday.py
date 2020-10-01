# If statements review
# Keith Brazill

import datetime

today = datetime.datetime.today()
dayofweek = today.weekday() # day of week in number 0-6 

print("Lets check if its Tuesday")

if dayofweek == 1:        #== comparison operator , : here is what to do if condition is through(code on next line)
    print("It's Tuesday!")
elif dayofweek == 0:
    print("Its not Tuesday")
    print("Luckily it will be Tuesday tomorrow")

else:
    print("Unfortunately its not Tuesday")

print("Thanks for checking if its Tuesday")
