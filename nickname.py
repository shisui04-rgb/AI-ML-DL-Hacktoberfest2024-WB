import random

# Predefined lists of adjectives and nouns
adjectives = ["Awesome", "Cool", "Funny", "Happy", "Lazy", "Silly", "Smart", "Tall", "Tiny"]
nouns = ["Bear", "Cat", "Dog", "Dragon", "Elephant", "Fish", "Fox", "Giraffe", "Horse"]

def generate_nickname():
    """Generate a random nickname."""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = f"{adjective} {noun}"
    return nickname

print("Random Nickname Generator")
print("Here is your random nickname:")
print(generate_nickname())
