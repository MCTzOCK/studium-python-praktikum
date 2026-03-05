def tokenize(string):
    res = []
    current = ""
    for c in string:
        if c in "0123456789":
            current += c
        else:
            if current:
                res.append(int(current))
                current = ""
            if c in "-()":
                res.append(c)
                continue
            if c != " ":
                raise ValueError(f"Unexpected character: {c}")
    if current:
        res.append(int(current))
    return res
