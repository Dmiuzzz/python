l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n_l = [l[i] for i in range(1, len(l)) if l[i] > l[i-1]]
print(n_l)