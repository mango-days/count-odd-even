# Count number of even and odd elements in an array
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
index2 = len ( numbers ) - 1
index1 = 0
while index1 < index2 :
    if numbers [ index1 ] % 2 == 1 : index1 += 1
    elif numbers [ index2 ] % 2 == 0 : index2 -= 1
    elif ( numbers [ index1 ] % 2 == 0 and numbers [ index2 ] % 2 == 1 ) :
        temp = numbers [ index1 ] 
        numbers [ index1 ] = numbers [ index2 ] 
        numbers [ index2 ] = temp
        index1 += 1
        index2 -= 1
print ( index1 , "odd numbers")
print ( index2 , "even numbers")