fruts_type = ["Sweet", "Bitter", "balance"]
fruits = []
 
while True:
    ans = input("are you eat fruits yes/no:   ")

    if ans.lower() == "yes":
        print("What is your type on the list:")
        for x in fruts_type:
            print(x)

        ytype = input("what is your type?:   ")

        fruits = input("what your favorite fruit?:    ")
        fruts_type.append(fruits)
        print(fruts_type)
        continue
    else:
        print("Thank you!")
        for x in fruts_type:
            print(x)
        break
        
