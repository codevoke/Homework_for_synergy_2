def smart_split(line):
    _k = False
    _k_char = ""
    _otv = []
    _item = ""
    for char in line:
        if char in ["\"", "'", "`"]:
            if not(_k):
                _k = True
                _k_char = char
                _item += "\""
            else:
                if char == _k_char:
                    _k = False
                    _item += "\""
        elif char == " " and not(_k):
            _otv.append(_item)
            _item = ""
        else:
            _item += char
    _otv.append(_item)
        
    return _otv

syntax_dict = {
    "string": "<string>",
    "int": "<int>",
    "=": "<operator '='>",
    "+": "<operator '+'>",
    "-": "<operator '-'>",
    "*": "<operator '*'>",
    "/": "<operator '/'>",
    "true": "<bool 'True'>",
    "false": "<bool 'False'>"
}

def analizator(token):
    if token.startswith("\"") and token.endswith("\""):
        token = "string"
    elif not [x for x in token if x not in [range(10)]]:
        token = "int"
    elif not [x for x in token if x not in [range(10), '.']]:
        token = "float"
    if token in ["True", "true"]:
        token = "true"
    if token in ["False", "false"]:
        token = "false"
    if syntax_dict.get(token):
        return syntax_dict[token]
    else:
        return "<undefined>"
    
testcase = [
"int a = 5",
"bool b = False",
"""string c = 'test "BTN" '"""
]
print(testcase)
for _ in testcase:
    l = smart_split(_)
    for __ in l:
        print(analizator(__), end=" ")
    print()