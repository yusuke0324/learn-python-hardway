my_name = 'Yusuke Takeuchi'
my_age = 27
my_height = 170 #cm
my_weight = 57 #kg
my_eye = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d centi-meters" % my_height
print "He's %d kg heavy" % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eye, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
