def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def combination(n, r):
    if r == 0 or r == n:
        return 1
    return combination(n - 1, r - 1) + combination(n - 1, r)


def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


if __name__ == "__main__":
    print("Power Function Result:")
    print("2^8 =", power(2, 8))

    print("\nCombination Function Result:")
    print("C(5,2) =", combination(5, 2))

    print("\nTower of Hanoi Steps:")
    hanoi(3, 'A', 'B', 'C')
