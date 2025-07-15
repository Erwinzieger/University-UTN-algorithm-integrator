# las lámparas de bajo consumo cuestan $800
print('×××¡Bienvenido a Ferre Lámparas!×××\n')

lamparas_cliente = int(input('\t¿Cuantas lamparas deseas comprar?:  '))  # Toma de informacion cantidad lamparas.
lamparas_precio = 800 # Precio individual de lamparas


cantidad_total = lamparas_cliente * lamparas_precio # Cuenta: Cantidad de lámparas multiplicada por el precio de las lámparas.

# En todos los if y elif donde haya que elegir la marca, se tomara en cuenta por número o nombre de la marca. 
# Si el usuario decide escribirlo, no se tomara en cuanto si escribe tanto en minúsculas como mayúsculas o con espacio. Se tomará de todas maneras.
# Se le notificará al usuario que opción a elegido para que no haya confusiones.
# El usuario podrá saber de cuanto es el costo total sin el descuento aplicado.

if lamparas_cliente >= 11:
    precio_total = cantidad_total * 0.5
    doble_descuento = precio_total * 0.95

    print(f'''\t\n        Al comprar 6 productos o mas se obtiene un 50% de descuento, pero al llegar tambien a mas de $4000 se aplica un descuento adicional de 5% OFF.
        El precio total es de: ${doble_descuento:.0f}
            \n\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}
''')

elif lamparas_cliente == 6 or lamparas_cliente == 7 or lamparas_cliente == 8 or lamparas_cliente == 9 or lamparas_cliente == 10 :   
    precio_total = cantidad_total * 0.5
    print(f'\tAl comprar 6 o mas se obtiene un 50% de descuento. El precio total es de: ${precio_total:.0f}')
    print(f'\n\tEl precio sin el descuento es de ${lamparas_precio * lamparas_cliente}')
    
elif lamparas_cliente == 5: 
    marca_lampara = input('\t¿Qué marca desea comprar? Ingrese numero o escriba (1- ArgentinaLuz / 2- Otra Marca): ')
    if marca_lampara == '1' or marca_lampara.lower().replace(' ', '') == 'argentinaluz': 
        precio_total = cantidad_total * 0.6
        print(f'\t\tUsted selecciono [1- ArgentinaLuz]. Se aplicó un 40% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

    elif marca_lampara == '2' or marca_lampara.lower().replace(' ', '') == 'otramarca':
        precio_total = cantidad_total * 0.7
        print(f'\t\tUsted selecciono [2- Otra Marca]. Se aplicó un 30% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')


elif lamparas_cliente == 4:
    marca_lampara = input('\t¿Qué marca desea comprar? Ingrese numero o escriba (1- ArgentinaLuz / 2- FelipeLamparas / 3- Otra Marca): ')
    if marca_lampara == '1' or marca_lampara.lower().replace(' ', '') == 'argentinaluz':
        precio_total = cantidad_total * 0.75
        print(f'\t\tUsted selecciono [1- ArgentinaLuz]. Se aplico un 25% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

    elif marca_lampara == '2' or marca_lampara.lower().replace(' ', '') == 'felipelamparas':
        precio_total = cantidad_total * 0.75
        print(f'\t\tUsted selecciono [2- FelipeLamparas]. Se aplico un 25% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

    elif marca_lampara == '3' or marca_lampara.lower().replace(' ', '') == 'otramarca':
        precio_total = cantidad_total * 0.80
        print(f'\t\tUsted selecciono [3- Otra Marca]. Se aplico un 20% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

elif lamparas_cliente == 3:
    marca_lampara = input('\t¿Qué marca desea comprar? Ingrese numero o escriba (1- ArgentinaLuz / 2- FelipeLamparas / 3- Otra Marca): ')
    if marca_lampara == '1' or marca_lampara.lower().replace(' ', '') == 'argentinaluz':
        precio_total = cantidad_total * 0.85
        print(f'\t\tUsted selecciono [1- ArgentinaLuz]. Se aplico un 15% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

    elif marca_lampara == '2' or marca_lampara.lower().replace(' ', '') == 'felipelamparas':
        precio_total = cantidad_total * 0.90
        print(f'\t\tUsted selecciono [2- FelipeLamparas]. Se aplico un 10% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

    elif marca_lampara == '3' or marca_lampara.lower().replace(' ', '') == 'otramarca':
        precio_total = cantidad_total * 0.95
        print(f'\t\tUsted selecciono [3- Otra Marca]. Se aplico un 5% de descuento. El precio total es de: ${precio_total:.0f}')
        print(f'\n\t\tEl precio sin el descuento es de: ${lamparas_precio * lamparas_cliente}')

elif lamparas_cliente == 2:
    print(f'\n\tUsted agregó 2 productos. El precio total es de: ${cantidad_total} ')

elif lamparas_cliente == 1:
    print(f'\n\tUsted agregó 1 producto. El precio total es de: ${cantidad_total} ')