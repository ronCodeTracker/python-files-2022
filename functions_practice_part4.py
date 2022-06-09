



def max_num(num_one, num_two, num_three):
    num_high = 0
    if num_one > num_two:
        num_high = num_one
    else: 
        num_high = num_two
    if num_high < num_three:
        num_high = num_three
    print(num_high)

max_num(4, 7, 66)



def mult_list(list_one):
    add_one = 0
    increment_one = 0
    print(list_one)
    for n in list_one:
        increment_one += 1
        if increment_one == 1:
             add_one = n
        else:
             add_one *= n
    print(add_one)

mult_list([3,2,2])




def rev_string(string_one):
    if len(string_one) == 0:

       return string_one 

    else:

       return rev_string(string_one[1:]) + string_one[0]


print("Reverse: ", rev_string("seven seven seven nine nine nine"))


def num_within(number, beg_range, end_range):
    bool_one = False
    for n in range(beg_range, end_range  + 1):
        #print(n)
        if number == n:
            bool_one = True
    print(bool_one)


num_within(3,2,4)
num_within(3,1,3)
num_within(10, 2, 5)
            


         
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)



