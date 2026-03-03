#Schreiben Sie eine Funktion histogram(strings) welche eine Liste von Zeichenketten als Parameter erwartet. Sie soll ein Dictionary zurückgeben, welches für jede auftretende Zeichenkette ihre Häufigkeit enthält. Beispiel: histogram(["foo", "bar", "check", "foo", "check", "door"]) führt zur Rückgabe des folgenden Dictionaries: {"foo": 2, "bar": 1, "check": 2, "door": 1}

def histogram(strings):
    hist = {}
    for string in strings:
        if string in hist:
            hist[string] += 1
        else:
            hist[string] = 1
    return hist

# Testfälle
print(histogram(["foo", "bar", "check", "foo", "check", "door"]))  # {"foo": 2, "bar": 1, "check": 2, "door": 1}
print(histogram([]))  # {}
print(histogram(["a", "b", "c", "a", "b", "c", "a"]))  # {"a": 3, "b": 2, "c": 2}
print(histogram(["hello", "world", "hello", "python"]))  # {"hello": 2, "world": 1, "python": 1}