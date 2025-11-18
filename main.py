from agents.planner_agent import PlannerAgent
from agents.quiz_agent import QuizAgent
from agents.insights_agent import InsightsAgent
from agents.memory_agent import MemoryAgent

from services.session_service import SessionService
from services.memory_bank import MemoryBank

print("🔥 Multi-Agent Smart Study Planner — Starting Up...")

session = SessionService()
memory = MemoryBank()

planner_agent = PlannerAgent(session, memory)
quiz_agent = QuizAgent(session, memory)
insights_agent = InsightsAgent(session, memory)
memory_agent = MemoryAgent(session, memory)

def run_system():
    syllabus = input("\n📘 Enter your syllabus topics (comma separated):\n→ ")

    # Step 1: Create initial study plan
    plan = planner_agent.generate_study_plan(syllabus)
    print("\n🗓 Initial Study Plan:\n", plan)

    # Step 2: Generate quiz
    quiz = quiz_agent.generate_quiz(plan)
    print("\n📝 Quiz Generated:\n", quiz)

    # Step 3: User answers
    answers = input("\n✏ Enter your quiz answers:\n→ ")
    score, feedback = quiz_agent.evaluate_answers(answers)
    print("\n📊 Feedback:", feedback)

    # Step 4: Save memory
    memory_agent.store_performance(score, feedback)

    # Step 5: Generate insights
    updated_plan = insights_agent.adjust_plan_based_on_performance(plan, feedback)
    print("\n🔁 Updated Study Plan:\n", updated_plan)


if __name__ == "__main__":
    run_system()
