# name:  Ronald Kiefer
# hebrew:  ר ו נ  א ל ד
# date: June 13, 2022 Monday
# description:  list comprehensions bootcamp python



list_one = [('English', 88), ('Science', 90), 
            ('Math', 97), ('Social Science', 82)]

print_one = sorted(list_one, key =  lambda list_one: list_one[1])

print(print_one)


list = [3, 6, 9, 2]

print_two = lambda list: [i**3 for i in list]  

print(print_two(list))


lambda_one = lambda num:True if  num % 2 == 0 else  False
print([lambda_one(x) for x in [3, 6, 9, 2]])

list_two = []
[list_two.append(i) for i in range(1 , 101)]

print(list_two)

sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})


