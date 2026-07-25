name = input("Hey, ¿cómo te llamas?: ")
print("Hola, " + name + "! Bienvenidx a mi juego!")

should_we_play = input("¿Quieres jugar? (sí/no): ").lower()

if (should_we_play == "sí" or should_we_play == "si"):
    print("¡Genial! Vamos a jugar.") 
    print("...")
    weapon = input("Antes de comenzar, elige un arma para tu aventura. ¿Quieres una espada o un arco? (espada/arco): ").lower()
    print("...")
    if weapon == "espada": 
        print("Has elegido la espada. ¡Preparate para la aventura!") 
    elif weapon == "arco":
        print("Has elegido el arco. ¡Preparate para la aventura!")
    else:
        print("¡Ups! Opción no válida. Se te asignará una espada por defecto.")
        weapon = "espada"

    direction = input("Estás en un bosque oscuro. ¿Quieres ir a la izquierda o a la derecha? (izquierda/derecha): ").lower()
    if direction == "izquierda":
        print("...")
        print("Decides ir a la izquierda.")
        print("...")
        bridge_choice = input("Te encuentras con un puente roto y no puedes cruzar. ¿Quieres nadar por debajo o intentar cruzarlo? (nadar/cruzar): ").lower()
        if bridge_choice == "nadar":
            print("...")
            print("Decides nadar por debajo del puente.")
            print("...")
            print("¡Felicidades! Has nadado con éxito a través del río y has llegado a un lugar seguro.")
        elif bridge_choice == "cruzar":
            print("...")
            print("Decides intentar cruzar el puente.")
            print("...")
            print("Oh no, el puente se rompe y caes al agua desmayado. ¡Fin del juego!")
    elif direction == "derecha":
        print("...")
        print("Decides ir a la derecha.")
        print("...")
        cliff_choice = input("Te encuentras con un acantilado. ¿Quieres escalarlo o buscar un camino alrededor? (escalar/caminar): ").lower()
        if cliff_choice == "escalar":
            print("...")
            print("Decides escalar el acantilado.")
            print("...")
            print("Oh no, te resbalas y caes. ¡Fin del juego!")
        elif cliff_choice == "caminar":
            print("...")
            print("Decides buscar un camino alrededor del acantilado.")
            print("...")
            print("Te pierdes en el bosque, pero finalmente encuentras un camino seguro. ¡Felicidades! Has llegado a un lugar seguro.")

    else:
        print("¡Ups! Opción no válida. Fin del juego.")

else:
    print("OK, quizás en otra ocasión...")