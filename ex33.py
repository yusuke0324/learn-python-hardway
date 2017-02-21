
def add_numbers(max, step):
    i = 0
    numbers = []

    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

def add_numbers_for(max, step):
    numbers =[]
    for i in range(0, max, step):
        numbers.append(i)

    print "The numbers: "
    for num in numbers:
        print num


add_numbers(10, 2)
add_numbers_for(10, 2)