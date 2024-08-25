import math

class Calculator:
    def __init__(self):
        self.stack = []
        self.functions = {
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'sqrt': lambda x: math.sqrt(x),
            'log': lambda x: math.log10(x),
            'exp': lambda x: math.exp(x)
        }

    def update(self, key):
        if key == 'C':
            self.stack = []
        elif key == '=':
            if self.stack:
                try:
                    result = self.stack[-1]
                    self.stack = [result]
                except Exception as e:
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
                except Exception as e:
                    self.stack = ["Error"]
        elif key in self.functions:
            if self.stack:
                value = self.stack.pop()
                try:
                    self.stack.append(self.functions[key](value))
                except Exception as e:
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
