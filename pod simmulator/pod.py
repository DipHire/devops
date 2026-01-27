class Pod:
    def __init__(self, name):
        self.name = name
        self.status = "Pending"

    def start(self):
        if self.status == "Pending":
            self.status = "Running"
        self.show_status()

    def crash(self):
        if self.status == "Running":
            self.status = "CrashLoopBackOff"
        self.show_status()

    def restart(self):
        if self.status == "CrashLoopBackOff":
            print("Restarting pod…")
            self.status = "Running"
        self.show_status()

    def delete(self):
        self.status = "Terminated"
        self.show_status()

    def show_status(self):
        print(f"Pod: {self.name}    Status: {self.status}")


pod = Pod("auth-pod")

pod.start()
pod.crash()
pod.restart()
pod.delete()
