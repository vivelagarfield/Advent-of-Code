'''
DAY 1: Report Repair

Find the two entries that sum to 2020; 
What do you get if you multiply them together?

'''

import itertools


# Naive approach
def two_sum_naive(num_arr, pair_sum):
  # search first element in the array
  for i in range(len(num_arr) - 1):
    # search other element in the array
    for j in range(i + 1, len(num_arr)):
      # if these two elemets sum to pair_sum, print the pair
      if num_arr[i] + num_arr[j] == pair_sum:
        print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")
        return(num_arr[i] * num_arr[j])



def two_sum_hashing(num_arr, pair_sum):

    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        hashTable[num_arr[i]] = num_arr[i]




if __name__ == "__main__":
    
    # load input file
    input_dir = "C:/Users/YangZh/Desktop/input.txt"
    my_file = open(input_dir, "r")
    input = my_file. readlines()
    input = [int(n) for n in input]


    # PART I
    print("PART I")
    num_arr = input
    pair_sum = 2020

    # Function call inside print
    print("Naive approach")
    answer = two_sum_naive(num_arr, pair_sum) 

    print("Optimized approach")
    two_sum_hashing(num_arr, pair_sum)

    print("Multipllied answer: ", answer)

    # PART II
    print("PART II")
    lst = []
    for subset in itertools.combinations(input, 3):
        if (sum(list(subset))) == 2020:
            if list(subset) not in lst:
                lst.append(subset)
    print("Multiplied answer: ", lst[0][0] * lst[0][1] * lst[0][2])