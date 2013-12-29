import StringIO
import csv
import fileinput
import sys

from phpserialize import unserialize

errors = 0
# I'm not proud of this code, but it works.
for line in fileinput.input():
    whole = line[1:-2]
    whole = whole.replace('\\', '')
    f = StringIO.StringIO()
    f.write(whole)
    f.seek(0)
    reader = csv.reader(f, delimiter=',', quotechar="'")
    try:
        row = reader.next()
    except:
        errors += 1
        continue
    filename = row[0]
    serialized = row[4]
    try:
        info = unserialize(serialized)
    except:
        errors += 1
        continue
    if info['frameCount'] > 1:
        print filename

sys.stderr.write("Errors: {}\n".format(errors))
