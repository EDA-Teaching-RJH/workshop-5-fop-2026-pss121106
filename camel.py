camel_case = input("camelcase:")
print("snake_case:", end="")
for char in camel_case:
    if char.isupper():
        print("_" + char.lower() , end="")
    else:
        print(char,end="")

if __name__ =="_main_":
    main()