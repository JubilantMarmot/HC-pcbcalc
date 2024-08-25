class Calculator:
    def __init__(self):
        self.stack = []

    def update(self, key):
        if key == 'C':
            self.stack = []
        elif key == '=':
            if self.stack:
                try:
                    result = self.stack[-1]
                    self.stack = [result]
                except:
                    self.stack = ["Error"]
        elif key in '+-*/':
            if len(self.stack) >= 2:
                b = self.stack.pop()
                a = self.stack.pop()
                try:
                    if key == '+':
                        self.stack.append(a + b)
                    elif key == '-':
                        self.stack.append(a - b)
                    elif key == '*':
                        self.stack.append(a * b)
                    elif key == '/':
                        self.stack.append(a / b)
                except:
                    self.stack = ["Error"]
        else:
            try:
                number = float(key)
                self.stack.append(number)
            except ValueError:
                self.stack = ["Error"]

    def get_display(self):
        if self.stack:
            return str(self.stack[-1])
        return "0"