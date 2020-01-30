import re
import math

kanjiJSON = open('kanji.json', 'w+')

startingJSON = [
    '{',
    '\t"kanji": {',
    '\t\t"n5": ['
]

s = 0
while s < 3:
    kanjiJSON.write(startingJSON[s] + '\n')
    s += 1


n5Kanji = open('n5Kanji.js', 'r')
n5Read = n5Kanji.read()
n5Range = range(1, 81)

# got examples
for n in n5Range:
    pattern1 = 'KanjiBox\(.+ ' + 'n5ex' + str(n)
    check = re.search(pattern1, n5Read)
    if check is not None:
        found = check.group()
        foundClean = found.replace(', n5ex' + str(n), '').replace('KanjiBox(', '[').replace("'", '"')
        print(foundClean)
        toJSON = [
            '\t\t\t{\n',
            '\t\t\t\t"kanji": ' + foundClean + '],\n'
        ]
        kanjiJSON.write(toJSON[0])
        kanjiJSON.write(toJSON[1])


    pattern2 = 'n5ex' + str(n) + ' = \[(()\n(.+))+\]'
    check2 = re.search(pattern2, n5Read)
    if check2 is not None:
        found2 = check2.group()
        found2Clean = found2.replace('n5ex' + str(n) + ' = [', '').replace("'", '"').replace('[', '\t\t\t\t[')
        toJSON2 = [
            '\t\t\t\t"examples": [',
            found2Clean,
            '\n\t\t\t\t]\n',
            '\t\t\t},\n'
        ]
        kanjiJSON.write(toJSON2[0])
        kanjiJSON.write(toJSON2[1])
        kanjiJSON.write(toJSON2[2])
        kanjiJSON.write(toJSON2[3])


endingJSON = [
    '\t\t],',
    '\t}',
    '}'
]

e = 0
while e < 3:
    kanjiJSON.write(endingJSON[e] + '\n')
    e += 1
