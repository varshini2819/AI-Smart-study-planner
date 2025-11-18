class PlannerAgent:
    def __init__(self, session, memory):
        self.session = session
        self.memory = memory

    def generate_study_plan(self, syllabus_text):
        topics = [t.strip() for t in syllabus_text.split(',')]
        plan = {
            "total_topics": len(topics),
            "weekly_schedule": {
                f"Day {i+1}": topics[i] if i < len(topics) else None
                for i in range(len(topics))
            }
        }
        self.session.log("PlannerAgent", "Plan created")
        return plan
