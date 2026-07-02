
# Question 1: Programming Fundamentals
# Removes duplicates from a list of integers and sorts the result ascending.


def duplicate_and_sort(numbers):
    # a sorted list with duplicate values removed.
    unique_numbers = set(numbers) 
    # sorted() returns ascending order by default
    return sorted(unique_numbers)   


if __name__ == "__main__":
    numbers = [12, 7, 12, 3, 5, 7, 8, 3, 9]
    result = duplicate_and_sort(numbers)
    print("Original list:", numbers)
    print("Deduplicated & sorted:", result)
