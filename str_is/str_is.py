tw = {}

tw["letter"] = 'a'
tw["digit"] = '1'
tw["alphanum"] = 'a1'
tw["numalpha"] = '1a'
tw["decimal_en"] = '123.45'
tw["decimal_es"] = '123,45'
tw["word"] = 'word'
tw["composed-word"] = "composed-word"
tw["concatenated_word"] = "concatenated_word"
tw["apostrophe-word"] = "O'hara"


for k in tw:
    kind = []
    if tw[k].isalnum():
        kind.append('isalnum')

    if tw[k].isalpha():
        kind.append('isalpha')
        
    if tw[k].isdecimal():
        kind.append('isdecimal')
        
    if tw[k].isdigit():
        kind.append('isdigit')
        
    if tw[k].isidentifier():
        kind.append('isidentifier')
        
    if tw[k].isnumeric():
        kind.append('isnumeric')
        

    print(f"{k:20}: {f"'{tw[k]}'":24} is {kind}")