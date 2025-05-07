#Aumento de poblacion
pais1 =float(20.3)
pais2 = float(18.4)
tasa_pais1 = float(0.02)
tasa_pais2 = float(0.03)
var=0
while(pais2<=pais1):
    print(f"Año",var,"La población del país 1 es:", round(pais1, 2), "La población del país 2 es:", round(pais2, 2))
    pais1 = pais1(1+tasa_pais1)
    pais2 = pais2(1+tasa_pais2)
    var= var+1
print(f"Año",var,"La población del país 1 es:", round(pais1, 2), "La población del país 2 es:", round(pais2, 2))
print(f"El país B supera la población del país A después de {var} años.")