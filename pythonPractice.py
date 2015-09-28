
print "Hello World!"

print "I could have code like this."

print "This will run."

#####################################
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4


print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2

print "Is it greater?", 5 > -4
print "Is it greater or equal?", 5 >= -4
print "Is it less or equal?", 5 <= -4

#######################################
cars = 100
print "There are" ,cars, "cars in total"

print "You have %s cars" %cars

#######################################
my_eyes = 'Blue'
my_hair = 'Brown'

print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

######################################
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()

print "You are %s years old and %s tall" %(age,height)

#######################################
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

print_two(4,"Cars")

###################################
def filereadfunc(filename):
    print filename.read()

file = open("/home/leeladhar/Desktop/demfile.txt")

filereadfunc(file)

######################################
people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

####################################

count = [1, 2, 3, 4, 5]
fruits = ['apples', 'pears', 'apricots']

# this first kind of for-loop goes through a list
for number in count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#####################################

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print stuff['name']
print stuff['age']
