from machine import Pin
import time

rows = [Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT), Pin(10, Pin.OUT)]
cols = [Pin(11, Pin.IN, Pin.PULL_UP), Pin(12, Pin.IN, Pin.PULL_UP), Pin(13, Pin.IN, Pin.PULL_UP)]

def scan_matrix():
    matrix = [[0 for _ in range(len(cols))] for _ in range(len(rows))]
    
    for row_index, row_pin in enumerate(rows):
        row_pin.value(0)
        time.sleep(0.01)

        for col_index, col_pin in enumerate(cols):
            if not col_pin.value():
                matrix[row_index][col_index] = 1
            else:
                matrix[row_index][col_index] = 0

        row_pin.value(1)

    return matrix

def main():
    while True:
        matrix = scan_matrix()
        
        for row in matrix:
            print(' '.join(str(col) for col in row))
        
        print('---')
        time.sleep(0.1)

if __name__ == "__main__":
    main()
