#!/usr/bin/python


def main():

    input_data = enter_input()
    (withdraw, balance) = validate_data(input_data)
    print_output(withdraw, balance)

    return

def enter_input():
    print 'Enter withdraw amount and Account balance separated by space'
    input_data = raw_input("Input:\n")
    return input_data

def validate_data(input_data):
    try:
        (withdraw, balance) = input_data.strip().split(' ')
        withdraw = int(withdraw)
        balance = float(balance)
    except ValueError:
        print 'Incorrect input. Try again'
        exit(0)

    return (withdraw, balance)

def print_output(withdraw, balance):
    if withdraw > balance:
        print_output(balance)

    elif (withdraw % 5 != 0) or ( withdraw < 0):
        print_output(balance)

    elif withdraw % 5 == 0:
        balance = balance - withdraw - 0.5

    print '\nOutput:'
    print balance

if __name__ == '__main__':
  main()
