import random

def truth_or_dare():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}! Let's play Truth or Dare.")
    
    while True:
        choice = input("Enter 't' for Truth, 'd' for Dare, or 'q' to quit: ").lower()
        
        if choice == 't':
            print("Truth: What is your biggest fear?")
            # You can add more truth questions here
        elif choice == 'd':
            print("Dare: Do 10 jumping jacks.")
            # You can add more dare tasks here
        elif choice == 'q':
            print("Thanks for playing! See you next time.")
            break
        else:
            print("Invalid choice. Please enter 't', 'd', or 'q'.")

truth_or_dare()
