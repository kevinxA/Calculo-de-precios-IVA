#Kevin Aguey
#Curso 4to "B"

print("Ingrese el nombre del producto ")
Producto = input()
print("Cuantas unidades lleva ")
Unidades = int(input())
print("valor del producto ")
Valor = int(input())

Subtotal = Unidades * Valor
IVA = Subtotal * 0.19
Total = Subtotal + IVA

print("El total a pagar por",Producto,"es:", Producto)
print("El subtotal de la boleta es:", Subtotal)
print("El IVA fue",IVA)
print("El total a pagar con IVA es de",Total)