# excuse-generator-in-python
A fun Python program that generates random excuses for work, school, or daily life by combining a subject, a reason, and a time. Perfect for playful situations or creating creative excuses on the fly.



working 


START

# Define lists of possible parts of excuses
subjects = [list of things that can fail]
reasons = [list of reasons things went wrong]
times = [list of when it happened]

LOOP indefinitely
    # Pick one random item from each list
    subject = RANDOM CHOICE from subjects
    reason = RANDOM CHOICE from reasons
    time = RANDOM CHOICE from times

    # Combine them into a full excuse
    excuse = subject + reason + time

    # Display the excuse
    PRINT excuse

    # Ask user if they want another excuse
    user_input = INPUT "Do you want to create another excuse? (yes/no)"

    # If user says 'no', exit the loop
    IF user_input is "no" THEN
        PRINT "Thanks for using the Excuse Generator!"
        BREAK LOOP
    END IF

END LOOP

END
