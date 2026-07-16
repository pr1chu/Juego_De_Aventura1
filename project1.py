name = input("Hey, ¿cómo te llamas?: ")
print("Hola, " + name + "! Bienvenidx a mi juego!")

should_we_play = input("¿Quieres jugar? (sí/no): ").lower()

if (should_we_play == "sí" or should_we_play == "si" or should_we_play == "yes"):
    print("¡Genial! Vamos a jugar.")
else:
    print("OK, quizás en otra ocasión...")