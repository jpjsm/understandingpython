#Counting the number of chars in an input string
textvalue = ''
while(len(textvalue)==0):
    textvalue = raw_input('Type some text: ')
print "'>{0}<'input text has {1} chars.".format(textvalue, len(textvalue))