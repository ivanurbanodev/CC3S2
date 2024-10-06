import pytest
from src.models import Question, Quiz  

# Prueba para la clase Question
def test_question_is_correct():
    question = Question("¿Cuál es la capital de Francia?", ["Londres", "París", "Roma"], "París", "facil")
    
    # Verificar que la respuesta correcta es "París"
    assert question.is_correct("París") == True
    # Verificar que una respuesta incorrecta no es aceptada
    assert question.is_correct("Roma") == False

# Prueba para agregar preguntas al cuestionario
def test_add_question():
    quiz = Quiz()
    question = Question("¿Cuál es la capital de España?", ["Madrid", "Barcelona"], "Madrid", "facil")
    
    # Añadir la pregunta
    quiz.add_question(question)
    
    # Verificar que la pregunta fue añadida
    assert len(quiz.questions) == 1
    assert quiz.questions[0].description == "¿Cuál es la capital de España?"

# Prueba para obtener la siguiente pregunta basada en la dificultad
def test_get_next_question():
    quiz = Quiz()
    
    # Agregar dos preguntas con diferentes dificultades
    question1 = Question("Pregunta fácil", ["Opción 1", "Opción 2"], "Opción 1", "facil")
    question2 = Question("Pregunta difícil", ["Opción A", "Opción B"], "Opción A", "dificil")
    
    quiz.add_question(question1)
    quiz.add_question(question2)
    
    # Verificar que solo la pregunta fácil es obtenida en dificultad "facil"
    next_question = quiz.get_next_question()
    assert next_question.description == "Pregunta fácil"

# Prueba para responder preguntas y cambiar la dificultad
def test_answer_question_and_change_difficulty():
    quiz = Quiz()
    
    # Agregar tres preguntas fáciles y dos medianas
    question1 = Question("Pregunta 1", ["1", "2"], "1", "facil")
    question2 = Question("Pregunta 2", ["3", "4"], "3", "facil")
    question3 = Question("Pregunta 3", ["5", "6"], "5", "facil")
    
    question4 = Question("Pregunta 4", ["A", "B"], "A", "medio")
    question5 = Question("Pregunta 5", ["C", "D"], "C", "dificil")
    
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)
    quiz.add_question(question4)
    quiz.add_question(question5)

    # Responder correctamente las tres preguntas fáciles
    assert quiz.answer_question(question1, "1") == True
    assert quiz.answer_question(question2, "3") == True
    assert quiz.answer_question(question3, "5") == True
    
    # Verificar que la dificultad ha cambiado a "medio" después de 3 respuestas correctas
    assert quiz.current_difficulty == "medio"

    # Responder una pregunta más y verificar que la dificultad no ha cambiado a "dificil"
    assert quiz.answer_question(question4, "A") == True
    assert quiz.current_difficulty == "medio"  # Aún en nivel "medio"

    # Responder una quinta pregunta y verificar que la dificultad sube a "dificil"
    assert quiz.answer_question(question5, "C") == True
    assert quiz.current_difficulty == "dificil"  # Ahora en nivel "difícil"

# Prueba para verificar el conteo de respuestas incorrectas
def test_answer_question_incorrect():
    quiz = Quiz()
    question = Question("Pregunta incorrecta", ["1", "2"], "1", "facil")
    quiz.add_question(question)

    # Responder incorrectamente
    assert quiz.answer_question(question, "2") == False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1
