import random
import os


def random_meme():
    memes = os.listdir("assets/")
    choice = random.choice(memes)
    return f"assets/{choice}"


def spongify(s):
    return "".join([s[i].upper() if i % 2 else s[i].lower() for i in range(len(s))])


def get_reacts(message) -> list[str]:
    TIME_CARD_REACTS = {
        "bot": "🤖",
        "timecard": "📝",
        "sign": "✍️",
        "errors": "⚠️",
        "helpdesk": "🤯",
        "holiday": "🌴",
        "never": "🙃",
        "jimmy": "👨‍💼",
        "charge codes": "💳",
        "PTO": "🏖️",
        "payroll": "💰",
        "email": "📧",
        "week": "📅",
        "today": "📅",
        "check": "✅",
        "hours": "🕰️",
        "ASAP": "🏃",
    }
    reactions = []
    for keyword, emoji in TIME_CARD_REACTS.items():
        if keyword in message:
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
