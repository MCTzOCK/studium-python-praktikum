# Ändern Sie das Histogramm wie folgt. Statt einer Liste von Zeichenketten soll eine Liste von Listen von Zeichenketten verarbeitet werden. Zwei Listen von Zeichenketten gelten als gleich, wenn diese als Mengen gleich sind, also dieselben Elemente (möglicherweise mehrfach) enthalten. Geben Sie ein Dictionary zurück, das Mengen als Schlüssel und die entsprechenden Anzahlen als Werte enthält.
#
# Bemerkung: Beachten Sie, dass "a und b sind als Mengen gleich" nicht dasselbe ist wie "a ist eine Permutation von b": Die Listen [1,1,2] und [1,2,2] sind als Mengen gleich (mathematisch:
# {
# 1
# ,
# 2
# }
# {1,2}), aber es gibt keine Permutation, die die eine Liste in die andere überführt.
#
# Beispiel: Die Eingabe [["a", "b", "a"], ["b"], ["b", "a"]] soll dazu führen, dass die Menge
# {
# b
# }
# {b} einmal und die Menge
# {
# a
# ,
# b
# }
# {a,b} zweimal gefunden wird.

def histogram(lists):
    hist = {}
    for lst in lists:
        # Erstellen einer Menge aus der Liste, um die Reihenfolge zu ignorieren
        key = frozenset(lst)  # frozenset ist unveränderlich und kann als Schlüssel verwendet werden
        if key in hist:
            hist[key] += 1
        else:
            hist[key] = 1
    return hist

# Testfälle
print(histogram([["a", "b", "a"], ["b"], ["b", "a"]]))  # {frozenset({'b'}): 1, frozenset({'a', 'b'}): 2}
print(histogram([["x", "y"], ["y", "x"], ["z"]]))  # {frozenset({'x', 'y'}): 2, frozenset({'z'}): 1}
print(histogram([[], [], ["a"]]))  # {frozenset(): 2
