# open text file and write a javascript program
file = open('program1.js', 'w')
def fw(statement):
    file.write(statement + '\n')

fw('// js program written by python program')
fw('window.onload = () => {')
fw('let title = document.createElement("h1");')
fw('let titleText = document.createTextNode("Title 1");')
fw('title.appendChild(titleText);')
fw('document.body.appendChild(title);')
fw('}')
file.close()

v
