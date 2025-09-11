Original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numberlist = []
def filter_even_numbers(nums):
    for num in nums:
        if num % 2 == 0:
            even_numberlist.append(num)
    return even_numberlist
filter_even_numbers(Original_list)
print(f"Original list: {Original_list}")
print(f"List with even numbers only: {even_numberlist}")