#estrategia de descuento segun el valor de la compra
valor_compra=0
descuento=0
balota=0
valor_compra=int (input ("Digite el valor de la variable valor_compra:"))
color_balota=input("ingrese el valor de la balota")
if valor_compra>=50000 and color_balota=="roja":
    
    descuento=valor_compra (valor_compra*0.1)
    print(f"sacaste la balota roja el valor de la compra es {valor_compra} el total a pagar {descuento}")
elif valor_compra>=50000 and color_balota=="verde":
    decuento=valor_compra-(valor_compra*0.015)
    print(f"sacaste la balota verde el valor de la compra es {valor_compra} el total a pagar {descuento}")
elif valor_compra>=50000 and color_balota=="azul":
    descuento=valor_compra-(valor_compra*0.2)
    print(f"sacaste la balota azul el valor de la compra es {valor_compra} el total a pagar {descuento}")
elif valor_compra>=50000 and color_balota=="amarrillo":
    descuento=valor_compra-(valor_compra*0.5)
    print(f"sacaste la balota amarillo el valor de la compra es {valor_compra} el total a pagar {descuento}")
elif valor_compra>=50000 and color_balota=="negro":
    descuento=valor_compra-(valor_compra*1)
    print(f"sacaste la balota negra el valor de la compra es {valor_compra} el total a pagar {descuento}")
elif valor_compra<50000:
    print(f"no participas en el sorteo total a pagar {valor_compra}")