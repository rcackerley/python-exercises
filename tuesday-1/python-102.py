name = raw_input("What is your name? ")
print("Hello, %s" % name)
name_length = len(name)
big_name = name.upper()
print("%s is %s characters long" % (big_name, name_length))

name = raw_input("What is your name?")
favorite_food = raw_input("What is your favorite food?")
hobby = raw_input("What is your favorite hobby?")

print("%s likes to eat %s and enjoys %s" % (name, favorite_food, hobby))