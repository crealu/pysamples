from collections import OrderedDict
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

def pretty(p):
    pp.pprint(p)

oldStyle = open('cleanStyle.css', 'r')
oldStyleData = oldStyle.read()

ejs = open('index.ejs', 'r')
ejsLines = ejs.readlines()

classes_and_ids = []

tried_regex = [
    'id=".+"',
    'id="(.+)"',
    '(id=".+")',
    'id="(.+")',
    'id=(".+")',
    'id=(".+"\s)|id=(".+">)' # new/current
]

def cleanREMatch(id_string, troublePattern):
    troubleCheck = re.search(troublePattern, id_string)
    if troubleCheck is not None:
        trouble = troubleCheck.group()
        noTrouble = id_string.replace(str(trouble), '')
        return noTrouble

def readIds():
    for i in ejsLines:
        idPattern = 'id=(".+"\s)|id=(".+">)'
        idCheck = re.search(idPattern, i)
        if idCheck is not None:
            idConfirm = idCheck.group()
            idFilter = idConfirm.replace('id="', '').replace('"', '').replace(' ', '').replace('>', '')
            if 'class' in idFilter:
                idClean = cleanREMatch(idFilter, 'class=(.+)')
                classes_and_ids.append('#' + idClean)
            else:
                classes_and_ids.append('#' + idFilter)

    #pretty(classes_and_ids)
    #print(len(classes_and_ids))

#print('\n regex id results:\n')
readIds()

def separateClasses(class_string):
    if ' ' in class_string:
        classSplit = class_string.split(' ')
        for cn in classSplit:
            classes_and_ids.append('.' + cn)
    else:
        classes_and_ids.append('.' + class_string)

def readClasses():
    for j in ejsLines:
        classPattern = 'class=(".+"\s)|class=(".+">)'
        classCheck = re.search(classPattern, str(j))
        if classCheck is not None:
            classConfirm = classCheck.group()
            classFilter = classConfirm.replace('class="', '').replace('"', '').replace('>', '')
            if 'id=' in classFilter:
                classClean = cleanREMatch(classFilter, 'id=(.+)')
            else:
                classClean = classFilter

            separateClasses(classClean)

    #pretty(classes_and_ids)

#print('\n regex class results:\n')
readClasses()

def readJS():
    kanjiJSFile = open('kanji.js', 'r')
    kanjiJSlines = kanjiJSFile.readlines()
    classPattern = "'\w+'|'\w+-\w+'|'\w+-\w+-\w+'"

    kanjiJSClasses = []

    for kjsl in kanjiJSlines:
        if '.classList.add(' in kjsl:
            classMatch = re.search(classPattern, kjsl)
            if classMatch is not None:
                classes = '.' + classMatch.group().replace("'", "")
                kanjiJSClasses.append(classes)

    jsClassesToAdd = [
        '.cm-example-kanji',
        '.cm-example-reading',
        '.cm-example-english',
        '.kanji-p',
        '.onkun-p',
        '.onkun-p',
        '.collected-kanji',
        '.set-title-form',
        '.hidden-set-data',
        '.submit-set-form-btn',
        '.test-slide',
        '.kanji-wrapper',
        '.answer-wrapper',
        '.all-choices-wrapper',
        '.choice-wrapper',
        '.test-input',
        '#check-kanji-btn'
    ]

    return (kanjiJSClasses + jsClassesToAdd)

allJSClasses = readJS()
all_classes_and_ids = classes_and_ids + allJSClasses
#pretty(all_classes_and_ids)
#classes_and_ids_clean = list(set(classes_and_ids))
#pretty(classes_and_ids)

classes_and_ids_clean = list(OrderedDict.fromkeys(all_classes_and_ids))
pretty(classes_and_ids_clean)

pyStyle = open('pyStyle.css', 'w+')


# IT WORKS!
def readCheckWrite():
    for e in classes_and_ids_clean:
        elementPattern = e + ' {(\n\s+.+:.+;)+\n}'
        ch = re.search(elementPattern, oldStyleData)
        if ch is not None:
            keyPropStyle = ch.group()
            pyStyle.write(keyPropStyle + '\n\n')

readCheckWrite()
