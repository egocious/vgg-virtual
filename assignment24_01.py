#Assignment 1
#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3 No. of Lower case Characters : 12

def capital_count(sentence):
    count = 0
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for char in sentence:
        if char in uppercase:
            count = count + 1
    print ("Question 1. Total number of upper case letter is: ") + str(count)

sentence = "The rain in Spain falls mainly on the Plain"
capital_count(sentence)

print "-" * 40

def small_count(words):
    count = 0
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    for char in words:
        if char in lowercase:
            count = count + 1
    print ("Question 1a. Total number of lower case letter is: ") + str(count)

words = "The rain in Spain falls mainly on the Plain"
small_count(words)

print "-" * 40

#Assignment 2
#Write a Python function to find the Max of three numbers

def maximun_nos():
    numbers = (14, 54, 78)
    result = max(numbers)
    print "Question 2. The maximum number is " + str(result)

maximun_nos()

#Assignment 3
#Write a Python function that takes a number as a parameter and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and #that has no positive divisors other than 1 and itself.

print "-" * 40

def prime_nos():
    number = int(raw_input("Enter any number >> "))
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print "Question 3. " + str(number) + " is not a prime number"
                break
        else:
            print "Question 3. " + str(number) + " is a prime number"
    else: 
        print "Question 3. This is not a prime number"

prime_nos()

