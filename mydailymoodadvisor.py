import datetime

name = input("Enter your name: ")
mood = input("Enter your current mood (e.g., happy, sad, stressed, tired): ").lower()
energy = int(input("Enter your energy level (1 to 10): "))

print("\n--- Daily Mood Advice ---")
print("User Name:", name)
print("Current Mood:", mood)
print("Energy Level:", energy)

if mood == "happy" and energy > 5:
    print("Advice: Great energy! Go out and spread your positive vibe!")
elif mood == "happy":
    print("Advice: Keep smiling and take a cozy break to enjoy the day!")
elif mood == "sad" or mood == "stressed":
    if energy > 5:
        print("Advice: Take a light walk or listen to your favorite music to relax.")
    else:
        print("Advice: Get some rest, drink water, and take it easy today.")
elif mood == "tired" or energy <= 3:
    print("Advice: Time to recharge! Get some sleep or grab a warm drink.")
else:
    print("Advice: Stay mindful and make time for something you enjoy today!")

now = datetime.datetime.now()
print("Date and Time:", now)