def count(fileName, letter):
    file = open(fileName, "r")
    text = file.read()
    count = 0
    for char in text:
       if char == letter:
           count += 1
    return count
x_szama = count('count-x-y-w.txt','X')
y_szama = count('count-x-y-w.txt','Y') 
w_szama = count('count-x-y-w.txt','W')

print(x_szama + y_szama - w_szama)         