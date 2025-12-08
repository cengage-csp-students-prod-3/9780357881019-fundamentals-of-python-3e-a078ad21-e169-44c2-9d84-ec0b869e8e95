import random

class Doctor:
    """Represents a simple doctor model."""

    def __init__(self):
        self.responses = [
            "You seem to think that {0}?",
            "And what do you think about this?",
            "Did I just hear you say that {0}?",
            "Why do you believe that {0}?",
            "I would like to hear more about that.",
            "Go on."
        ]

    # Task 1: greeting method
    def greeting(self):
        return "Hello, how can I help you today?"

    # Task 2: farewell method
    def farewell(self):
        return "Have a nice day!"

    # Random reply method
    def reply(self, patient_input):
        # Eğer hasta 'Yes', 'Correct', gibi kısa cevaplar verirse direkt random seç
        if patient_input.strip().lower() in ["yes", "correct", "no"]:
            return random.choice(self.responses)
        # Yoksa {0} ile hastanın cümlesini ekleyerek yanıt
        response = random.choice(self.responses)
        if "{0}" in response:
            response = response.format(patient_input)
        return response


def main():
    doc = Doctor()
    print(doc.greeting())

    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print(doc.farewell())
            break
        print(doc.reply(user_input))


if __name__ == "__main__":
    main()
