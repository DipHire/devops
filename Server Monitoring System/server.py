class Server:
    def __init__(self, name, cpu, memory):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.status = self.is_healthy()

    def update_usage(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory
        self.status = self.is_healthy()
        self.log_status()

    def is_healthy(self):
        return self.cpu < 80 and self.memory < 75

    def summary(self):
        health = "HEALTHY" if self.status else "UNHEALTHY"
        output = f"Server: {self.name} CPU: {self.cpu} | MEM: {self.memory} | {health}"
        print(output)
        return output

    def log_status(self):
        with open("server_report.txt", "a") as file:
            file.write(self.summary() + "\n")


server1 = Server("app-server", 45, 60)
server2 = Server("db-server", 92, 81)

server1.log_status()
server2.log_status()
