# Beginner project 7.
# Mad libs

print("Welcome to the mad libs game!")
name = input("Enter a name: ").capitalize()
verb1 = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
body_part = input("Enter a part of the body: ")
verb2 = input("Enter another verb: ")

story = f'''The King {name} did not know of anything that could have {verb1} at the palace
            during his absence worth the {adjective} he was experiencing;
            so he very readily gave his {noun1}, and was freed.
            When he had shaken the {noun2} from his {body_part}, he looked in the well for the
            ugly monster which had held him captive, but he was nowhere to be seen.
            Summoning his attendants, he at once set out for home, where he {verb2} in a few days.'''

print(story)
