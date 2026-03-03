def floodfill(arr, x, y, value):
    w = arr[y][x]
    todo = [(x, y)]
    seen = set(todo)

    while todo:
        x, y = todo.pop()
        arr[y][x] = value

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(arr[0]) and 0 <= ny < len(arr) and arr[ny][nx] == w and (nx, ny) not in seen:
                todo.append((nx, ny))
                seen.add((nx, ny))

# Testfälle
a = [["#","#","*","*","*","!"],
     ["*","#","#","*","!","!"],
     ["*","#","#","!","#","#"],
     ["*","#","#","!","#","*"],
     ["#","#","!","!","#","#"],
     ["#","#","#","!","!","#"],
     ["#","*","#","#","#","#"]]

floodfill(a, 1, 0, "-")
print(a)