import random

# List of words to choose from
word_list = ["python", "java", "ruby", "javascript", "php", "csharp", "swift","Hello", "world", "computer", "programming", "language", "algorithm", "data", "analysis", "network", "security", "encryption", "decryption", "artificial", "machine", "neural", "deep", "language", "big", "cloud", "virtual", "augmented", "blockchain", "cryptocurrency", "internet", "cybersecurity", "privacy", "digital","automation", "chatbot", "customer", "e-commerce", "entrepreneurship", "innovation", "marketing", "mobile app", "online", "project", "social", "user", "virtual", "web", "content", "branding", "marketing", "gamification", "growth", "influencer", "search ", "video", "web", "website", "cloud storage", "digital art", "e-book", "e-commerce platform", "ecommerce website", "email marketing", "infographic", "landing page", "responsive design", "sales funnel", "social media advertising", "social media management", "web hosting","artificial general intelligence", "brain-computer interface", "cybernetics", "quantum computing", "nanotechnology", "genetic engineering", "robotics", "space exploration", "virtual reality headset", "wearable technology", "augmented reality glasses", "autonomous vehicles", "drones", "smart home", "smart city", "smart grid", "smartphone", "smartwatch", "voice assistant", "3D printing", "blockchain technology", "decentralized finance", "cryptocurrency wallet", "distributed ledger", "stablecoin", "NFTs", "machine vision", "fintech", "neurotechnology", "neuromarketing", "neuroscience", "quantum mechanics", "cyber warfare", "ethical hacking", "penetration testing", "vulnerability assessment", "data privacy regulation", "cyber insurance", "cybersecurity framework", "endpoint", "cloud", "zero"]
# Select a random word from the list
chosen_word = random.choice(word_list)



# Create an empty list to store the user's guesses
display = ["_" for letter in chosen_word]

# Initialize the number of tries
tries = 6
previous_guesses = []

# Loop until the user has no more tries or has guessed the word
while tries > 0 and "_" in display:
    # Display the current state of the game
    print(f"{' '.join(display)}  (Tries left: {tries})")

    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    if guess in previous_guesses:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
    previous_guesses.append(guess)
    # Check if the user's guess is in the chosen word
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        tries -= 1
        print(f"{guess} is not in the word. You have {tries} tries left.")




# Check if the user won or lost
if "_" not in display:
    print(f"Congratulations! You guessed the word {chosen_word}!")
else:
    print(f"Sorry, you ran out of tries. The word was {chosen_word}. Better luck next time!")

