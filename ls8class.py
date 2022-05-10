class GenericQuestion:

    def __init__(self, text, author, difficulty, answer, theme, user_answer="", is_asked=False,):
        self.text = text
        self.author = author
        self.difficulty = difficulty
        self.answer = answer
        self.theme = theme
        self.user_answer = user_answer
        self.score = difficulty * 10
        self.is_asked = is_asked


class Question(GenericQuestion):

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer in self.answer

    def build_question(self):
        return f"Тема: {self.theme}, Сложность: {self.difficulty}\n {self.text}"