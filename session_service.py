class SessionService:
    def __init__(self):
        self.logs = []

    def log(self, agent, message):
        entry = f"[{agent}] {message}"
        self.logs.append(entry)
        print("🔍 LOG:", entry)
