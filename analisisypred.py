import numpy as np
import pandas as pd
def cargar_datos(ruta_archivo):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=str) # faltaba el dtype para que conservara los valores del string
    return datos

if __name__ == "__main__":
    ruta_archivo = "C:\\Users\\Juan\\Downloads\\retail_sales_dataset.csv"
    datos = cargar_datos(ruta_archivo)
    print(datos)
    
sales=cargar_datos("C:\\Users\\Juan\\Downloads\\retail_sales_dataset.csv")

#orden datos
#Transaction ID
#Date
#Customer ID
#Gender
#Age
#Product Category
#Quantity
#Price per Unit
#Total Amount

print(np.shape(sales))
print(np.ndim(sales))

#poner los datos en formato float o int ya que al cargarlos estaban en str  

Trans_ID=sales[0:,0]
Date=sales[0:,1]
Customer_ID=sales[0:,2]
Gender=sales[0:,3]
Age=sales[0:,4]
productos=sales[0:, 5]
cantidades= sales[0:,6].astype(float)
precio=sales[0:,7].astype(float)
Monto=sales[0:,8].astype(float)

#Calcula el total de ventas por producto y por tienda, creo que no hay datos de las tiendas solo de los distintos productos

productos_unicos = np.unique(productos)
total_ventas_producto = {}
for producto in productos_unicos:
    suma_ventas = np.sum(cantidades[productos == producto])

    total_ventas_producto[producto] = suma_ventas

for producto, total in total_ventas_producto.items():
    print(f"Producto: {producto}, Total Vendido: {total}")


#Calcula el promedio de ventas diarias por producto y por tienda.
productos_unicos = np.unique(productos)
promedio_ventas_producto = {}
for producto in productos_unicos:
    prmdio_ventas = np.mean(cantidades[productos == producto])

    promedio_ventas_producto[producto] = prmdio_ventas

for producto, total in promedio_ventas_producto.items():
    print(f"Producto: {producto}, Promedio Vendido: {total}")
        

#Identifica los productos y tiendas con mayores y menores ventas.
print(total_ventas_producto)
producto_maximo= max(total_ventas_producto, key=total_ventas_producto.get)
      
valor_max=total_ventas_producto[producto_maximo]
print(valor_max)


producto_minimo= min(total_ventas_producto, key=total_ventas_producto.get)
      
valor_min=total_ventas_producto[producto_minimo]
print(valor_min)

