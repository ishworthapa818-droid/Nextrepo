#Random password generator (list comprehension)
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])

print("your random pasword is", password)