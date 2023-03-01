"""Word Finder: finds random words from a dictionary."""

import os, random


class WordFinder:
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'r')
        self.file_size = os.stat(path).st_size

    def get_random_line(self):
        random_line = random.randint(0, self.file_size)
        self.file.seek(random_line)
        self.file.readline()
        line = str(self.file.readline())
        return line
        

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)


    def get_random_special(self):
        line = list(self.get_random_line()) + [' ']
        print(line)

        while line[0] in '#\n ':
            line = list(self.get_random_line()) + [' ']

        line = ''.join(line)
        line = line.strip()
        line.replace('\n', '')

        return line
        
    
        
        
       
        
