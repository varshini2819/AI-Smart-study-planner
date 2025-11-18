class InsightsAgent:
    def __init__(self, session, memory):
        self.session = session
        self.memory = memory

    def adjust_plan_based_on_performance(self, plan, feedback):
        if "revise" in feedback.lower():
            plan["priority_adjusted"] = True
        self.session.log("InsightsAgent", "Plan updated")
        return plan
