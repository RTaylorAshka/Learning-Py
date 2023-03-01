"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    """class generates a serial number starting from specified number and increments by one with every generation."""

    

    def __init__(self, start):
        self.start = start
        self.current = start


    """first function returns a serial number and the second function iterates it by one for the next generation"""

    def generate(self):
        self.return_serial()
        self.iterate()
        
    
    """resets serial number to specified starting number"""

    def reset(self):
        self.current = self.start

    """iterates serial by one"""

    def iterate(self):
        self.current = self.current + 1

    """returns the serial number"""

    def return_serial(self):
        return self.current
