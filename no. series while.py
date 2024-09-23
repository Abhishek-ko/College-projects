
s = int(input("Enter starting point: "))
e = int(input("Enter ending point: "))
u = int(input("Enter updation point: "))
f = input("Enter 'v' for vertical and 'h' for horizontal: ")
o = input("Enter 'r' for reverse and 'f' for forward: ")
b = int(input("Enter a break number: "))
n = int(input("Enter a continue number: "))


if u == 0:
    print("Updation point cannot be zero!")
else:
    
    if o == "r":
        if s > e:  
            for i in range(s, e-1, -u):
                if i == n:
                    continue  
                if i == b:
                    break  
                if f == "h":
                    print(i, end=", ")
                elif f == "v":
                    print(i)
        else:
            print("Error: For reverse order, starting point must be greater than ending point.")

    
    elif o == "f":
        if s < e:  
            for i in range(s, e+1, u):
                if i == n:
                    continue  
                if i == b:
                    break  
                if f == "h":
                    print(i, end=", ")
                elif f == "v":
                    print(i)
        else:
            print("Error: For forward order, starting point must be less than ending point.")
