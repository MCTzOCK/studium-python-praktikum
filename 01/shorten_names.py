def shortName(name):
    if " " not in name:
        return name
    parts = name.split()
    lastName = parts[-1]
    initials = [part[0] for part in parts[:-1]]
    return ".".join(initials) + ". " + lastName

if __name__ == "__main__":
    print(shortName("Johnson"))
    print(shortName("Harry Potter"))
    print(shortName("John Fitzgerald Kennedy"))
    print(shortName("John Ronald Reuel Tolkien"))