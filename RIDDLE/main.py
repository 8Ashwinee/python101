"""
Riddle Game
-----------
A friendly, terminal-based riddle game
"""

import difflib
import random
import string

MAX_ATTEMPTS = 3

# Each riddle has the question a list of accepted answers and a hint.
RIDDLES = [
    {
        "question": "I have cities but no houses, forests but no trees, "
                    "and water but no fish. What am I?",
        "answers": ["map", "a map"],
        "hint": "You might unfold me on a road trip, or open me on your phone.",
    },
    {
        "question": "I am always hungry and must always be fed. "
                    "The finger I touch will soon turn red. What am I?",
        "answers": ["fire", "flame"],
        "hint": "Careful, I'm hot, and I love wood.",
    },
    {
        "question": "What has a heart that doesn't beat?",
        "answers": ["artichoke", "an artichoke"],
        "hint": "You can find me in the vegetable aisle.",
    },
    {
        "question": "What is so fragile that saying its name breaks it?",
        "answers": ["silence"],
        "hint": "Shhh... the moment you speak, I'm gone.",
    },
    {
        "question": "I speak without a mouth and hear without ears. "
                    "I have no body, but I come alive with wind. What am I?",
        "answers": ["echo", "an echo"],
        "hint": "Shout in a canyon and I'll answer you.",
    },
    {
        "question": "The more of me you take, the more you leave behind. "
                    "What am I?",
        "answers": ["footsteps", "steps", "footprints"],
        "hint": "Think of a walk along a sandy beach.",
    },
    {
        "question": "What has keys but can't open locks, "
                    "and has space but no room?",
        "answers": ["keyboard", "a keyboard", "computer keyboard"],
        "hint": "You're probably using one right now.",
    },
    {
        "question": "What gets wetter the more it dries?",
        "answers": ["towel", "a towel"],
        "hint": "You'll find me in the bathroom.",
    },
    {
        "question": "What can travel around the world while staying "
                    "in the same corner?",
        "answers": ["stamp", "a stamp", "postage stamp"],
        "hint": "I'm stuck on the top corner of an envelope.",
    },
    {
        "question": "I have hands but I can't clap. What am I?",
        "answers": ["clock", "a clock", "watch", "a watch"],
        "hint": "I tell you something every minute.",
    },
]

ARTICLES = ("a ", "an ", "the ")


def normalize(text):
    """Lowercase, strip punctuation and extra spaces, drop a leading article."""
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    for article in ARTICLES:
        if text.startswith(article):
            text = text[len(article):]
            break
    return text


def is_correct(guess, answers):
    """True if the guess matches any accepted answer (typos allowed)."""
    guess = normalize(guess)
    if not guess:
        return False
    for answer in answers:
        answer = normalize(answer)
        if guess == answer:
            return True
        # Be lenient about small typos but only for longer words
        # so short answers like "map" can't be matched by accident
        if len(answer) >= 5 and difflib.SequenceMatcher(None, guess, answer).ratio() >= 0.85:
            return True
    return False


def ask_riddle(number, total, riddle):
    """
    Ask one riddle. Returns (points_earned, action)
    where action is 'next' or 'quit'.
    """
    print(f"\nRiddle {number} of {total}")
    print("-" * 40)
    print(riddle["question"])
    print("(Type 'hint' for a clue, 'skip' to move on, or 'quit' to stop.)")

    wrong_guesses = 0
    hint_used = False

    while wrong_guesses < MAX_ATTEMPTS:
        attempts_left = MAX_ATTEMPTS - wrong_guesses
        reply = input(f"Your answer ({attempts_left} attempt{'s' if attempts_left != 1 else ''} left): ").strip()
        command = reply.lower()

        if command == "quit":
            return 0, "quit"

        if command == "skip":
            print(f"No problem! The answer was: {riddle['answers'][0].title()}")
            return 0, "next"

        if command == "hint":
            if hint_used:
                print(f"Hint (again): {riddle['hint']}")
            else:
                hint_used = True
                print(f"Hint: {riddle['hint']}  (this will cost you 1 point)")
            continue

        if is_correct(reply, riddle["answers"]):
            points = max(1, MAX_ATTEMPTS - wrong_guesses - (1 if hint_used else 0))
            praise = random.choice(["Correct!", "Nice one!", "You got it!", "Brilliant!"])
            print(f"{praise} +{points} point{'s' if points != 1 else ''}")
            return points, "next"

        wrong_guesses += 1
        if wrong_guesses < MAX_ATTEMPTS:
            print(random.choice(["Not quite, try again!", "Close, but no.", "Hmm, nope. Give it another go."]))

    print(f"Out of attempts! The answer was: {riddle['answers'][0].title()}")
    return 0, "next"


def rating_for(score, max_score):
    """Return a fun rating based on the percentage scored."""
    if max_score == 0:
        return "Riddle rookie"
    percent = score / max_score
    if percent == 1:
        return "Riddle master! Flawless."
    if percent >= 0.7:
        return "Sharp thinker!"
    if percent >= 0.4:
        return "Not bad at all. Keep at it!"
    return "Good effort. Time for round two?"


def play_round(num_riddles=5):
    """Play one full round and return the (score, max_score)."""
    chosen = random.sample(RIDDLES, k=min(num_riddles, len(RIDDLES)))
    score = 0
    answered = 0

    for number, riddle in enumerate(chosen, start=1):
        points, action = ask_riddle(number, len(chosen), riddle)
        score += points
        answered += 1
        if action == "quit":
            print("\nLeaving early, no worries!")
            break

    max_score = answered * MAX_ATTEMPTS
    print("\n" + "=" * 40)
    print(f"Game over! You scored {score} out of {max_score}.")
    print(rating_for(score, max_score))
    print("=" * 40)
    return score


def main():
    print("=" * 40)
    print("      Welcome to the Riddle Game!")
    print("=" * 40)
    name = input("What's your name? ").strip() or "Player"
    print(f"\nHi {name}! Solve each riddle in up to {MAX_ATTEMPTS} tries.")
    print("Faster answers earn more points (3 for first try).")

    best = 0
    try:
        while True:
            score = play_round()
            best = max(best, score)
            print(f"Your best score this session: {best}")

            again = input("\nPlay again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                break
    except (KeyboardInterrupt, EOFError):
        print()

    print(f"\nThanks for playing, {name}! See you next time.")


if __name__ == "__main__":
    main()
