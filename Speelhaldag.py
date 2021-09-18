personen = int(input('Hoeveel personen? '))
toegangticket = int(input('Hoeveel kost een enkele toegangsticket in centen? '))
bedragper5minuten = int(input('hoeveel is het bedrag per 5 minuten in centen om gebruik te maken van de VR-bril? '))
aantalkeer = int(input('hoeveel vaak moet je dan dat bedrag betalen om 45 minuten gebruik te kunnen maken? '))

saldo = personen * (toegangticket + bedragper5minuten * aantalkeer)

print('Dit geweldige dagje-uit met ' + str(personen) + ' mensen in de Speelhal voor 45 minuten VR kost je maar ' + str(saldo) + ' cent')