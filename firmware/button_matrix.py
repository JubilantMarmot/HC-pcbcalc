from machine import Pin
import time

class ButtonMatrix:
    def __init__(self, row_pins, col_pins):
        self.rows = [Pin(pin, Pin.OUT) for pin in row_pins]
        self.cols = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in col_pins]
        
    def scan(self):
        matrix = [[0 for _ in range(len(self.cols))] for _ in range(len(self.rows))]
        
        for row_index, row_pin in enumerate(self.rows):
            row_pin.value(0)
            time.sleep(0.01)
            
            for col_index, col_pin in enumerate(self.cols):
                if not col_pin.value():
                    matrix[row_index][col_index] = 1
                else:
                    matrix[row_index][col_index] = 0
                    
            row_pin.value(1)
        
        return matrix
