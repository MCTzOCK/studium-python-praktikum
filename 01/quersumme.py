# Schreiben Sie eine Funktion cross_sum(n, b). Die Parameter n und b sind beide natürliche Zahlen, b≥2
# Die Funktion soll die Quersumme der Zahl n im Zahlensystem zur Basis b berechnen und das Ergebnis zurückgeben.

def cross_sum(n, b):
    if b < 2:
        raise ValueError("Die Basis b muss größer oder gleich 2 sein.")

    quersumme = 0
    while n > 0:
        quersumme += n % b
        n //= b

    return quersumme


if __name__ == "__main__":
    print(cross_sum(1234, 10))  # Ausgabe: 10
    print(cross_sum(1234, 16))  # Ausgabe: 1 + 2 + 3 + 4 = 10
    print(cross_sum(255, 16))   # Ausgabe: 15 + 15 = 30
    print(cross_sum(212, 10))
    print(cross_sum(212, 16))