def generate(n, mod):
    if not ((type(n) == type(int())) and (type(mod) == type(int()))):
        raise TypeError
    if not ((n > 0) and (mod > n)):
        raise ValueError
    generated = []
    cycles = []
    for x in range(1, mod):
        if x not in generated:
            cycles.append[[x]]
            next = (n * x) % mod
            while next not in cycles[-1]:
                cycles[-1].append(next)
                generated.append(next)
                next = (cycles[-1][-1] * n) % mod
    return cycles
