def solve():
    for a in range(1, 31):
        for b in range(1, 31):
            if (b**2 - 1) % a == 0 and (a**2 + 1) % b == 0:
                print(f"({a}, {b})")

if __name__ == '__main__':
    solve()
