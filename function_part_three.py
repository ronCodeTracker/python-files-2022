

def name_args(**key_values):
	for k in key_values.keys():
		print(f'{k}:{key_values[k]}')


name_args(name="Random", beach="Mori Point", movie="prey")


def all_true(iter):
	return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))



def any_true(iter):
	return any(iter)

print(any_true([True,True,True]))
print(any_true((True, False)))
print(any_true((False, False)))


def recursive_factorial(number):

	
  if number <= 1:
    return 1
  else:
    return number * recursive_factorial(number-1)

print(recursive_factorial(3))
print(recursive_factorial(6))






def recursive_deduplicate(my_str,i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      #no duplicate at current position, check next
      return recursive_deduplicate(my_str,i+1)
      
print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))



def recursive_reverse(str, i=0):
  #empty string case
  if len(str)==0:
    return ""
  #base case
  elif i == len(str)-1:
    return str[0]
  else:
    #recursive case
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))

