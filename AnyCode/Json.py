import json

x = {"we":24, "as":12, "sd":333}

print(x)

jd = json.dumps(x, indent=2)

del(x)

ljd = json.loads(jd)
print(type(ljd))
print(ljd)

x = ljd

print(x)
