croissant = int(input('Hoeveel croissants? '))
stokbrood = int(input('Hoeveel stokbroden? '))
kortingbonnen = int(input('hoeveel kortingsbonnen van 50 cent? '))

saldo = (croissant * 39) + (stokbrood * 278) - (kortingbonnen * 50)


print('De feestlunch kost je bij de bakker ' + str(saldo) + ' cent voor de ' + str(croissant) + ' croissantjes en de ' + str(stokbrood) + ' stokbroden als de ' + str(kortingbonnen) + ' kortingsbonnen nog geldig zijn!')