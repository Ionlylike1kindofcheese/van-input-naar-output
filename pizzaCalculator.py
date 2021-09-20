# Robin Vervoorn. opdracht: Pizza Calculator

smallprize = 6.95
mediumprize = 11.50
largeprize = 15.50
smallammout = int(input("Hoeveel kleine pizza's wilt u hebben? "))
mediumammout = int(input("Hoeveel medium pizza's wilt u hebben? "))
largeammout = int(input("Hoeveel large pizza's wilt u hebben? "))

pizzaprijs = (smallprize * smallammout) + (mediumprize * mediumammout) + (largeprize * largeammout)

print("De prijs voor " + str(smallammout) + " kleine pizza's, " + str(mediumammout) + " medium pizza's en " + str(largeammout) + " large pizza's is in totaal " + str(pizzaprijs) + " euro.")