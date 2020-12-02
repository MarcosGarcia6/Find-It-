import heapq_max

lista = []
time1 = [14,21,2]#list for input validation.
food1 = ['italian','american','turkish','japanese','spanish']#list for input validation.
zone1 = ['plaza','aqueduct']#list for input validation.
price1 = [1,2,3]#list for input validation.

print('Welcome to FindIt!\nAre you hangry?\nTell us your preferences!!')

food = str(input('\nEnter kind of food you want information about (italian,american,turkish,japanese,spanish): '))
while food.lower() not in food1: #Input validation
    print('\nSorry that kind of food is not available, please try again.')
    food = str(input('\nEnter kind of food you want information about (italian,american,turkish,japanese,spanish): '))
time = int(input('\nEnter at what time you want to go (14, 21  or 2): '))

while time not in time1 : #Input validation
    print('\nSorry that time is not available, please try again.')
    time = int(input('\nEnter at what time you want to go (14, 21 or 2): '))
zone = str(input('\nEnter which zone you want the restaurant to be (plaza or aqueduct): '))

while zone.lower() not in zone1: #Input validation
    print('\nSorry that time is not available, please try again.')
    zone = str(input('\nEnter which zone you want the restaurant to be (plaza or aqueduct): '))
price = int(input('\nEnter the price range you are willing to pay (1-3) from cheap to expensive: '))

while price not in price1: #Input validation
    print('\nSorry that time is not available, please try again.')
    price = int(input('\nEnter the price range you are willing to pay (1-3) from cheap to expensive: '))

shops = {} #Create the dictionary
preferencia = {food,time, zone, price} #Save inputs on a set.
shops['king marcos'] = ( 'aqueduct', 'turkish', 'aqueduct number 9',1,21,'698745236')
shops['burger of Toni']= ('plaza','american','Plaza Mayor 5',3,14,'654123699')
shops['Pizza Roma'] = ('plaza','italian','Aqueduct number 4',3,14,'65432891')
shops['King Kebab'] = ('aqueduct','turkish','Aqueduct number 6',1,14,'632132655')
shops['Sushicatessen'] = ('plaza','japanese','Plaza number 7',3,21,'698754123')
shops['El sitio'] = ('aqueduct','spanish','aqueduct 9', 2,14,'687542139')
shops['burbuja'] = ('aqueduct','spanish','aqueduct 8', 1,2,'652145698')
shops['Maribel'] = ('aqueduct', 'spanish', 'aqueduct 6',3,21,'698541254')
shops['Pepe'] = ('plaza', 'spanish', ' plaza number 11', 2,14,'654287146')
shops['Poke'] = ( 'plaza', 'japanese', 'plaza number 22', 3, 21, '685471235')
shops['giulani'] = ( 'plaza', 'italian', 'plaza number 68', 2,14,'645872146')
shops['Fosters'] = ('aqueduct', 'american', 'aqueduct number 45',2,21,'652314785')
shops['boss kebab'] = ('plaza', 'turkish', 'plaza number 64',1,21,'654896547')
shops['Telepizza'] = ('plaza', 'italian','plaza number 56', 2, 14, '698547123')
shops['Dominos pizza']= ('plaza', 'italian', 'plaza number 57', 2,14,'659874532')
shops['Damario']= ('plaza', 'italian', 'plaza number 8', 3,14,'698547123')

shops_heap= [] #Create List so after we can convert it to heap.

for keys, condiciones in shops.items(): #Here we do a loop that will go through the dictionary. And will get the different intersections values.
    condicion = set(condiciones)
    priority = len(preferencia & condicion) #We save the lenght of the intersection.
    shop = (priority,keys)
    heapq_max.heappush_max(shops_heap, shop)

#Check the restaurants that bests fits your preferences
print('Restaurant info: ',shops[shops_heap[0][1]])
print(heapq_max.heappop_max(shops_heap)[1])
input('Press enter if you want to see the next restaurant')

#Check the next one
print('Restaurant info: ', shops[shops_heap[0][1]])
print(heapq_max.heappop_max(shops_heap)[1])
input('Press enter if you want to see the next restaurant')

#Check the next one
print('Restaurant info: ', shops[shops_heap[0][1]])
print(heapq_max.heappop_max(shops_heap)[1])
input('Press enter if you want to see the next restaurant')


#Check the next one
print('Restaurant info: ', shops[shops_heap[0][1]])
print(heapq_max.heappop_max(shops_heap)[1])
input('Press enter if you want to see the next restaurant')

#Check the next one
print('Restaurant info: ', shops[shops_heap[0][1]])
print(heapq_max.heappop_max(shops_heap)[1])
input('Press enter if you want to see the next restaurant')