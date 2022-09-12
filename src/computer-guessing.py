# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt: str, options: list[str]) -> str:
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


print("Please thing of a number from 1 to 20, both included.")
print("Let me know how good my guess is.\n")

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.
for guess in reversed(range(1,21)):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break

   print("I must have been too low, right?", result)        


# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.
upper=20
lower=1
while True:
    guess=((upper+lower)//2)
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    if result == "low":
        lower=guess+1
        print("I must have been too low, right?", result)
    if result == "high":
        upper= guess-1
        print("I must have been too low, right?", result)
