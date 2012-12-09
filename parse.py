#!/usr/bin/env python
# http://pypi.python.org/pypi/phpserialize
import sys
import csv
import StringIO

class LineReader:
    def __init__(self):
        self.line = ''
        self.seperator = "\n"
        self.window = []

    def add(self, character):
        self.window.append(character)
        self.line += character
        ###print "'%s'" % self.line
        if len(self.window) > len(self.seperator):
            self.window.pop(0)

    def found_line(self):
        if ''.join(self.window) == self.seperator:
            rv = self.line
            self.line = ''
            return rv
        else:
            return False

def process(row):
    if len(row) < 8:
        return False
    if not row[7] == "'image'":
        return False
    if not row[8] == "'gif'":
        return False
    # print [row[0],row[7],row[8]]
    # print row
    return True




reader = LineReader()
inside_insert = False
search = 'INSERT INTO `image` VALUES'
while True:
    c = sys.stdin.read(1)
    if not len(c) > 0:
        break
    reader.add(c)
    line = reader.found_line()
    if len(reader.line) > len(search) and reader.line.startswith(search):
        inside_insert = True
        reader.line = ''
        reader.seperator = '),'
    if not inside_insert:
        continue
    if not line:
        continue
    
    # strip out '(' at beginning and '),' at end
    string = line[1:-2]
    # print line[1:-2]
    string_array = string.split(',')
    rv = process(string_array)
    if rv == True:
        print line
    
