from MyModule import *

while True:
    print("Valikud:")
    print("1. Registreeri")
    print("2. Sisselogimine")
    print("3. Välju")
    valik = input("Vali: (1-4): ")

    if valik == '1':
        register()  
    elif valik == '2':
        login()      
    elif valik == '3':
        print("Head aega!")
        break
    else:
        print("Vale valik, proovi uuesti.")
        
