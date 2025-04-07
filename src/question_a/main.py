#add import
from question_a import get_persons_category

def main():
    max_inputs = 5
    for i in range(max_inputs):
        user_input = input("Enter the person's age or type quit to exit the program: ")

        if user_input.lower() == "quit":
            print("Exiting program..")
            break 

        if user_input.isdigit():
            age = int(user_input)
            category = get_persons_category(age)
            print("The person is classified as: " + category)
        else:
            print("Invalid number")

main()


