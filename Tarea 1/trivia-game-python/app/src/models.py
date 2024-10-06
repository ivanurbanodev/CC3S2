class Question:
    def __init__(self, description, options, correct_answer, difficulty):
        self.description = description  
        self.options = options  
        self.correct_answer = correct_answer  
        self.difficulty = difficulty  # Se agrega el atributo para poner el nivel de dificultad de la pregunta

    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []  
        self.current_question_index = 0  
        self.correct_answers = 0 
        self.incorrect_answers = 0  
        self.current_difficulty = "facil"  # Se coloca el nivel de difcultad como atributo y se inicializza como facil

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        # Filtra las preguntas que coinciden con la dificultad actual
        available_questions = []
        for question in self.questions:
            if question.difficulty == self.current_difficulty:
                available_questions.append(question)

        # Si hay preguntas disponibles, retorna la siguiente
        if self.current_question_index < len(available_questions):
            question = available_questions[self.current_question_index]
            self.current_question_index += 1  # Avanza al siguiente índice
            return question
        return None  # Si no hay más preguntas, retorna None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            # Cambia la dificultad tras 3 o 5 respuestas correctas
            if self.correct_answers % 3 == 0:
                self.current_difficulty = "medio"  # Sube a nivel "medio"
            if self.correct_answers % 5 == 0:
                self.current_difficulty = "dificil"  # Sube a nivel "difícil"
            return True
        else:
            self.incorrect_answers += 1 
            return False