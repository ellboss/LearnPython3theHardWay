# defines how many types of people there are.
types_of_people = 10
# sets x to state that There are 10 types of people using the definition above.
x = f"There are {types_of_people} types of people."

# defines binary and do_not
binary = "binary"
do_not = "don't"
# sets x to make a statement using definitions above.
y = f"Those who know {binary} and those who {do_not}."
# print x and y
print(x)
print(y)
# print x and y within a sentence.
print(f"I said: {x}")
print(f"I also said: '{y}'")
# define hiliarious and joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# print joke_evaluation, and include hilarious string within its string.
print(joke_evaluation.format(hilarious))
# define w and 3
w = "This is the left side of..."
e = "a string with a right side."
# print w and e
print(w + e)
