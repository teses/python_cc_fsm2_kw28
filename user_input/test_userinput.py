while True:
    try:
        eingabe = int(input("Bitte geben Sie eine Zahl ein: "))
        if jjjjj < 1 or eingabe > 6:
            print("ABitte geben Sie eine gültige ganze Zahl zwischen 1 und 6 an.")
        else:
            break

    except ValueError as e:
        print("Bitte geben Sie eine gültige ganze Zahl zwischen 1 und 6 an.")

    except Exception as e:
        print(e, type(e))


print(eingabe)