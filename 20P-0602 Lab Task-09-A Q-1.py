a = [1,3,5]
print ('a =',a)

b = [2,4,6]
print ('b =',b)
# we add a and b for c
c = a + b   #In this we can add the contaginate the strings and make them into one string 
print ('c =',c)
# We Calculate the mean
total = 0   #In this code we take a total and counter and in start take them equal to zero
counter = 0 #Then we take each element of c one by one and also keep the counter which tells us how many element the c has
for i in c:
    total = total + i  
    counter = counter + 1
Mean = total / counter     #Then we calculate the mean by dividing the total with the counter and print the mean
print ("Find the average/mean value from list c =",Mean)
# We 42 in c at index 3 
c.insert(3,42) #this will put the number 42 on the four index and move the rest in front the first number is the index and second is the number
print ('Insert fourth element in list c 42 =',c)
# We append 7,8,9 in the c
n = [7,8,9]       # In this we take three numbers and with the help of for loop we append the numbers in c one by one
for i in n:
    c.append(i)
print ('Append 7, 8 and 9 to the end of c =',c)
# We print the first two elements
print ('The first two values of list c are =',c[0:2]) # this will give us the values of 0 and 1 index we give 2  [0:2] because it always stops one number before
# We print the last element
print ('The Last value of list b is =',b[-1])  # we give -1 because the last index of every list is -1
# We Calculate the length of list 
counter = 0   #In this we take the counter in starting 0
for i in a:   #It will take all the elements of a and put them equal to i until all the elements in the list are finished
    counter = counter + 1   #This will add 1 each time one element is put equal to i  
print ("The length of list a is : ", str(counter))  #this will print the number of times the i is equaled to a element and it will give the number of elements of a