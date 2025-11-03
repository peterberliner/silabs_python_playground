class Register:
    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"register({self.name}={self.value})"
    
    def increment(self):
        self.value += 1
    
    def half(self):
        self.value = int(self.value / 2)
    
    def triple(self):
        self.value = int(self.value * 3)