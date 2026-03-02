def comprehend(a):
    a = [x for x in a if x[0] not in "zZ"]
    a = [str.upper(x) for x in a]
    return a


if __name__ == "__main__":
    print(comprehend(["Hallo", "Welt", "Zeitung", "lesen"]))