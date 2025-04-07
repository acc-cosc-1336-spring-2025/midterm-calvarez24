#add import
from question_b import use_global, global_variable

global_variable = 10

def main():
    print("Original variable:", global_variable)
    use_global()
    print("Modified variable:", global_variable)


main()

