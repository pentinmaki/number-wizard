import random

def select_difficulty():
    """Valitse pelivaikeustaso"""
    print("\n=== SELECTA DIFFICULTY ===")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-500)")
    
    while True:
        try:
            choice = input("Choose difficulty (1-3): ").strip()
            if choice == "1":
                return 1, 50
            elif choice == "2":
                return 2, 100
            elif choice == "3":
                return 3, 500
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nGame cancelled.")
            exit()

def calculate_score(attempts, max_range):
    """Laske pisteet yritysten perusteella"""
    base_score = max(0, 100 - (attempts * 5))
    difficulty_multiplier = {50: 1, 100: 1.5, 500: 2}
    return int(base_score * difficulty_multiplier.get(max_range, 1))

def play_game():
    """Pääpelifunktio"""
    print("\n" + "="*40)
    print("  🧙 WELCOME TO NUMBER WIZARD! 🧙")
    print("="*40)
    
    total_score = 0
    games_played = 0
    
    while True:
        difficulty, max_number = select_difficulty()
        
        print(f"\n→ I'm thinking of a number between 1 and {max_number}...")
        
        number_to_guess = random.randint(1, max_number)
        guess = None
        attempts = 0
        max_attempts = max_number // 5  # Yläräja yrityksille
        
        while guess != number_to_guess:
            try:
                if attempts >= max_attempts:
                    print(f"\n✗ Game Over! You've reached the maximum attempts ({max_attempts}).")
                    print(f"The number was: {number_to_guess}")
                    break
                
                remaining = max_attempts - attempts
                prompt = f"Guess (attempts left: {remaining}): "
                guess = int(input(prompt))
                attempts += 1
                
                # Validoi syöte alueen sisällä
                if guess < 1 or guess > max_number:
                    print(f"Please enter a number between 1 and {max_number}.")
                    attempts -= 1
                    continue
                
                if guess < number_to_guess:
                    diff = number_to_guess - guess
                    print(f"↑ Too low! (difference: ~{diff})")
                elif guess > number_to_guess:
                    diff = guess - number_to_guess
                    print(f"↓ Too high! (difference: ~{diff})")
                else:
                    score = calculate_score(attempts, max_number)
                    total_score += score
                    games_played += 1
                    
                    print(f"\n✓ Congratulations! You guessed it in {attempts} tries!")
                    print(f"Points earned: {score}")
                    print(f"Total score: {total_score}")
                    
                    # Yritysanalyysi
                    avg_attempts = max_number // 2 // 2  # Optimaalinen arvio
                    if attempts <= avg_attempts:
                        print("⭐ Amazing! You're a true wizard!")
                    elif attempts <= avg_attempts * 2:
                        print("👍 Good job!")
                    else:
                        print("💡 Keep practicing!")
                    
            except ValueError:
                print("⚠ Please enter a valid number.")
                attempts -= 1
            except KeyboardInterrupt:
                print("\n\nGame cancelled.")
                break
        
        # Kysy pelausta uudelleen
        print("\n" + "-"*40)
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
    
    # Lopputilastot
    if games_played > 0:
        print("\n" + "="*40)
        print("  📊 FINAL STATISTICS")
        print("="*40)
        print(f"Games played: {games_played}")
        print(f"Total score: {total_score}")
        avg_score = total_score // games_played
        print(f"Average score per game: {avg_score}")
        print("="*40)

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nThanks for playing!")
    print("\nGoodbye! 👋")
