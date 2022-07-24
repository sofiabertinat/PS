# PS TP1
Procesamiento de señales MSE, TP1

Parte 3 - simulaciones:
  3-1
    Se  implemento el módulo signals.py, donde se definen 3 funciones que devuelven las señales de Sin, Cuadrada, y Triengular. EL correcto funcionamiento de las mismas se puede apreciar en las figuras 3_1_1, 3_1_2 y 3_1_3.
  3-2
    2_1
      En la figura 3_2_1, se muestra el resultado obtenido, estas señales no es posible diferenciarlas, hay que agregar un filtro antialiasis para no dejar que entre al sistema la señal no deseada.
    2_2
      En la figura 3_2_2, se muestra el resultado obtenido, como se observa ambas señales tienen la misma frecuencia, pero se encuentran desfasadas. Este comportamiento se debe a que .
      
 Parte 5 - CIAA
  5_1
    Dentro de la carpeta TP1_5_1 se encuentra el código en C, donde, dado q7_t a= 0x040 y q7_t b=0x23, se calcula q7_t c = a*b e imprime el resultado. Se obtuvo como resultado en decimal de c=17. 
    Con respecto al redondeo, como el resultado de a*b es de 16 bits, el método fue un corrimiento a la derecha, perdiendo la parte menos significativa, la cual no se tiene en cuenta.
 
