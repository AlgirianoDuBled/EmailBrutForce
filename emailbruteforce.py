import time

# Lijst van mogelijke wachtwoorden
possible_passwords = ["azerty", "Schildpad", "paswoord", "JamesBond007", "Caroline", "admin", "Superman", "12345", "password", "letmein", "admin", "qwerty", "welcome", "secret123"]

# Correct wachtwoord voor de film
correct_password = "secret123"

def brute_force(email):
    print(f"Proberen in te loggen op het account van {email}...\n")

    for password in possible_passwords:
        time.sleep(1)  # Simuleer de tijd die nodig is voor brute-forcing
        print(f"Proberen: {password}")

        if password == correct_password:
            print(f"Succes! Het wachtwoord voor {email} is: {password}")
            break
    else:
        print("Wachtwoord niet gevonden, probeer het opnieuw!")

if __name__ == "__main__":
    # Vraag om een e-mailadres
    email = input("Voer het e-mailadres in: ")
    brute_force(email)
