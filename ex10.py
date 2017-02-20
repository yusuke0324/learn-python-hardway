tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* cat food
\t* Finishes%s
\t* Catnip\n\t* Grass
""" % tabby_cat
three_quotes = '''
Is something different?
  What is different?
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print three_quotes

