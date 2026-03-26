def apply_updates(data, updates):
    n = len(data)
    diff = [0] * (n + 1)

    # Mark ranges
    for l, r in updates:
        diff[l - 1] += 1
        if r < n:
            diff[r] -= 1

    # Prefix sum to get number of flips per index
    flips = 0
    for i in range(n):
        flips += diff[i]
        if flips % 2 == 1:  # odd number of negations
            data[i] *= -1

    return data

#my brute force fails for large amounts
# def brute_force(data, updates):
#     for l,r in updates:
#         for i in range(l-1, r):
#             data[i] = data[i] * -1
#     return data


data = [1, 2, 3, 4, 5]
updates = [
    [1, 3],  # negate indices 0–2
    [2, 4]   # negate indices 1–3
]
# print(brute_force(data, updates))
print(apply_updates(data, updates))