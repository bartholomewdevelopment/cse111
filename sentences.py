import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on tense and quantity."""
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

def make_sentence(quantity, tense):
    """Build and return a sentence."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    
    sentence = f"{determiner} {noun} {verb}."
    return sentence.capitalize()

def main():
    # Generate six sentences with different quantities and tenses
    print(make_sentence(1, "past"))    # single, past
    print(make_sentence(1, "present")) # single, present
    print(make_sentence(1, "future"))  # single, future
    print(make_sentence(2, "past"))    # plural, past
    print(make_sentence(2, "present")) # plural, present
    print(make_sentence(2, "future"))  # plural, future

if __name__ == "__main__":
    main()
