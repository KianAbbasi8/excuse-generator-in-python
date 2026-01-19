# Title: Excuse Generator
# Description: This Python script generates random excuses by combining a subject, a reason, 
# and a time. It can be used for fun or to simulate unexpected problems in daily tasks.

import random

# List of subjects (things that can fail)
subjects = [
    "My internet ",
    "The server ",
    "My laptop ",
    "The electricity ",
    "My phone ",
    "The system ",
    "My alarm ",
    "The application ",
    "The update ",
    "My keyboard "
]

# List of reasons (what went wrong)
reasons = [
    "stopped working ",
    "crashed suddenly ",
    "was under maintenance ",
    "froze at the wrong time ",
    "ran out of battery ",
    "needed an urgent restart ",
    "was not responding ",
    "updated automatically ",
    "lost connection ",
    "behaved strangely "
]

# List of times (when it happened)
times = [
    "right before submission.",
    "at the last moment.",
    "during the meeting.",
    "just before the deadline.",
    "while I was working.",
    "in the middle of the task.",
    "exactly at the wrong time.",
    "when everything was ready.",
    "during the final step.",
    "without any warning."
]

# Main loop to generate excuses
while True:
    # Randomly select one subject, reason, and time
    subject = random.choice(subjects)
    reason = random.choice(reasons)
    time = random.choice(times)
    
    # Combine into a full excuse
    excuse = f"{subject}{reason}{time}"
    
    # Display the excuse
    print("\n" + excuse)
    
    # Ask the user if they want another excuse
    input_user = input("Do you want to create another excuse? yes / no: ").strip().lower()
    if input_user == "no":
        print("Thanks for using the Excuse Generator!")
        break
