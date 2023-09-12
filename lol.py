def fr(n):
    if n == 1:
        return 1
    return fr(n - 1) * n


print(fr(5))
