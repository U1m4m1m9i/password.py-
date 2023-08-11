#random password generator
import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lowercase + uppercase + numbers + symbols
length = 16
password ="".join(random.sample(string,length))

print("your password is:" + password)