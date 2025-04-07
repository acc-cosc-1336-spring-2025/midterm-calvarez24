#add import
from question_c import reverse_string

def main():
    while True:
        user_input = input("enter a string to reverse or type quit to exit:")

        if user_input.lower() == 'quit':
            print("Goodbye")
            break 

        reversed_str = reverse_string(user_input)
        print("Reversed string: " + reversed_str)

main()