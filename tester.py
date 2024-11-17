from geo.utils import calculate_area
import sys

def main():
    radius = float(sys.stdin.read().strip())
    expected_area = 314.1592653589793
    calculated_area = calculate_area(radius)
    
    print(f"Calculated Area: {calculated_area}")
    
    # 결과 확인
    if abs(calculated_area - expected_area) < 1e-9:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()