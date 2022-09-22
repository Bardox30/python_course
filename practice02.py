print('''
*******************************************************************************
              _________
            /'        /|
           /         / |_
          /         /  //|
         /_________/  ////|
        |   _ _    | 8o////|
        | /'// )_  |   8///|
        |/ // // ) |   8o///|
        / // // //,|  /  8//|
       / // // /// | /   8//|
      / // // ///__|/    8//|
     /.(_)// /// |       8///|
    (_)' `(_)//| |       8////|___________
   (_) /_\ (_)'| |        8///////////////
   (_) \"/ (_)'|_|         8/////////////
    (_)._.(_) d' Hb         8oooooooopb'
      `(_)'  d'  H`b
            d'   `b`b
           d'     H `b
          d'      `b `b
         d'           `b
        d'             `b
*******************************************************************************
''')
print("Bienvenidos a la cripta.")
print("Tu mision es encontrar a Giomaru y hacer lo que quieras con el.")

#Write your code below this line 👇

choice1 = input('Estas a punto de cruzar la carretera. A donde decides ir? Escribe "izquierda" or "derecha" \n').lower()
if choice1 == "izquierda":
  choice2 = input('Te acercas a un lago. Hay una isla en el medio del lago. Escibe "esperar" para esperar por un bote. Escribe "nadar" para nadar hasta llegar. \n').lower()
  if choice2 == "esperar":
    choice3 = input("Llegas a la isla y encuentra un cuchillo en el suelo, lo coges por si acaso. Hay una casa con tres puertas de diferentes colores, rojo, amarillo y azul. Cual color eliges? \n").lower()
    if choice3 == "rojo":
      print("Encuentras al Giomaru de frente. El va a abrazarte y te acuchilla por la espalda. RIP.")
    elif choice3 == "amarillo":
      print("Encuentras al Giomaru de espaldas. Te acercas rapido y lo acuchillas a ese weon! Ganas el juego!")
    elif choice3 == "azul":
      print("Encuentras al Giomaru de costado. El te lanza uno de sus microfonos para noquearte. De ahi mueres porque te acuchilla. RIP.")
    else:
      print("No entraste a ninguna puerte y por eso mueres de frio. RIP.")
  else:
    print("Eres atacado por un malvado caiman y mueres. RIP.")
else:
  print("Te caes a un hoyo. RIP.")