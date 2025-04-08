# Madlibs - word game; create story by filling blanks with random words

template = "The {adjective} {noun} {verb} over the lazy {animal}."

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
animal = input("Enter an animal: ")

mad_lib = template.format(adjective=adjective, noun=noun, verb=verb, animal=animal)

print(mad_lib)
