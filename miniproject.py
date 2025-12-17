print("Welcome to liars game")


num_players = int(input("Enter number of players: "))
print(f"{num_players} have joined the game")

num_rounds = int(input("How many rounds do you want to play?: "))


scores = [0] * num_players

for round_no in range(1, num_rounds + 1):
    print(f"\n--- Round {round_no} ---")

    question = input("Enter a yes/no question: ")
    print(f"Question: {question}")

    
    answers = []
    for i in range(num_players):
        ans = input(f"Player {i+1}, do you agree with the question? (yes/no): ").lower()

        
        while ans not in ("yes", "no"):
            ans = input("Please enter yes or no only: ").lower()

        answers.append(ans)

    
    yes_count = answers.count("yes")
    no_count = answers.count("no")

    
    if yes_count > no_count:
        print(f"Minority group with {no_count} players won this round")
        for i in range(num_players):
            if answers[i] == "no":
                scores[i] += 1

    elif no_count > yes_count:
        print(f"Minority group with {yes_count} players won this round")
        for i in range(num_players):
            if answers[i] == "yes":
                scores[i] += 1

    else:
        print("No one won this round (Tie)")


print("\n--- Final Scores ---")
for i in range(num_players):
    print(f"Player {i+1}: {scores[i]} points")


max_score = max(scores)
winners = [i+1 for i, s in enumerate(scores) if s == max_score]

print("Winner(s):", winners)

