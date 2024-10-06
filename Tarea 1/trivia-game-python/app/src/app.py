def run_quiz():
    print("===================================")
    print("********Juego de Trivia***********")
    print("===================================")
    print("Escoge la opción correcta.\n")

    quiz = Quiz()
    # Aquí cargarías las preguntas

    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(f"\nPregunta {quiz.current_question_index + 1}:")
            print(question.description)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta (número de opción): ")
            if quiz.answer_question(question, answer):
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta correcta era: {question.correct_answer}")
        else:
            break

    print(f"\nJuego terminado.")
    # Se agrearon las preguntas y sus respectivas respuestas
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
