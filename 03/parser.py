#  Der Parser erhält nicht die Zeichenkette als Eingabe, sondern die Ausgabe des Tokenizers. Die Zerlegung der Zeichenkette in Tokens ist bereits die halbe Miete. Der zweite Schritt ist die Erstellung des Syntaxbaums. Diesen Schritt realisieren wir in der Funktion
#
# def parseMinus(array):
#
# welche die von tokenize erstellte Liste entgegen nimmt. Die Funktion gibt ein Tupel aus zwei Werten (tree, length) zurück, nämlich den erstellten Syntaxbaum und die Anzahl der Tokens, die geparsed wurden. Die Strategie funktioniert grob wie folgt:
#
# while True:
# 	parse operand
# 	parse operator
#
# Sie parsen also abwechselnd Operanden und Operatoren.
#
# Im Detail können Sie diese Logik wie folgt implementieren:
#
#     Schleife
#         Starten Sie mit einer Schleife. In dieser Schleife sind das Parsen von Operand und Operator eingebunden.
#     Operand parsen: Ein Operand kann eine Zahl oder ein Ausdruck sein, der in Klammern steht. Gehen Sie wie folgt vor:
#         Sie erstellen eine Variable expr = None, in welcher der bisherige Syntaxbaum gespeichert ist.
#         Erstellen Sie eine Variable pos = 0, die die aktuelle Position im Array markiert. Dieser Wert wird immer dann geeignet erhöht, wenn Tokens erfolgreich geparsed wurden. Somit ist array[pos] immer das nächste zu verarbeitende Token.
#         Wir gehen davon aus, dass wir eine beliebig lange Kette von Ausdrücken und Operatoren vorfinden, etwa "100 - 20 - 13 - 4". Also parsen wir in einer Schleife immer abwechselnd einen Ausdruck (Operand) und einen Operator.
#         Für den Operanden gibt es folgende Fälle:
#             Wenn das Ende des Arrays erreicht ist, so wird eine Exception geworfen, denn ein Ausdruck darf nicht leer sein oder mit einem Operator (Minuszeichen) enden.
#             Wenn das aktuelle Token ein Minuszeichen oder eine Klammer zu ist, so wird ebenfalls eine Exception geworfen.
#             Wenn das aktuelle Token eine Zahl ist (also wenn isinstance(array[pos], int) erfüllt ist), dann ist diese Zahl ein (sehr einfacher) Ausdruck. Diesen merken Sie sich in einer Variablen, nennen wir sie t. Dann erhöhen Sie pos um eins.
#             Wenn das aktuelle Token eine Klammer auf ist, so wird parseMinus rekursiv mit der Liste array[pos+1 : ] aufgerufen. Diese beginnt hinter der öffnenden Klammer. Der rekursive Funktionsaufruf wird uns als Rückgabewert den von ihm erstellten Unter-Syntaxbaum und die Anzahl der verarbeiteten Tokens zurückliefern. Den ersten Rückgabewert speichern Sie wieder in t. Den zweiten Wert müssen Sie zu pos dazu addieren. Schließlich wird überprüft, ob das folgende Token eine Klammer zu ist — sonst wird eine Exception geworfen. Denken Sie daran, pos auch für die beiden Klammern zu erhöhen.
#         Jetzt haben wir einen Operanden in t zwischengespeichert.
#         Sobald der Token vorliegt, muss folgendes passieren, um diesen in den Syntaxbaum einzufügen:
#             Falls die Variable expr den Wert None enthält, so wird der neu erstellte Ausdruck t darin gespeichert.
#             Andernfalls wird ein neues Objekt Subtraction(expr, t) erstellt und in expr gespeichert.
#     Operator oder Ende des Ausdrucks parsen: An dieser Stelle im Ausdruck können ein Minuszeichen, eine schließende Klammer oder das Ende der Zeichenkette auftreten. Alle anderen Fälle sind Fehler.
#         Beim Parsen des Operators gibt es die folgenden Fälle:
#             Wenn das Ende des Arrays erreicht ist, so wird die Schleife beendet.
#             Wird der Operator "-" gefunden, so wird pos erhöht und die Schleife läuft weiter.
#             Wird eine Klammer zu gefunden, so wird die Schleife beendet.
#             Wird eine Klammer auf oder eine Zahl gefunden, so wird eine Exception geworfen.
#         Wenn die Schleife beendet ist, so gibt die Funktion das Tupel (expr, pos) zurück.

from tokenizer import tokenize

class Subtraction:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        l = "(" + str(self.left) + ")" if isinstance(self.left, Subtraction) else str(self.left)
        r = "(" + str(self.right) + ")" if isinstance(self.right, Subtraction) else str(self.right)
        return l + " - " + r

    def __call__(self):
        l = self.left() if isinstance(self.left, Subtraction) else int(self.left)
        r = self.right() if isinstance(self.right, Subtraction) else int(self.right)
        return l - r

def parseMinus(array):
    expr = None
    pos = 0
    while True:
        if pos >= len(array):
            raise ValueError("Unexpected end of expression")
        if array[pos] == "-" or array[pos] == ")":
            raise ValueError("Unexpected operator or closing parenthesis")
        if isinstance(array[pos], int):
            t = array[pos]
            pos += 1
        elif array[pos] == "(":
            t, length = parseMinus(array[pos + 1:])
            pos += length + 2
            if pos > len(array) or array[pos - 1] != ")":
                raise ValueError("Expected closing parenthesis")
        else:
            raise ValueError("Unexpected token: " + str(array[pos]))

        if expr is None:
            expr = t
        else:
            expr = Subtraction(expr, t)

        if pos >= len(array):
            break
        if array[pos] == "-":
            pos += 1
        elif array[pos] == ")":
            break
        else:
            raise ValueError("Unexpected token: " + str(array[pos]))
    return (expr, pos)

def parse(array):
    result = parseMinus(array)
    if result[1] != len(array):
        raise Exception("invalid symbol " + array[result[1]])
    return result[0]

input = "(40 - 5) - (18 - (13 - 10))"
expr = parse(tokenize(input))
print(expr())   # 20
print(expr)     # (40 - 5) - (18 - (13 - 10))