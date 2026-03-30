def solve():
    a = [0] * 21
    a[1] = 1
    a[2] = 1
    for n in range(1, 19):
        a[n+2] = 3 * a[n+1] - a[n]
        
    for i in range(1, 21):
        b_i = a[i] % 8
        print(f"({a[i]}, {b_i})")

if __name__ == '__main__':
    solve()
