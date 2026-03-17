
import datetime

class AgentLogger:
    def __init__(self):
        self.logs = []

    def log(self, agent, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] [{agent}] {message}"
        self.logs.append(entry)

    def save(self, path="output/log.txt"):
        import os
        os.makedirs("output", exist_ok=True)
        with open(path, "w") as f:
            f.write("\n".join(self.logs))

    def get_logs(self):
        return "\n".join(self.logs)
