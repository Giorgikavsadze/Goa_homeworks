# Use filter() to remove all None values from a list.

Nonein = list(filter(lambda name: name is not None, ["Ioane", None, "Beqa", None, "Nikolozi"]))

print(Nonein)