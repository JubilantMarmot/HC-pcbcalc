class Calculator:
    def __init__(self):
        self.expression = ""
    
    def update(self, key):
        if key == 'C':
            self.expression = ""
        elif key == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += key
    
    def get_display(self):
        return self.expression
