def figure(n):
    for j in range(n):
        print((j+1)*"#")
    print()
    for i in range(n):
        print((n-i)*"#")
    print()
    for É in range(n):
        print(É*".",(n-É)*"#")
    print()
    print(n * "#")
    for w in range(n-2):
         #print("#", (n-2)*".", "#")
        print("#{}#".format((n-2)*"."))
    print(n * "#")




figure(30)