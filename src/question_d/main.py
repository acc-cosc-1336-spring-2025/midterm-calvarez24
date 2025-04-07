#add import

from question_d import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number to sum the even values or type quit to exit")

        if user_input.lower() == 'quit':
            print("Goodbye")
            break

        if user_input.isdigit():
            num = int(user_input)
            total_sum = get_sum_of_evens(num)
            print("Sum of even numbers up to", num, ":", total_sum)
        else:
            print("Invalid number")

main()