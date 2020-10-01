# while loop review
# greatest common diviser (for 50 and 20 this is 10, highest number that divide both numbers)
# keep looping until number is found

a = 50
b = 20

while b > 0:
    a, b, = b, a % b # old values = new values of variables
    #tmp = a ,alternative method other languages
    #a = b
    # b = tmp % b
print(a)