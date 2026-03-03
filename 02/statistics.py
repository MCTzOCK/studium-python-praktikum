def statistics(data):
    sd = sorted(data);
    minimum = sd[0]
    maximum = sd[-1]
    mean = sum(data) / len(data)
    median = 0

    if len(sd) % 2 == 1:
        median = sd[len(sd) // 2]
    else:
        median = (sd[len(sd) // 2 - 1] + sd[len(sd) // 2]) / 2

    variance = sum((x - mean) ** 2 for x in data) / len(data)

    return {
        'mean': mean,
        'variance': variance,
        'median': median,
        'minimum': minimum,
        'maximum': maximum
    }


print(statistics([-3,-5,-4,-6]))