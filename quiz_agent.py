class QuizAgent:
    def __init__(self, session, memory):
        self.session = session
        self.memory = memory

    def generate_quiz(self, plan):
        topics = plan["weekly_schedule"].values()
        quiz = [f"What is {t}?" for t in topics if t]
        self.session.log("QuizAgent", "Quiz generated")
        return quiz

    def evaluate_answers(self, answers):
        # Simple evaluation placeholder
        score = len(answers.split()) % 5  
        feedback = "Good, but revise complex topics."
        self.session.log("QuizAgent", "Answers evaluated")
        return score, feedback
