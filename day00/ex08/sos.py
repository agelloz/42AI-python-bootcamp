import sys

morse = {
'A': '.- ',
'B': '-... ',
'C': '-.-. ',
'D': '-.. ',
'E': '. ',
'F': '..-. ',
'G': '--. ',
'H': '.... ',
'I': '.. ',
'J': '.--- ',
'K': '-.- ',
'L': '.-.. ',
'M': '-- ',
'N': '-. ',
'O': '--- ',
'P': '.--. ',
'Q': '--.- ',
'R': '.-. ',
'S': '... ',
'T': '- ',
'U': '..- ',
'V': '...- ',
'W': '.-- ',
'X': '-..- ',
'Y': '-.-- ',
'Z': '--.. ',
'0': '----- ',
'1': '.---- ',
'2': '..--- ',
'3': '...-- ',
'4': '....- ',
'5': '..... ',
'6': '-.... ',
'7': '--... ',
'8': '---.. ',
'9': '----. '}

for arg in sys.argv[1:]:
    for c in arg:
        if not c.isalnum() and c != ' ':
            print('ERROR')
            exit()
i = 0
for arg in sys.argv[1:]:
    i += 1
    if i > 1:
        sys.stdout.write(' / ')
    for c in arg:
        if c == ' ':
            sys.stdout.write(' / ')
        else:
            sys.stdout.write(morse[c.upper()])
sys.stdout.write('\n')
