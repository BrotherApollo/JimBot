import random
import os


def random_meme():
    memes = os.listdir("assets/memes")
    choice = random.choice(memes)
    return f"assets/{choice}"


def spongify(s):
    return "".join([s[i].upper() if i % 2 else s[i].lower() for i in range(len(s))])


def get_reacts(message) -> list[str]:
    TIME_CARD_REACTS = {
        "🤖": ["bot"],
        "📝": ["timecard"],
        "✍️": ["sign"],
        "⚠️": ["error"],
        "🤯": ["helpdesk"],
        "🌴": ["holiday", "pto", "time off"],
        "🙃": ["never"],
        "👨‍💼": ["jimmy"],
        "💳": ["charge codes", "chargecode"],
        "💰": ["payroll", "expense"],
        "📧": ["email"],
        "📅": ["week", "today"],
        "✅": ["check", "checked"],
        "🕰️": ["hours"],
        "🏃": ["asap", "soon"],
        "🦞": ["lobster", "lucid", " ll "],
    }

    reactions = []
    for emoji, keywords in TIME_CARD_REACTS.items():
        if any(trigger in message for trigger in keywords):
            reactions.append(emoji)

    return reactions


def generate_excuse():
    subjects = [
        "I",
        "My dog",
        "My alarm",
        "The internet",
        "My computer",
        "My coffee machine",
    ]

    verbs = ["ate", "deleted", "blocked", "misplaced", "forgot", "refused"]

    objects = [
        "my timecard",
        "the VPN connection",
        "my access credentials",
        "the report",
        "the reminder email",
    ]

    modifiers = [
        "because Mercury is in retrograde.",
        "and I couldn't stop crying.",
        "while I was trying to meditate.",
        "and then the Wi-Fi exploded.",
        "and I was trapped in a parallel universe.",
        "and I reported it as phishing.",
    ]
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(modifiers)}"
