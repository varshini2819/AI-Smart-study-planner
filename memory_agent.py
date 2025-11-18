class MemoryAgent:
    def __init__(self, session, memory):
        self.session = session
        self.memory = memory

    def store_performance(self, score, feedback):
        record = {
            "score": score,
            "feedback": feedback
        }
        self.memory.save(record)
        self.session.log("MemoryAgent", "Memory saved")
