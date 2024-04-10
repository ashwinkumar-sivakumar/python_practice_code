'''Given two lists with elements and indices, write a Python program to find elements of list 1 at indices present in list 2.

Examples:

Input : lst1 = [10, 20, 30, 40, 50]
        lst2 = [0, 2, 4]
Output : [10, 30, 50]
Explanation:
Output elements at indices 0, 2 and 4 i.e 10, 30 and 50 respectively.

Input : lst1 = ['Hello', 'geeks', 'for', 'geeks']
        lst2 = [1, 2, 3]
Output : ['geeks', 'for', 'geeks']'''

def find_list(lst1, lst2):
    return[lst1[i] for i in lst2] #note to put square brackets

lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(find_list(lst1,lst2))