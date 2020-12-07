'''
DAY 2: Password Philosophy

'''

import re


def is_valid(line):
    
    # pattern to capture
    p = re.compile(r"(\d{1,2})\-(\d{1,2})(\s)([a-z])(\:\s)(.*)")
    # remove newlines
    line = re.sub("\n", "", line)
    # grouping by patterns
    m = re.match(p, line)
    groups = m.groups()
    
    # capture min, max, alphabet and password
    n_min = int(groups[0])
    n_max = int(groups[1])
    alphabet = groups[3]
    password = groups[5]
    
    # determine if password is valid
    if ((password.count(alphabet) >= n_min) & (password.count(alphabet) <= n_max)):
        return True
    else:
        return False



def is_valid_position(line):
    
    # pattern to capture
    p = re.compile(r"(\d{1,2})\-(\d{1,2})(\s)([a-z])(\:\s)(.*)")
    # remove newlines
    line = re.sub("\n", "", line)
    # grouping by patterns
    m = re.match(p, line)
    groups = m.groups()
    
    # capture positions (position - 1 = index in list)
    pos_1 = int(groups[0]) - 1
    pos_2 = int(groups[1]) - 1
    alphabet = groups[3]
    password = groups[5]
    
    # check position
    if [password[pos_1], password[pos_2]].count(alphabet) == 1:
        return True
    else: 
        return False
    


if __name__ == "__main__":
    
    # load input file
    input_dir = "C:/Users/YangZh/Desktop/input.txt"
    my_file = open(input_dir, "r")
    input = my_file. readlines()
  
    # PART I
    print("PART I")
    valid_list = [is_valid(line) for line in input]
    print("Answer: ", valid_list.count(True))

    # PART II
    print("PART II")
    valid_list = [is_valid_position(line) for line in input]
    print("Answer: ", valid_list.count(True))