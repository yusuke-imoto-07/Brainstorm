import tkinter as tk
from Brainstorming import Brainstorming

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.brainstorming = Brainstorming()

        self.title("Brainstorming with OpenAI")
        self.geometry("1500x1500")

        # Left side
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=0, column=0, sticky="n")

        # Theme input
        self.theme_label = tk.Label(self.left_frame, text="Discussion Theme:")
        self.theme_label.pack()
        self.theme_entry = tk.Entry(self.left_frame)
        self.theme_entry.pack()

        # Role input
        self.roles_label = tk.Label(self.left_frame, text="Roles for OpenAI:")
        self.roles_label.pack()
        self.role_entries = [tk.Entry(self.left_frame) for _ in range(5)]
        for entry in self.role_entries:
            entry.pack()

        # Send button
        self.send_button = tk.Button(self.left_frame, text="Send", command=self.send)
        self.send_button.pack()

        # Clear button
        self.clear_button = tk.Button(self.left_frame, text="Clear", command=self.clear)
        self.clear_button.pack()

        # Clear History button
        self.clear_history_button = tk.Button(self.left_frame, text="Clear History", command=self.clear_history)
        self.clear_history_button.pack()

        # Right side
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=0, column=1, sticky="n")

        # Discussion history
        self.history_labels = [tk.Label(self.right_frame, text=f"Discussion History {i+1}:") for i in range(5)]
        self.history_texts = [tk.Text(self.right_frame, height=9) for _ in range(5)]
        for i in range(5):
            self.history_labels[i].pack()
            self.history_texts[i].pack()

        # Conclusion side
        self.conclusion_frame = tk.Frame(self)
        self.conclusion_frame.grid(row=0, column=2, sticky="n")

        # Conclusion
        self.conclusion_label = tk.Label(self.conclusion_frame, text="Conclusion:")
        self.conclusion_label.pack()
        self.conclusion_text = tk.Text(self.conclusion_frame)
        self.conclusion_text.pack()

    def send(self):
        theme = self.theme_entry.get()
        roles = [entry.get() for entry in self.role_entries]
        for i, role in enumerate(roles):
            if i == 0:
                content = f"あなたは{role}です。{theme}について独自の視点から斬新なアイデアを3つ提示、" \
                          f"それぞれの案のメリットと改善点を挙げてください。" \
                          f"口調は、ご自身の人格に沿った口調を再現してください。" \
                          f"アイデアを過剰描きした後に、それぞれのアイデアについて言及してください。" \
                          f"回答は1000文字以内に纏めてください。"
            elif i == len(roles) - 1:
                content = f"あなたは{role}です。提示されたアイデアについてメリットと改善点を評価した上で、" \
                          f"あなたの視点から、最終的に採用すべきと思うアイデアを一つ決定してください。また、その根拠を述べてください。" \
                          f"口調は、ご自身の人格に沿った口調を再現してください." \
                          f"回答は1000文字以内に纏めてください。"
            else:
                content = f"あなたは{role}です。これまでに出たアイデアについてメリットと改善点を評価した上で、" \
                          f"あなたの目線から採用すべき案を挙げてください。また、独自の視点から新たに独創的なアイデアを1つ提示してください。" \
                          f"また、そのアイデアのメリットと改善点を挙げてください。" \
                          f"口調は、ご自身の人格に沿った口調を再現してください" \
                          f"アイデアを過剰描きした後に、それぞれのアイデアについて言及してください。" \
                          f"回答は1000文字以内に纏めてください。"
            self.brainstorming.add_message("system", content)
            answer = self.brainstorming.brainstorm()
            self.brainstorming.add_message("assistant", answer)
            self.history_texts[i].insert(tk.END, f"{role}: {answer}\n")
        # Get the last answer as the conclusion
        self.conclusion_text.delete(1.0, tk.END)
        self.conclusion_text.insert(tk.END, answer)

    def clear(self):
        self.theme_entry.delete(0, tk.END)
        for entry in self.role_entries:
            entry.delete(0, tk.END)
        for text in self.history_texts:
            text.delete(1.0, tk.END)
        self.conclusion_text.delete(1.0, tk.END)
        self.brainstorming = Brainstorming()

    def clear_history(self):
        for text in self.history_texts:
            text.delete(1.0, tk.END)
        self.conclusion_text.delete(1.0, tk.END)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
