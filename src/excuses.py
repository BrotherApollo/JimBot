import random

subjects = [
    "I", "My dog", "My alarm", "The internet", "My computer", "My coffee machine"
]

verbs = [
    "ate", "deleted", "blocked", "misplaced", "forgot", "refused"
]

objects = [
    "my timecard", "the VPN connection", "my access credentials", "the report", "the reminder email"
]

modifiers = [
    "because Mercury is in retrograde.",
    "and I couldn't stop crying.",
    "while I was trying to meditate.",
    "and then the Wi-Fi exploded.",
    "and I was trapped in a parallel universe."
]

def generate_excuse():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(modifiers)}"


# for i in range(100):
#     print(generate_excuse())