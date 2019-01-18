def print_root():
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1,r2))

a = 1
b = 2
c = -8

print_root()

a = 2
b = -6
c = -8

print_root()

x = int(input())
y = int(input())
z = int(input())


def print_root2(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1,r2))

print_root2(x,y,z)