import random

def simulate_dice_rolls(num_rolls):
    counts = [0] * 11  # Initialize counts for sums from 2 to 12

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        counts[total - 2] += 1  # Increment count for the corresponding sum

    probabilities = [count / num_rolls for count in counts]  # Calculate probabilities
    return probabilities

def display_probabilities(probabilities):
    print("Sum\tProbability")
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i}\t{prob:.2%} ({prob * 36:.0f}/36)")

def main():
    num_rolls = 1000000  # Number of dice rolls
    probabilities = simulate_dice_rolls(num_rolls)
    display_probabilities(probabilities)

if __name__ == "__main__":
    main()
