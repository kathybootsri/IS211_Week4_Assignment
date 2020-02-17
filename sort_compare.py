# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:19:54 2020

@author: -
"""
def insert_func(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


def shell_func(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

#      print("After increments of size",sublistcount, "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def insert_sort(a_list):
    from timeit import Timer        
    insert_func(a_list)
#    print(a_list)
    func = "insert_func(" + str(a_list) + ")"    
    t1 = Timer(str(func), "from __main__ import insert_func")
    print("Insert Sort: ",t1.timeit(number=1000), "milliseconds") 
    
def shell_sort(a_list):
    shell_func(a_list)
#    print(a_list)
    from timeit import Timer
    func = "shell_func(" + str(a_list) + ")"    
    t1 = Timer(str(func), "from __main__ import shell_func")
    print("Shell Sort: ",t1.timeit(number=1000), "milliseconds") 
    
def python_sort(a_list):
    a_list.sort()
#    print(a_list)
    import timeit
    func = str(a_list) + ".sort()"   
    print("Python Sort Sort: ", timeit.timeit(func, number=1000), "milliseconds") 

def insert_sort_analyze(list_size):
     print("Analyzing Insert Sort Runtime...")
     from statistics import mean
     import random
     t1_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         insert_func(a_list)
         func = "insert_func(" + str(a_list) + ")"     
         t1 = Timer(str(func), "from __main__ import insert_func")
         t1_list.append(t1.timeit(number=1000))
                
     seq_avg = mean(t1_list)
     print("Insert Sort took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))

def shell_sort_analysis(list_size):
     print("Analyzing Shell Sort Runtime...")
     from statistics import mean
     import random
     t2_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         shell_func(a_list)
         func = "shell_func(" + str(a_list) + ")"      
         t2 = Timer(str(func), "from __main__ import shell_func")
         t2_list.append(t2.timeit(number=1000))
                
     seq_avg = mean(t2_list)
     print("Shell Sort took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))

def python_sort_analysis(list_size):
     print("Analyzing Python Sort Runtime...")
     from statistics import mean
     import random
     t3_list = []
     for x in range(100):
         a_list = random.sample(range(0, list_size), list_size)
        
         from timeit import Timer
         python_sort(a_list)
         func = str(a_list) + ".sort()"    
         t3 = Timer(str(func), "from __main__ import shell_func")
         t3_list.append(t3.timeit(number=1000))
                
     seq_avg = mean(t3_list)
     print("Python Sort took {:.7f} seconds to run through {} lists, on average.".format(seq_avg, list_size))



"""TEST BASIC SORT FUNCTIONS"""    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(a_list)
print(a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
python_sort(a_list)
print(a_list)

"""TEST SORT FUNCTION RUN TIME ANALYSIS"""

if __name__ == "__main__":
    insert_sort_analyze(500)
    shell_sort_analysis(500)
    python_sort_analysis(500)
