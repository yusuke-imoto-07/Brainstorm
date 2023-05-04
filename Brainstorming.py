from api import get_answer

class Brainstorming:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def brainstorm(self):
        return get_answer(self.messages)
