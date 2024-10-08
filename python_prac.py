def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    total = 0
    count = 0
    if grades == []:
        return -1
    for grade in grades:
        if grade >= 0:
            total += grade
            count += 1
    return total / count

def find_prime_factors(number):
    """Write code to return the prime factors of the number. 

    Args:
        number (int): Number to find the prime factors of
    """
    factors = []
    
    # Handle 2 separately (for even numbers)
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    
    # Check for odd factors from 3 upwards
    n = 3
    while n * n <= number:
        while number % n == 0:
            factors.append(n)
            number //= n
        n += 2
    
    # If n is still greater than 2, it's a prime factor
    if number > 2:
        factors.append(number)
      
    return factors

def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """
   
    future_value = principal * (1 + rate)**years
    interest_amount = future_value - principal
    
    return interest_amount

def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """
    word_list = []
    for number in code:
        if number == 0:
            word_list.append(' ')  # add space for 0    
        else:
            valid_number = (number - 1) % 26 + 1
            word_list.append(chr(valid_number + 64)).lower()  # Convert number to loweercase letter
    
    return ''.join(word_list)


def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    list_results = []
    for i in range(1, length+1):
        list_results.append("*" * i)
    
    return "\n".join(list_results)
        

def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    list_result = []
    for i in range(1, length+1):
        if len(list_result) < 2:
            list_result.append("*" * i)
        elif len(list_result) == length-1:
            list_result.append("*" * i)
        else:
            string_test = "*" + (" "*(i-2)) + "*"
            list_result.append(string_test)
    return "\n".join(list_result)

# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """
    count = 10
    while count <= 10:
        user_input = int(input("guess the number: "))
        if user_input == number:
            print("Correct")
            break
        else:
            print("Incorrect")
            count -= 1
            
print(hollow_triangle(5))
#print(triangles(5))