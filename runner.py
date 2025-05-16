# Sample speed data (higher value = faster runner)
runner_speeds = {
    1: 9.8,
    2: 10.2,
    3: 10.5,
    4: 11.0  # Fastest runner
}

# Function to compare two runners
def compare(runner1, runner2):
    """
    Simulate a race between two runners.
    Returns the winner (runner number).
    """
    if runner_speeds[runner1] > runner_speeds[runner2]:
        return runner1
    else:
        return runner2

# Main function to find the fastest runner
def find_fastest_runner(n):
    wins = [0] * (n + 1)  # index 0 unused

    # Compare each runner with every other runner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                winner = compare(i, j)
                if winner == i:
                    wins[i] += 1

    # Fastest runner will have (n - 1) wins
    for i in range(1, n + 1):
        if wins[i] == n - 1:
            return i

    return -1  # No fastest runner found

# Example usage
n = 4  # number of runners
fastest = find_fastest_runner(n)
print(f"The fastest runner is: Runner {fastest}")
