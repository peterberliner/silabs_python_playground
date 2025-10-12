from register import Register

class Command:
    def __init__(self, line: str):
        self.line = line
        parts = line.split()
        self.command_str = parts[0]
        self.args = parts[1:]

    def execute(self, reg_a: Register, reg_b: Register) -> int:
        if self.command_str == "hlf":    
            self.name = "half"
            self.reg = reg_a if self.args[0].strip() == 'a' else reg_b
            self.reg.half()
            return 1
        elif self.command_str == "tpl":
            self.name = "triple"
            self.reg = reg_a if self.args[0].strip() == 'a' else reg_b
            self.reg.triple()
            return 1
        elif self.command_str == "inc":
            self.name = "increment"
            self.reg = reg_a if self.args[0].strip() == 'a' else reg_b
            self.reg.increment()
            return 1
        elif self.command_str == "jmp":
            self.name = "jump"
            self.offset = self.args[0].strip()
            if self.offset[0] == '+':
                self.offset = self.offset[1:]
                self.offset = int(self.offset)
            else:
                self.offset = self.offset[1:]
                self.offset = int(self.offset) * -1              
            return self.offset
        elif self.command_str == "jie":
            self.name = "jump if even"
            self.reg = reg_a if 'a' in self.args[0] else reg_b
            offset = self.args[1].strip()
            if offset[0] == '+':
                offset = offset[1:]
                offset = int(offset)
            else:
                offset = offset[1:]
                offset = int(offset) * -1  
            if self.reg.value % 2 == 0:
                return offset
            else:
                return 1
        elif self.command_str == "jio":
            self.name = "jump if one"
            self.reg = reg_a if 'a' in self.args[0] else reg_b
            offset = self.args[1].strip()
            if offset[0] == '+':
                offset = offset[1:]
                offset = int(offset)
            else:
                offset = offset[1:]
                offset = int(offset) * -1  
            if self.reg.value == 1:
                return offset
            else:
                return 1
        raise ValueError(f"Unknown command: {self.command_str}")
