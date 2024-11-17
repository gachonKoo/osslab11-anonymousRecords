import geo.utils as utils

def main():
    a, b = 3, 4
    c = utils.pythagoras(a, b)
    expected_c = 5.0
    print('c =', c)

    r = 10
    area = utils.circle(r)
    expected_area = 314.1592653589793
    print('area =', area)

    if abs(c - expected_c) < 1e-9:
        print("Pythagorean Success")
    else:
        print("Pythagorean Failure")

    if abs(area - expected_area) < 1e-9:
        print("Circle Area Success")
    else:
        print("Circle Area Failure")

if __name__ == "__main__":
    main()