from typing import List


def distribute_compressed_parts(parts, processes) -> List[List[bytes]]:
    n = len(parts)
    p = processes

    if n == p:
        # Distribute a part in each process
        allocations = [[part] for part in parts]
    elif n > p:
        # Distribute between processes
        parts_per_process = n // p
        module = n % p
        allocations = []
        init = 0
        for i in range(p):
            end = init + parts_per_process + (1 if i < module else 0)
            allocations.append(parts[init:end])
            init = end
        return allocations
    else:
        # Distribute between processes, regardless of processes having no part assigned to it
        allocations = [[] for _ in range(p)]
        for i, part in enumerate(parts):
            allocations[i % p].append(part)

    return allocations
