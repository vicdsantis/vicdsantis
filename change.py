def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:")
    print(f"{expense}")
    print(f"Dinero recibido")
    print(f"{money}\n")
    print(f"{"Vuelto"}\n")
    print(f"{"Pesos:"}\n")
    print(f"{int(money - expense)}")
    print(f"Centavos:")
    print(f"{int(money % expense)**2}")
