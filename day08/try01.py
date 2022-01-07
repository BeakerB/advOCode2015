a = "\x27"

print(a)

escaped = a.translate(str.maketrans({'"':  r'\"', "\\": r"\\", "@":  r"\x"}))

print(escaped)
