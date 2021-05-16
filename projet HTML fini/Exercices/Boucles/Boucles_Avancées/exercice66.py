def tables():
    for i in range(10):
        print("Table de",i+1,": ")
        for j in range(10):
            print(i+1,"x",j+1, "=", (i+1)*(j+1))
tables()