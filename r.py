def get_runner_speeds():
    speeds = {}
    n = int(input("Enter the number of runners: "))
    for i in range(1, n + 1):
        speed = float(input(f"Enter speed for Runner (m/s){i}: "))
        speeds[i] = speed
    return speeds

def compare(r1, r2, speeds):
    return r1 if speeds[r1] < speeds[r2] else r2

def find_fastest_runner(speeds):
    n = len(speeds)
    wins = [0] * (n + 1)
    for i in speeds:
        for j in speeds:
            if i != j:
                winner = compare(i, j, speeds)
                if winner == i:
                    wins[i] += 1
    for i in speeds:
        if wins[i] == n - 1:
            return i
    return -1

def main():
    print("=== Fastest Runner Finder ===")
    speeds = get_runner_speeds()
    fastest = find_fastest_runner(speeds)
    if fastest != -1:
        print(f"\n Fastest Runner is: Runner {fastest} with speed {speeds[fastest]} m/s")
    else:
        print("\n No unique fastest runner identified.")

if __name__ == "__main__":
    main()
