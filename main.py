shops = {}

shops[1]= ('burger of Toni','plaza','american','Plaza Mayor 5',3,12,22,'654123699')
shops[2] = ('Pizza Roma','plaza','italian','Aqueduct number 4',3,11,22,'65432891')
shops[3] = ('King Kebab','aqueduct','turkish','Aqueduct number 6',1,9,22,'632132655')
shops[4] = ('Sushicatessen','plaza','japanese','Plaza number 7',3,12,23,'698754123')
shops[5] = ('El sitio','aqueduct','spanish','aqueduct 9', 2,7,24,'687542139')
shops[6] = ('burbuja', 'aqueduct','spanish','aqueduct 8', 1,8,23,'652145698')
shops[7] = ('Maribel', 'aqueduct', 'spanish', 'aqueduct 6',3,13,22,'698541254')
shops[8] = ('Pepe', 'plaza', 'spanish', ' plaza number 11', 2,14,23,'654287146')
shops[9] = ('Poke', 'plaza', 'japanese', 'plaza number 22', 3, 11,21, '685471235')
shops[10] = ('giulani', 'plaza', 'italian', 'plaza number 68', 2,12,22,'645872146')
shops[11] = ('Fosters', 'aqueduct', 'american', 'aqueduct number 45',2,13,22,'652314785')
shops[12] = ('boss kebab', 'plaza', 'turkish', 'plaza number 64',1,9,22,'654896547')
shops[13] = ('Telepizza', 'plaza', 'italian','plaza number 56', 2, 13,20, '698547123')
shops[14]= ('Dominos pizza', 'plaza', 'italian', 'plaza number 57', 2,14,22,'659874532')
shops[15]= ('Damario','plaza', 'italian', 'plaza number 8', 3,12,22,'698547123')
def choose():
    preferences  = int(input('Enter 1 if you want to set any preferences or 2 if you just want information about a kind of restaurants: '))
    if preferences == 2:
        inp1 = str(input('Enter kind of food you want information about (italian,american,turkish,japanese,spanish): '))
        if inp1.lower() == 'italian':
            for keys, value in shops.items():
                if value[2] == 'italian':
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
        if inp1.lower() == 'american':
            for keys, value in shops.items():
                if value[2] == 'american':
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
        if inp1.lower() == 'turkish':
            for keys, value in shops.items():
                if value[2] == 'turkish':
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
        if inp1.lower() == 'japanese':
            for keys, value in shops.items():
                if value[2] == 'japanese':
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
        if inp1.lower() == 'spanish':
            for keys, value in shops.items():
                if value[2] == 'spanish':
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
    if preferences == 1:
        option = str(input('Insert your preference(Open, Price, Location): '))
        if option.lower() == 'open':
            time = int(input('Enter time in 24 hours terms when you want to go: '))
            print()
            print('the following shops are open: ')
            print()
            for keys, value in shops.items():
                if time > value[5] and time < value[6]:
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()

        if option.lower() == 'price':
            precio = int(input('How much willing to pay(scale 1 to 3): '))
            for keys, value in shops.items():
                if precio >= value[4]:
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()
        if option.lower() == 'location':
            locali = str(input('Which zone do you prefer(aqueduct or plaza): '))
            print()
            print('the following shops are open: ')
            print()
            for keys, value in shops.items():
                if locali == value[1]:
                    print()
                    print('The name of the shop is', value[0])
                    print('The zone is located in: ', value[1])
                    print('The type of food is: ', value[2])
                    print('The location of the shop is: ', value[3])
                    print('The price is', value[4], 'from a scale from 1 to 3')
                    print('The shop opens at ', value[5])
                    print('The shop closes at ', value[6])
                    print('The phone number is ', value[7])
                    print()

choose()