def distribute(parts, processes):
    n = len(parts)
    p = processes

    if n == p:
        # Distribute a part in each process
        allocations = [[part] for part in parts]
    elif n > p:
        # Distribute between processes
        allocations = [[] for _ in range(p)]
        for i, part in enumerate(parts):
            allocations[i % p].append(part)
    else:
        # Distribute between processes, regardless of processes having no part assigned to it
        allocations = [[] for _ in range(p)]
        for i, part in enumerate(parts):
            allocations[i % p].append(part)

    return allocations
