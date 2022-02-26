# JSON - JavaScriptobjectNotation

import json

x = '{"name": "Ion", "age": "30", "city": "Iasi"}'
y = json.loads(x)
print(y, type(y))

z = json.dumps(y)
print(json.dumps(z))
# a = json.dumps(["mere", "pere"])
# a = 42
a = 31.75
# a = True
print(json.dumps(a), type(a))
