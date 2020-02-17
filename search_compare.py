# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:08:12 2020

@author: kathybootsri
"""
#from timeit import Timer

def first_func(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def sec_func(a_list, item):
    a_list.sort()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos+1
    return found

def sequential_search(a_list, item):
    from timeit import Timer
    print(first_func(a_list, item))
    func = "first_func(" + str(a_list) + ", " + str(item) + ")"    
    t1 = Timer(str(func), "from __main__ import first_func")
    print("Sequential Search: ",t1.timeit(number=1000), "milliseconds")


def ordered_sequential_search(a_list, item):
    from timeit import Timer        
    print(sec_func(a_list, item))
    func = "sec_func(" + str(a_list) + ", " + str(item) + ")"    
    t1 = Timer(str(func), "from __main__ import sec_func")
    print("Ordered Sequential Search: ",t1.timeit(number=1000), "milliseconds") 

def third_func(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
        return found

def binary_search_iterative(a_list, item):
    from timeit import Timer        
    print(sec_func(a_list, item))
    func = "third_func(" + str(a_list) + ", " + str(item) + ")"    
    t1 = Timer(str(func), "from __main__ import third_func")
    print("Binary Search Iterative: ",t1.timeit(number=1000), "milliseconds") 
    
def fourth_func(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return fourth_func(a_list[:midpoint], item)
            else:
                return fourth_func(a_list[midpoint + 1:], item)

def binary_search_recursive(a_list, item):
    from timeit import Timer        
    print(fourth_func(a_list, item))
    func = "fourth_func(" + str(a_list) + ", " + str(item) + ")"    
    t1 = Timer(str(func), "from __main__ import fourth_func")
    print("Binary Search Recursive: ",t1.timeit(number=1000), "milliseconds") 

def sequential_search_analyze(item, list_size):
     print("Analyzing Sequential Search Runtime...")
     from statistics import mean
     import random
     t1_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         first_func(a_list, item)
         func = "first_func(" + str(a_list) + ", " + str(item) + ")"    
         t1 = Timer(str(func), "from __main__ import first_func")
         t1_list.append(t1.timeit(number=1000))
                
     seq_avg = mean(t1_list)
     print("Sequential Search took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))
         
def ordered_sequential_analyze(item, list_size):
     print("Analyzing Ordered Sequential Search Runtime...")    
     from statistics import mean
     import random
     t1_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         sec_func(a_list, item)
         func = "sec_func(" + str(a_list) + ", " + str(item) + ")"    
         t1 = Timer(str(func), "from __main__ import sec_func")
         t1_list.append(t1.timeit(number=1000))
                
     seq_avg = mean(t1_list)
     print("Ordered Sequential Search took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))

def binary_iterative_analyze(item, list_size):
     print("Analyzing Binary Search Iterative Runtime...") 
     from statistics import mean
     import random
     t1_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         third_func(a_list, item)
         func = "third_func(" + str(a_list) + ", " + str(item) + ")"    
         t1 = Timer(str(func), "from __main__ import third_func")
         t1_list.append(t1.timeit(number=1000))
                
     seq_avg = mean(t1_list)
     print("Binary Search Iterative took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))

def binary_recursive_analyze(item, list_size):
     print("Analyzing Binary Search Recursive Runtime...")     
     from statistics import mean
     import random
     t1_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         fourth_func(a_list, item)
         func = "fourth_func(" + str(a_list) + ", " + str(item) + ")"    
         t1 = Timer(str(func), "from __main__ import fourth_func")
         t1_list.append(t1.timeit(number=1000))
                
     seq_avg = mean(t1_list)
     print("Binary Search Recursive took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))

"""TEST BASIC SEARCH FOR ONE INPUT LIST"""
test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
sequential_search(test_list, 3)
sequential_search(test_list, 13)

ordered_sequential_search(test_list, 3)
ordered_sequential_search(test_list, 13)

binary_search_iterative(test_list, 3)
binary_search_iterative(test_list, 13)

binary_search_recursive(test_list, 3)
binary_search_recursive(test_list, 13)


"""TEST ANALYSIS FOR LARGE SET OF RANDOM LISTS"""
if __name__ == "__main__":
    sequential_search_analyze(-1, 500) 
    #sequential_search_analyze(-1, 1000) 
    #sequential_search_analyze(-1, 10000) 
    
    ordered_sequential_analyze (-1, 500)
    #ordered_sequential_analyze (-1, 1000)
    #ordered_sequential_analyze (-1, 10000)
    
    binary_iterative_analyze (-1, 500)
    #binary_iterative_analyze (-1, 1000)
    #binary_iterative_analyze (-1, 10000)
    
    binary_recursive_analyze (-1, 500)
    #binary_recursive_analyze (-1, 1000)
    #binary_recursive_analyze (-1, 1000)








