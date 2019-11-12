# '''
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# '''

# # flesh out multiple_letter count:
# def multiple_letter_count(string="abcde"):
#     return {letter:string.count(letter) for letter in string}

def list_manipulation(ip_list, ip_command, ip_location, ip_value=None):
    #print(ip_list)
    if ip_list:
        if ip_command == 'remove' and ip_location == 'end':
            return ip_list.pop()
        elif ip_command == 'remove' and ip_location == 'beginning':
            return ip_list.pop(0)
        elif ip_command == 'add' and ip_location == 'beginning':
            ip_list.insert(0,ip_value)
            return ip_list
        elif ip_command == 'add' and ip_location == 'end':
            ip_list.append(ip_value)
            return ip_list
    else:
        return None

def is_palindrome(test_string):
    test_string = test_string.lower().replace(' ','')
    return test_string[::-1] == test_string

def frequency(ip_list,search_term):
    return ip_list.count(search_term)

def multiply_even_numbers(collection):
    product = 1
    for i in range(0,len(collection)):
        if collection[i] % 2 == 0:
            product *= collection[i]
    return product 
#print(list_manipulation([1,2,3],'remove','end'))
#print(list_manipulation([1,2,3],'remove','beginning'))
#print(list_manipulation([1,2,3],'add','beginning',20))
#print(list_manipulation([1,2,3],'add','end',30))

# print(is_palindrome('testing')) # False
# print(is_palindrome('tacocat')) # True
# print(is_palindrome('han nah')) # True
# print(is_palindrome('robert')) # False
# print(is_palindrome('amanap lanaCAnalp anama')) # True

#print(frequency([1,2,3,4,4,4], 4)) # 3
#print(frequency([True, False, True, True], False)) # 1

print(multiply_even_numbers([2,3,4,5,6])) # 48