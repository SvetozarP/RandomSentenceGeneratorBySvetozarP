import random


def get_random_word(words):
    return random.choice(words)


names: list = ["Peter", "Michel", "Johnny", "Michael", "John", "Gosho", "Sarah", "Pesho", "Mary", "Sarah",
               "Michelle", "Steve", "Stephen"]
places: list = ["Sofia", "Plovdiv", "Varna", "Burgas", "Stara Zagora", "Ruse", "Shumen", "Lovech"]
verbs: list = ["eats", "holds", "sees", "plays with", "brings"]
nouns: list = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs: list = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details: list = ["near the river", "at home", "at the park", "near the sea", "in the forest", "in the mountain"]

print("Welcome to the word generator! Here is your first sentence:")

while True:

    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}.")
    u_input = input("Press [Enter] to generate a new one or [q] to quit:")
    if u_input == "q":
        break
