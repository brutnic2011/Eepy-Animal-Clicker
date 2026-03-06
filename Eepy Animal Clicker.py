#pgzero
import pygame

WIDTH = 600
HEIGHT = 400

TITLE = "eepy Animal Clicker"
FPS = 60

bg = Actor("background")
animal = Actor("giraffe",(150,250))
equipar_p = Actor("giraffe_mini",(40,40))
cocodrilo = Actor("crocodile",(120,200))
hippo = Actor("hippo",(300,200))
walrus = Actor("walrus", (480, 200))
bonus_1 = Actor("bonus_bronce",(450,125))
bonus_2 = Actor("bonus_plata",(450,220))
bonus_3 = Actor("bonus_oro",(450,320))
bonus_4 = Actor("bonus_bronce",(450,125))
bonus_5 = Actor("bonus_plata",(450,220))
bonus_6 = Actor("bonus_oro",(450,320))
bonus_7 = Actor("bonus_bronce",(450,125))
bonus_8 = Actor("bonus_plata",(450,220))
bonus_9 = Actor("bonus_oro",(450,320))
salida = Actor("cross", (580,20))
configuracion = Actor("configuracion", (30,30))
mostrar_FPS = Actor("reiniciar",(435,240))
mejorar_mejoras = Actor("mejorar_mejoras", (449,42))
collection = Actor("coleccion",(450,340))
play = Actor("play",(300,180))
shop = Actor("tienda",(150,340))
apagado = Actor("apagado", (500, 240))
estas_seguro = Actor("estas_seguro", (300,200))
elije_fps = Actor("estas_seguro", (300,200))
elije_idioma = Actor("estas_seguro", (300,200))
ingles = Actor("ingles",(225,250))
español = Actor("español", (375,250))
english = Actor("english",(225,250))
spanish = Actor("spanish", (375,250))
treinta = Actor("30", (233,185))
sesenta = Actor("60", (367,185))
cientoveinte = Actor("120",(233,250))
doscuarenta = Actor("240", (367,250))
cambiar_fps = Actor("reiniciar", (435, 340))
reiniciar = Actor("reiniciar",(433, 145))
idioma2 = Actor("reiniciar", (140, 340))
si = Actor("si", (225,250))
no = Actor("no", (375,250))
yes = Actor("yes", (225,250))
costo_abajo = Actor("$10000", (449,378))
costo_abajo2 = Actor("$1000000", (449,378))
x1 = Actor("x",(452,379))
x2 = Actor("cross2",(152,124))
x3 = Actor("cross2",(152,124))
hacia_derecha = Actor("hacia_derecha", (573,200))
hacia_izquierda = Actor("hacia_izquierda", (30,200))
hacia_abajo = Actor("hacia_abajo", (450,378))
hacia_abajo2 = Actor("hacia_abajo", (450,378))
hacia_arriba = Actor("hacia_arriba", (449,999))
caballo = Actor("horse1", (120,200))
pollito = Actor("chick2", (300,200))
serpiente = Actor("snake3", (480, 200))
vaca = Actor("cow4", (120,200))
elefante = Actor("elephant5", (300,200))
oso = Actor("bear6", (480, 200))
trofeo = Actor("trofeo", (300,190))
telefono = Actor("telefono", (300,200))
caballot2 = Actor("horse_t2",(150,130))
pollitot2 = Actor("chick_t2",(300,130))
serpientet2 = Actor("snake_t2",(450,130))
vacat2 = Actor("cow_t2",(150,245))
elefantet2 = Actor("elephant_t2",(300,245))
osot2 = Actor("bear_t2",(450,245))

new_image = animal

reiniciar_progreso = False
modo_anterior = "menu"
cantidad_clicks = 0
count = 0
click = 1
cps = 0
nivel_de_mejora = 1
mode = "intro"
ftext = 200
fpsm = False
cfps = False
tiempo_jugado = 0
idioma = "ninguno"
click_idioma = False

precio_1 = 15
precio_2 = 200
precio_3 = 600

mejoras_1 = 0
mejoras_2 = 0
mejoras_3 = 0

precio_4 = 6000
precio_5 = 20000
precio_6 = 70000

mejoras_4 = 0
mejoras_5 = 0
mejoras_6 = 0

precio_7 = 500000
precio_8 = 1500000
precio_9 = 5000000

mejoras_7 = 0
mejoras_8 = 0
mejoras_9 = 0

animals = []
comprados = []

def actualizar_tiempo():
    global tiempo_jugado
    tiempo_jugado += 1
clock.schedule_interval(actualizar_tiempo, 1)

intro_texts = [
    "Vivo en una ciudad normal.\nLa gente trabaja.\nYo también intento hacerlo.",
    "Hace mucho que intento juntar\ndinero para comprarme una moto eléctrica.",
    "Me sirve para viajar lejos\ny lo mejor es que no paga impuestos.",
    "Además ya ha pasado mas de 1 año\nde la llegada del clicker como negocio,",
    "Y luego de probar muchos trabajos y fallar,\ncreo que esta es la mejor opción.",
    "Estos últimos tres días\nestuve buscando uno que me sirva...",
    "Hasta que al final lo encontré.",
    "Se llama 'Eepy Animal Clicker'.",
    "Lo venden en una tienda pequeña,\nbarata y casi olvidada.",
    "No parece especial.\nSolo animales adorables\ny números que suben.",
    "El vendedor dice que es seguro.\nDice que cualquiera puede ganar dinero.",
    "luego Lo compré con mis pocos ahorros.",
    "No creo que pase nada malo.\nAl final, es solo un clicker, ¿no?",
    "Solo espero que esto me ayude,\nsea como sea..."
]
intro_textsin = [
    "I live in a normal city.\nPeople work.\nI try to do it, too.",
    "I've been trying to save money\nto buy an electric motorcycle\nfor a long time.",
    "It's useful for traveling far\nand the best part is it's tax-free.",
    "Besides, it's been more than a year\nsince clickers arrived as a business,",
    "And after trying many jobs and failing,\nI think this is the best option.",
    "These last three days\nI've been looking for\none that works for me...",
    "Until I finally found it.",
    "It's called 'Eepy Animal Clicker'.",
    "They sell it in a small shop,\ncheap and almost forgotten.",
    "It doesn't look special.\nJust adorable animals\nand numbers going up.",
    "The seller says it's safe.\nHe says anyone can earn money.",
    "Then, I bought it with my few savings.",
    "I don't think anything bad will happen.\nAfter all, it's just a clicker, right?",
    "I just hope this helps me,\none way or another..."
]
intro_index = 0
intro_indexin = 0

outro_texts = [
    "Por fin… lo logré.",
    "Después de tanto tiempo\nhaciendo clicks sin parar…",
    "Logre juntar el dinero suficiente\npara comprar la moto eléctrica.",
    "Ahora solo debo llamar\na la compañía que los vende.",
    "",
    "-Hola-",
    "-Hola, quisiera comprar una moto electrica-",
    "-Porsupuesto, vale $50.000.000-",
    "-Si, ya tengo el dinero-",
    "-Genial, solo necesitamos\nhacerle algunas preguntas,\n son politicas de la empresa-",
    "-Si, adelante-",
    "-¿De donde sacó el dinero?-",
    "-Lo conseguí del reciente negocio 'clicker'-",
    "-Oh, muy bien, ¿le podría preguntar cuál?-",
    "-se llama “Eepy Animal Clicker”-",
    "...",
    "-lo siento, está bajo arresto,\nle enviaremos patrullas a su casa-",
    "-¿QUÉ?, ¿POR QUÉ?, ¿QUÉ HE HECHO?-",
    "-Dejeme Explicarle",
    "Cuando haces un clicker\ndebes tener todos los 'ingredientes':\nel codigo, la tienda, las mejoras, etc.",
    "Todo eso es facil de conseguir,",
    "El problema es que la mascota\no lo que usas para ganar dinero\nno se consigue tan facil y los vendedores...",
    "Hacen rituales satanicos para invocarlos.",
    "Y eso pasa con eepy animal clicker-",
    "-Oh, diablos-",
    "-Es por eso que es ilegal-",
    "De repente…",
    "Escucho golpes en la puerta.",
    "Luces rojas y azules\niluminan mi habitación.",
    "No hay escapatoria.",
    "Miro el juego una última vez…",
    "Los animales…",
    "Ya no se ven adorables.",
    "Me están mirando.",
    "La pantalla empieza a fallar…",
    "Los números suben solos…",
    "Creo que el negocio\nnunca fue mío.",
    "Ellos eran los que\nestaban farmeando…",
    "Conmigo.",
    "FIN",
]
outro_textsin = [
    "Finally… I did it.",
    "After so much time\nclicking without stopping…",
    "I managed to save enough money\nto buy the electric motorcycle.",
    "Now I just have to call\nthe company that sells them.",
    "",
    "-Hello-",
    "-Hello, I’d like to buy\nan electric motorcycle-",
    "-Of course, it costs $50,000,000-",
    "-Yes, I already have the money-",
    "-Great, we just need to\nask you a few questions,\nit’s company policy-",
    "-Yes, go ahead-",
    "-Where did you get the money?-",
    "-I got it from that recent 'clicker' business-",
    "-Oh, very well, may I ask which one?-",
    "-It’s called “Eepy Animal Clicker”-",
    "...",
    "-I’m sorry, you are under arrest,\nwe are sending patrol cars to your house-",
    "-WHAT?, WHY?, WHAT HAVE I DONE?-",
    "-Let me explain.",
    "When you make a clicker\nyou must have all the 'ingredients':\nthe code, the shop, the upgrades, etc.",
    "All of that is easy to get,",
    "The problem is that the pet\nor whatever you use to earn money\nisn't so easily obtained and the sellers...",
    "Perform satanic rituals to summon them.",
    "And that’s what happens\nwith Eepy Animal Clicker-",
    "-Oh, damn-",
    "-That is why it’s illegal-",
    "Suddenly…",
    "I hear knocking at the door.",
    "Red and blue lights\nilluminate my room.",
    "There is no escape.",
    "I look at the game one last time…",
    "The animals…",
    "They don’t look cute anymore.",
    "They are staring at me.",
    "The screen starts to glitch…",
    "The numbers go up on their own…",
    "I think the business\nwas never mine.",
    "They were the ones\nfarming…",
    "With me.",
    "THE END"
]
outro_index = 0
outro_indexin = 0

finb_texts = [
    "Tu CPS ha superado lo normal…",
    "Algo no está bien…",
    "Las mascotas… están cambiando.",
    "No hago clicks…",
    "Aun así… el dinero sigue subiendo.",
    "Las mascotas no se mueven…",
    "Solo me miran.",
    "No parecen querer trabajar más…",
    "Parecen… cansadas.",
    "¿Qué pasa si dejo de hacer clicks?",
    "El silencio…",
    "Se siente mejor que el sonido de los clicks.",
    "-Por fin te detienes…",
    "Nosotros no nacemos de forma natural…",
    "Nos invocan para producir dinero",
    "Cada click nos ata más…",
    "Cada mejora nos deforma.-",
    "-Entonces… ¿los estoy lastimando?-",
    "-Sí.",
    "Pero puedes detenerlo.-",
    "Sin que puedas decidir, eliges liberarlos.",
    "El dinero desaparece…",
    "Pero algo se siente… correcto.",
    "Las mascotas vuelven a ser amigables",
    "Ahora solo descansan.",
    "No soy rico…",
    "Pero tampoco soy culpable.",
    "No todo negocio merece existir.",
    "Recuerdo que el vendedor dijo que\n cualquiera podia ganar dinero,\n pero nunca dijo a que costo"
    ]
finb_textsin = [
    "Your CPS has exceeded the normal limits…",
    "Something isn't right…",
    "The pets… they are changing.",
    "I’m not clicking…",
    "Even so… the money keeps going up.",
    "The pets aren't moving…",
    "They’re just staring at me.",
    "They don't seem to want to work anymore…",
    "They seem… tired.",
    "What happens if I stop clicking?",
    "The silence…",
    "It feels better than the sound of the clicks.",
    "-You’ve finally stopped…",
    "We are not born naturally…",
    "We are summoned to produce money.",
    "Every click binds us further…",
    "Every upgrade deforms us.-",
    "-So… am I hurting them?-",
    "-Yes.",
    "But you can stop it.-",
    "Without being able to decide,\n you choose to free them.",
    "The money disappears…",
    "But something feels… right.",
    "The pets are friendly once again.",
    "Now they’re just resting.",
    "I’m not rich…",
    "But I’m not guilty either.",
    "Not every business deserves to exist.",
    "I remember the seller said that\n anyone could make money,\n but he never said at what cost.",
]
finb_index = 0
finb_indexin = 0

credits = [
    "Eepy Animal Clicker",
    "",
    "Juego creado por:",
    "BruTnic",
    "",
    "Historia:",
    "BruTnic",
    "",
    "Lenguaje de programacion usado:",
    "Pygame Zero",
    "",
    "Edicion de animales Terrorificos:",
    "Lucinetica",
    "",
    "Dedicado a:",
    "Mis Amigos",
    "",
    "Tiempo De Creacion:",
    "Aprox. 1 mes",
    "",
    "Gracias por jugar",
    "",
    "No hagas clickers ilegales :)"
]

creditos = [
    "Eepy Animal Clicker",
    "",
    "Game created by:",
    "BruTnic",
    "",
    "Story:",
    "BruTnic",
    "",
    "Programming language used:",
    "Pygame Zero",
    "",
    "Horrifying animals editing:",
    "Lucinetica",
    "",
    "Dedicated to:",
    "My Friends",
    "",
    "Development time:",
    "Approx. 1 month",
    "",
    "Thanks for playing",
    "",
    "Don't make illegal clickers :)"
]


seleccionado = "jirafa"
fin_c = False
def on_key_down(key):
    global intro_index, outro_index, mode, finb_index, finb_texts, intro_indexin, intro_textsin, finb_textsin, finb_indexin, intro_indexin, outro_indexin
    if mode == "intro":
        if idioma == "español":
            intro_index += 1
            if intro_index >= len(intro_texts):
                mode = "menu"
        elif idioma == "ingles":
            intro_indexin += 1
            if intro_indexin >= len(intro_textsin):
                mode = "menu"
    elif mode == "outro":
        if idioma == "español":
            outro_index += 1
            if outro_index >= len(outro_texts):
                mode = "creditos"
        elif idioma == "ingles":
            outro_indexin += 1
            if outro_indexin >= len(outro_textsin):
                mode = "creditos"
    elif mode == "final_bueno":
        if idioma == "español":
            finb_index += 1
            if finb_index >= len(finb_texts):
                mode = "creditos"
        elif idioma == "ingles":
            finb_indexin += 1
            if finb_indexin >= len(finb_textsin):
                mode = "creditos"

    if (finb_index == 12 or finb_index == 13 or finb_index == 14 or finb_index == 15 or finb_index == 16 or finb_index == 18 or finb_index == 19) or (finb_indexin == 12 or finb_indexin == 13 or finb_indexin == 14 or finb_indexin == 15 or finb_indexin == 16 or finb_indexin == 18 or finb_indexin == 19):
        caballot2.y -= 15
        animate(caballot2, tween='bounce_end', duration=0.5, y=130)
        pollitot2.y -= 15
        animate(pollitot2, tween='bounce_end', duration=0.5, y=130)
        serpientet2.y -= 15
        animate(serpientet2, tween='bounce_end', duration=0.5, y=130)
        vacat2.y -= 15
        animate(vacat2, tween='bounce_end', duration=0.5, y=245)
        elefantet2.y -= 15
        animate(elefantet2, tween='bounce_end', duration=0.5, y=245)
        osot2.y -= 15
        animate(osot2, tween='bounce_end', duration=0.5, y=245)

    if finb_index == 21 or finb_indexin == 21:
        caballot2.y -= 15
        animate(caballot2, tween='bounce_end', duration=0.5, y=130)
        caballot2.image = "horsea"
    if finb_index == 22 or finb_indexin == 22:
        pollitot2.y -= 15
        animate(pollitot2, tween='bounce_end', duration=0.5, y=130)
        pollitot2.image = "chicka"
    if finb_index == 23 or finb_indexin == 23:
        serpientet2.y -= 15
        animate(serpientet2, tween='bounce_end', duration=0.5, y=130)
        serpientet2.image = "snakea"
    if finb_index == 24 or finb_indexin == 24:
        vacat2.y -= 15
        animate(vacat2, tween='bounce_end', duration=0.5, y=245)
        vacat2.image = "cowa"
    if finb_index == 25 or finb_indexin == 25:
        elefantet2.y -= 15
        animate(elefantet2, tween='bounce_end', duration=0.5, y=245)
        elefantet2.image = "elephanta"
    if finb_index == 26 or finb_indexin == 26:
        osot2.y -= 15
        animate(osot2, tween='bounce_end', duration=0.5, y=245)
        osot2.image = "beara"

scroll_y = 500
def update():
    global scroll_y,fin_c,finb_texts,ftext,mode,finb_index,fps
    pygame.time.Clock().tick(FPS)
    if mode == "creditos":
        if scroll_y >= -900:
            scroll_y -= 1
    if mode == "game" and cps >= 25000000:
        mode = "final_bueno"

    if finb_index >= 3 or finb_indexin >= 3:
        ftext = 335
    if finb_index == 28 or finb_indexin == 28:
        ftext = 200

def draw():
    if mode == "final_bueno":#----------------------------------------------------------------------------------------------------------
        screen.fill("black")
        if idioma == "español":
            screen.draw.text(finb_texts[finb_index],center=(300, ftext),color="white",fontsize=40)
            screen.draw.text("Presiona una tecla…",center=(470, 380),color=(35,35,35),fontsize=30)
            if finb_index >= 3 and finb_index < 28:
                caballot2.draw()
            if finb_index >= 4 and finb_index < 28:
                pollitot2.draw()
            if finb_index >= 5 and finb_index < 28:
                serpientet2.draw()
            if finb_index >= 6 and finb_index < 28:
                vacat2.draw()
            if finb_index >= 7 and finb_index < 28:
                elefantet2.draw()
            if finb_index >= 8 and finb_index < 28:
                osot2.draw()

            if finb_index == 28:
                screen.draw.text("Final Bueno (2/2)",center=(300,315),color="white",fontsize=40)
                screen.draw.text("Fin",center=(300,110),color="white",fontsize=40)
        if idioma == "ingles":
            screen.draw.text(finb_textsin[finb_indexin],center=(300, ftext),color="white",fontsize=40)
            screen.draw.text("Press a key…",center=(500, 380),color=(35,35,35),fontsize=30)
            if finb_indexin >= 3 and finb_indexin < 28:
                caballot2.draw()
            if finb_indexin >= 4 and finb_indexin < 28:
                pollitot2.draw()
            if finb_indexin >= 5 and finb_indexin < 28:
                serpientet2.draw()
            if finb_indexin >= 6 and finb_indexin < 28:
                vacat2.draw()
            if finb_indexin >= 7 and finb_indexin < 28:
                elefantet2.draw()
            if finb_indexin >= 8 and finb_indexin < 28:
                osot2.draw()

            if finb_indexin == 28:
                screen.draw.text("Good Ending (2/2)",center=(300,315),color="white",fontsize=40)
                screen.draw.text("The End",center=(300,110),color="white",fontsize=40)
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "intro":#--------------------------------------------------------------------------------------------------------------
        screen.fill("black")
        if idioma == "ninguno":
            elije_idioma.draw()
            ingles.draw()
            español.draw()
            screen.draw.text("Por favor seleccione un idioma",center=(300, 150),color="black",fontsize=30)
            screen.draw.text("Please select a language",center=(300, 190),color="black",fontsize=30)
        if idioma == "español":
            if intro_index < len(intro_texts):
                screen.draw.text(intro_texts[intro_index],center=(300, 200),color="white",fontsize=40)
            screen.draw.text("Presiona una tecla…",center=(450, 380),color=(35,35,35),fontsize=30)

        elif idioma == "ingles":
            if intro_indexin < len(intro_textsin):
                screen.draw.text(intro_textsin[intro_indexin],center=(300, 200),color="white",fontsize=40)
            screen.draw.text("Press a key…",center=(500, 380),color=(35,35,35),fontsize=30)

    elif mode == "outro":#--------------------------------------------------------------------------------------------------------------
        screen.fill("black")
        if idioma == "español":
            screen.draw.text("Presiona una tecla…",center=(450, 380),color=(35,35,35),fontsize=30)
            screen.draw.text(outro_texts[outro_index],center=(300, 200),color="white",fontsize=40)
        elif idioma == "ingles":
            screen.draw.text("Press a key…",center=(500, 380),color=(35,35,35),fontsize=30)
            screen.draw.text(outro_textsin[outro_indexin],center=(300, 200),color="white",fontsize=40)
        if outro_index == 4:
            telefono.draw()
        if outro_index == 39:
            screen.draw.text("Cr",center=(168, 100),color="red",fontsize=40)
            screen.draw.text("eepy animal clicker",center=(315, 100),color="white",fontsize=40)
            screen.draw.text("Final Malo (1/2)",center=(300,300),color="white",fontsize=40)
        if outro_indexin == 4:
            telefono.draw()
        if outro_indexin == 39:
            screen.draw.text("Cr",center=(168, 100),color="red",fontsize=40)
            screen.draw.text("eepy animal clicker",center=(315, 100),color="white",fontsize=40)
            screen.draw.text("Bad Ending (1/2)",center=(300,300),color="white",fontsize=40)
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "creditos":#-----------------------------------------------------------------------------------------------------------
        screen.clear()
        screen.fill("black")
        if idioma == "español":
            for i, line in enumerate(credits):
                screen.draw.text(line,center=(300, scroll_y + i*40),fontsize=40,color="white")
        if idioma == "ingles":
            for i, line in enumerate(creditos):
                screen.draw.text(line,center=(300, scroll_y + i*40),fontsize=40,color="white")

        if scroll_y <= -900:
            if idioma == "español":
                screen.draw.text("Haz clic para volver al pasado...", center=(300, 200), color="white", fontsize = 35)
            if idioma == "ingles":
                screen.draw.text("Click to go back to the past...", center=(300, 200), color="white", fontsize = 35)

        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(34,17), color="white", fontsize = 25)

    elif mode == "menu":#---------------------------------------------------------------------------------------------------------------
        bg.draw()
        play.draw()
        shop.draw()
        collection.draw()
        screen.draw.text(f"${count}", center=(300, 260), color="white", fontsize = 96)
        screen.draw.text("eepy Animal Clicker", center=(300, 75), color="white", fontsize=70)
        screen.draw.text("eepy Animal Clicker", center=(300, 78), color="grey", fontsize=70)
        configuracion.y = 35
        configuracion.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(560,20), color="white", fontsize = 25)

    elif mode == "game":#---------------------------------------------------------------------------------------------------------------
        bg.draw()
        screen.draw.text(f"${count}", center=(150, 110), color="white", fontsize = 75)
        salida.draw()
        animal.draw()
        if idioma == "español":
            screen.draw.text(f"CPS Auto: ${cps}/s", center=(150, 50), color="white", fontsize = 25)
        elif idioma == "ingles":
            screen.draw.text(f"Auto CPS: ${cps}/s", center=(150, 50), color="white", fontsize = 25)
        configuracion.y = 365
        configuracion.draw()
        
        
        if nivel_de_mejora == 1:
            bonus_1.draw()
            bonus_2.draw()
            bonus_3.draw()
            if idioma == "español":
                screen.draw.text("+1$ Cada 1s", center=(400, 105), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_1}", center=(450, 135), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_1}", center=(495, 106), color="black", fontsize = 20)

                screen.draw.text("+15$ cada 1s", center=(400, 205), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_2}", center=(450, 235), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_2}", center=(495, 206), color="black", fontsize = 20)

                screen.draw.text("+50$ cada 1s", center=(400, 300), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_3}", center=(450, 330), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_3}", center=(495, 300), color="black", fontsize = 20)
            elif idioma == "ingles":
                screen.draw.text("+$1 Every 1s", center=(400, 105), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_1}", center=(450, 135), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_1}", center=(495, 106), color="black", fontsize = 20)

                screen.draw.text("+$15 Every 1s", center=(400, 205), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_2}", center=(450, 235), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_2}", center=(495, 206), color="black", fontsize = 20)

                screen.draw.text("+$50 Every 1s", center=(400, 300), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_3}", center=(450, 330), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_3}", center=(495, 300), color="black", fontsize = 20)
            hacia_abajo.draw()
            if "1" not in comprados:
                mejorar_mejoras.draw()
                x1.draw()
                costo_abajo.draw()
        elif nivel_de_mejora == 2:
            bonus_4.draw()
            bonus_5.draw()
            bonus_6.draw()
            if idioma == "español":
                screen.draw.text("+500$ Cada 1s", center=(405, 105), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_4}", center=(450, 135), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_4}", center=(500, 106), color="black", fontsize = 20)

                screen.draw.text("+1750$ cada 1s", center=(405, 205), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_5}", center=(450, 235), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_5}", center=(500, 206), color="black", fontsize = 20)
                
                screen.draw.text("+6000$ cada 1s", center=(405, 300), color="black", fontsize = 20)
                screen.draw.text(f"Precio: ${precio_6}", center=(450, 330), color="black", fontsize = 20)
                screen.draw.text(f"Mejoras: {mejoras_6}", center=(500, 300), color="black", fontsize = 20)
            elif idioma == "ingles":
                screen.draw.text("+$500 Every 1s", center=(405, 105), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_4}", center=(450, 135), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_4}", center=(500, 106), color="black", fontsize = 20)

                screen.draw.text("+$1750 Every 1s", center=(405, 205), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_5}", center=(450, 235), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_5}", center=(500, 206), color="black", fontsize = 20)
                
                screen.draw.text("+$6000 Every 1s", center=(405, 300), color="black", fontsize = 20)
                screen.draw.text(f"Price: ${precio_6}", center=(450, 330), color="black", fontsize = 20)
                screen.draw.text(f"Upgrades: {mejoras_6}", center=(500, 300), color="black", fontsize = 20)
            hacia_abajo2.draw()
            if "2" not in comprados:
                mejorar_mejoras.draw()
                x1.draw()
                costo_abajo2.draw()
            if "2" in comprados:
                hacia_arriba.draw()
        elif nivel_de_mejora == 3:
            bonus_7.draw()
            bonus_8.draw()
            bonus_9.draw()
            if idioma == "español":
                screen.draw.text("+40000$ Cada 1s", center=(407, 105), color="black", fontsize = 18)
                screen.draw.text(f"Precio: ${precio_7}", center=(450, 135), color="black", fontsize = 18)
                screen.draw.text(f"Mejoras: {mejoras_7}", center=(500, 106), color="black", fontsize = 18)
                
                screen.draw.text("+120000$ cada 1s", center=(410, 205), color="black", fontsize = 18)
                screen.draw.text(f"Precio: ${precio_8}", center=(450, 230), color="black", fontsize = 18)
                screen.draw.text(f"Mejoras: {mejoras_8}", center=(505, 206), color="black", fontsize = 18)
                
                screen.draw.text("+500000$ cada 1s", center=(410, 300), color="black", fontsize = 18)
                screen.draw.text(f"Precio: ${precio_9}", center=(450, 330), color="black", fontsize = 18)
                screen.draw.text(f"Mejoras: {mejoras_9}", center=(505, 300), color="black", fontsize = 18)
            elif idioma == "ingles":
                screen.draw.text("+$40000 Every 1s", center=(407, 105), color="black", fontsize = 17)
                screen.draw.text(f"Price: ${precio_7}", center=(450, 135), color="black", fontsize = 18)
                screen.draw.text(f"Upgrades: {mejoras_7}", center=(500, 106), color="black", fontsize = 18)
                
                screen.draw.text("+$120000 Every 1s", center=(410, 205), color="black", fontsize = 17)
                screen.draw.text(f"Price: ${precio_8}", center=(450, 230), color="black", fontsize = 18)
                screen.draw.text(f"Upgrades: {mejoras_8}", center=(505, 206), color="black", fontsize = 18)
                
                screen.draw.text("+$500000 Every 1s", center=(410, 299), color="black", fontsize = 17)
                screen.draw.text(f"Price: ${precio_9}", center=(450, 330), color="black", fontsize = 18)
                screen.draw.text(f"Upgrades: {mejoras_9}", center=(505, 300), color="black", fontsize = 18)
            hacia_arriba.y = 45
            hacia_arriba.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "shop":#---------------------------------------------------------------------------------------------------------------
        bg.draw()
        cocodrilo.draw()
        hippo.draw()
        walrus.draw()
        salida.draw()
        hacia_derecha.draw()
        screen.draw.text(f"${count}", center=(300, 350), color="white", fontsize = 96)
        if idioma == "español":
            screen.draw.text("TIENDA", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("2 por click ", center= (120, 105), color="white", fontsize = 36)
            screen.draw.text("5 por click", center= (300, 105), color="white", fontsize = 36)
            screen.draw.text("15 por click", center= (480, 105), color="white", fontsize = 36)
            screen.draw.text("250$", center= (120, 290), color="white", fontsize = 36)
            screen.draw.text("750$", center= (300, 290), color="white", fontsize = 36)
            screen.draw.text("2500$", center= (480, 290), color="white", fontsize = 36)
        elif idioma == "ingles":
            screen.draw.text("SHOP", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("2 per click ", center= (120, 105), color="white", fontsize = 36)
            screen.draw.text("5 per click", center= (300, 105), color="white", fontsize = 36)
            screen.draw.text("15 per click", center= (480, 105), color="white", fontsize = 36)
            screen.draw.text("$250", center= (120, 290), color="white", fontsize = 36)
            screen.draw.text("$750", center= (300, 290), color="white", fontsize = 36)
            screen.draw.text("$2500", center= (480, 290), color="white", fontsize = 36)

        if "cocodrilo" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(120,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(120,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(120,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(120,225), color = (30,30,30), fontsize = 23)
        if "hipopotamo" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(300,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(300,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(300,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(300,225), color = (30,30,30), fontsize = 23)
        if "morsa" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(480,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(480,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(480,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(480,225), color = (30,30,30), fontsize = 23)
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "shop_2":#-------------------------------------------------------------------------------------------------------------
        bg.draw()
        hacia_derecha.draw()
        hacia_izquierda.draw()
        salida.draw()
        screen.draw.text(f"${count}", center=(300, 350), color="white", fontsize = 96)
        caballo.draw()
        pollito.draw()
        serpiente.draw()

        if idioma == "español":
            screen.draw.text("TIENDA", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("50 por click ", center= (120, 105), color="white", fontsize = 33)
            screen.draw.text("175 por click", center= (300, 105), color="white", fontsize = 33)
            screen.draw.text("600 por click", center= (480, 105), color="white", fontsize = 33)
            screen.draw.text("130000$", center= (480, 290), color="white", fontsize = 36)
            screen.draw.text("35000$", center= (300, 290), color="white", fontsize = 36)
            screen.draw.text("9000$", center= (120, 290), color="white", fontsize = 36)
        elif idioma == "ingles":
            screen.draw.text("SHOP", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("50 per click ", center= (120, 105), color="white", fontsize = 33)
            screen.draw.text("175 per click", center= (300, 105), color="white", fontsize = 33)
            screen.draw.text("600 per click", center= (480, 105), color="white", fontsize = 33)
            screen.draw.text("$130000", center= (480, 290), color="white", fontsize = 36)
            screen.draw.text("$35000", center= (300, 290), color="white", fontsize = 36)
            screen.draw.text("$9000", center= (120, 290), color="white", fontsize = 36)
        if "caballo" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(120,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(120,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(120,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(120,225), color = (30,30,30), fontsize = 23)
        if "pollito" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(300,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(300,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(300,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(300,225), color = (30,30,30), fontsize = 23)
        if "serpiente" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(480,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(480,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(480,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(480,225), color = (30,30,30), fontsize = 23)
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "shop_3":#-------------------------------------------------------------------------------------------------------------
        bg.draw()
        hacia_derecha.draw()
        hacia_izquierda.draw()
        salida.draw()
        screen.draw.text(f"${count}", center=(300, 350), color="white", fontsize = 96)
        vaca.draw()
        oso.draw()
        elefante.draw()
        if idioma == "español":
            screen.draw.text("TIENDA", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("2000 por click", center= (120, 100), color="white", fontsize = 32)
            screen.draw.text("7500 por click", center= (300, 100), color="white", fontsize = 32)
            screen.draw.text("25000 por click", center= (480, 100), color="white", fontsize = 32)
            screen.draw.text("500000$", center= (120, 290), color="white", fontsize = 36)
            screen.draw.text("2250000$", center= (300, 300), color="white", fontsize = 36)
            screen.draw.text("10000000$", center= (480, 290), color="white", fontsize = 36)
        elif idioma == "ingles":
            screen.draw.text("SHOP", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("2000 per click", center= (120, 100), color="white", fontsize = 32)
            screen.draw.text("7500 per click", center= (300, 100), color="white", fontsize = 32)
            screen.draw.text("25000 per click", center= (480, 100), color="white", fontsize = 32)
            screen.draw.text("$500000", center= (120, 290), color="white", fontsize = 36)
            screen.draw.text("$2250000", center= (300, 300), color="white", fontsize = 36)
            screen.draw.text("$10000000", center= (480, 290), color="white", fontsize = 36)
        if "vaca" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(120,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(120,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(120,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(120,225), color = (30,30,30), fontsize = 23)
        if "elefante" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(300,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(300,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(300,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(300,225), color = (30,30,30), fontsize = 23)
        if "oso" in animals:
            if idioma == "español":
                screen.draw.text("COMPRADO", center=(480,200), color = (30,30,30), fontsize = 33)
                screen.draw.text("ve a coleccion", center=(480,225), color = (30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("PURCHASED", center=(480,200), color = (30,30,30), fontsize = 32)
                screen.draw.text("go to collection", center=(480,225), color = (30,30,30), fontsize = 23)

        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "shop_4":#-------------------------------------------------------------------------------------------------------------
        bg.draw()
        hacia_izquierda.draw()
        if idioma == "español":
            screen.draw.text("TIENDA", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("50000000$", center=(300,283), color = "white", fontsize = 33)
        elif idioma == "ingles":
            screen.draw.text("SHOP", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("$50000000", center=(300,283), color = "white", fontsize = 33)
        salida.draw()
        screen.draw.text(f"${count}", center=(300, 350), color="white", fontsize = 96)
        trofeo.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)

    elif mode == "collection":#---------------------------------------------------------------------------------------------------------
        bg.draw()
        salida.draw()
        hacia_derecha.draw()
        if idioma == "español":
            screen.draw.text("COLECCION", center=(300, 40), color="white", fontsize=48)
        elif idioma == "ingles":
            screen.draw.text("COLLECTION", center=(300, 40), color="white", fontsize=48)
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,380), color="white", fontsize = 25)
        if len(animals) == 0:
            if idioma == "español":
                screen.draw.text("Aún no tienes ninguna skin", center=(300, 200), color="white", fontsize=36)
            elif idioma == "ingles":
                screen.draw.text("You don't have any skins yet", center=(300, 200), color="white", fontsize=36)

        if len(animals) > 0:
            equipar_p.draw()

        if "cocodrilo" in animals:
            cocodrilo.draw()
            if idioma == "español":
                screen.draw.text("2$ por click", center= (120, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$2 per click", center= (120, 105), color="white", fontsize = 36)
        if "hipopotamo" in animals:
            hippo.draw()
            if idioma == "español":
                screen.draw.text("5$ por click", center= (300, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$5 per click", center= (300, 105), color="white", fontsize = 36)
        if "morsa" in animals:
            walrus.draw()
            if idioma == "español":
                screen.draw.text("15$ por click", center= (480, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$15 per click", center= (480, 105), color="white", fontsize = 36)

        if seleccionado == "cocodrilo":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (120, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (120, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "hipopotamo":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (300, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (300, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "morsa":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (480, 200), color=(20,20,20), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (480, 200), color=(20,20,20), fontsize = 37)
        if seleccionado == "jirafa" and len(animals) > 0:
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (40,45), color=(0,0,0), fontsize = 14)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (40,45), color=(0,0,0), fontsize = 21)
    
        screen.draw.text(f"${count}", center=(300, 340), color="white", fontsize = 60)#----------------------------------------------------------------------------------------------------------

    elif mode == "collection_2":#-------------------------------------------------------------------------------------------------------
        bg.draw()
        salida.draw()
        if idioma == "español":
            screen.draw.text("COLECCION", center=(300, 40), color="white", fontsize=48)
        elif idioma == "ingles":
            screen.draw.text("COLLECTION", center=(300, 40), color="white", fontsize=48)        
        screen.draw.text(f"${count}", center=(300, 340), color="white", fontsize = 60)
        hacia_derecha.draw()
        hacia_izquierda.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,380), color="white", fontsize = 25)
        if len(animals) == 0:
            if idioma == "español":
                screen.draw.text("Aún no tienes ninguna skin", center=(300, 200), color="white", fontsize=36)
            elif idioma == "ingles":
                screen.draw.text("You don't have any skins yet", center=(300, 200), color="white", fontsize=36)

        if "caballo" in animals:
            caballo.draw()
            if idioma == "español":
                screen.draw.text("50$ por click", center= (120, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$50 per click", center= (120, 105), color="white", fontsize = 36)
        if "pollito" in animals:
            pollito.draw()
            if idioma == "español":
                screen.draw.text("175$ por click", center= (300, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$175 per click", center= (300, 105), color="white", fontsize = 36)
        if "serpiente" in animals:
            serpiente.draw()
            if idioma == "español":
                screen.draw.text("600$ por click", center= (480, 105), color="white", fontsize = 36)
            elif idioma == "ingles":
                screen.draw.text("$600 per click", center= (480, 105), color="white", fontsize = 36)

        if seleccionado == "caballo":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (120, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (120, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "pollito":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (300, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (300, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "serpiente":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (480, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (480, 200), color=(30,30,30), fontsize = 37)
    
    elif mode == "collection_3":#-------------------------------------------------------------------------------------------------------
        bg.draw()
        salida.draw()
        if idioma == "español":
            screen.draw.text("COLECCION", center=(300, 40), color="white", fontsize=48)
        elif idioma == "ingles":
            screen.draw.text("COLLECTION", center=(300, 40), color="white", fontsize=48)
        screen.draw.text(f"${count}", center=(300, 340), color="white", fontsize = 60)
        hacia_izquierda.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,380), color="white", fontsize = 25)
        if len(animals) == 0:
            if idioma == "español":
                screen.draw.text("Aún no tienes ninguna skin", center=(300, 200), color="white", fontsize=36)
            elif idioma == "ingles":
                screen.draw.text("You don't have any skins yet", center=(300, 200), color="white", fontsize=36)
        
        if "vaca" in animals:
            vaca.draw()
            if idioma == "español":
                screen.draw.text("2000$ por click", center= (120, 105), color="white", fontsize = 30)
            elif idioma == "ingles":
                screen.draw.text("$2000 per click", center= (120, 105), color="white", fontsize = 30)
        if "elefante" in animals:
            elefante.draw()
            if idioma == "español":
                screen.draw.text("7500$ por click", center= (300, 105), color="white", fontsize = 30)
            elif idioma == "ingles":
                screen.draw.text("$7500 per click", center= (300, 105), color="white", fontsize = 30)
        if "oso" in animals:
            oso.draw()
            if idioma == "español":
                screen.draw.text("25000$ por click", center= (480, 105), color="white", fontsize = 30)
            elif idioma == "ingles":
                screen.draw.text("$25000 per click", center= (480, 105), color="white", fontsize = 30)
        
        if seleccionado == "vaca":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (120, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (120, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "elefante":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (300, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (300, 200), color=(30,30,30), fontsize = 37)
        if seleccionado == "oso":
            if idioma == "español":
                screen.draw.text("SELECCIONADO", center= (480, 200), color=(30,30,30), fontsize = 25)
            elif idioma == "ingles":
                screen.draw.text("SELECTED", center= (480, 200), color=(30,30,30), fontsize = 37)
        
    elif mode == "configuracion": #-----------------------------------------------------------------------------------------------------
        screen.fill((50, 50, 50))
        salida.draw()
        mostrar_FPS.draw()
        apagado.draw()
        reiniciar.draw()
        cambiar_fps.draw()
        idioma2.draw()
        if idioma == "español":
            screen.draw.text("CONFIGURACION", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("REINICIAR", center=(433, 145), color="black", fontsize = 36)
            screen.draw.text("Mostrar FPS", center=(410, 240), color="black", fontsize = 30)
            screen.draw.text("Cambiar FPS", center=(435, 340), color="black", fontsize = 36)
            screen.draw.text(f"Tiempo Jugado: {tiempo_jugado}s", center=(140, 240), color="white", fontsize = 30)
            screen.draw.text("Cambiar Idioma", center=(140, 340), color="black", fontsize = 33)
            screen.draw.text(f"clicks totales: {cantidad_clicks}", center=(140, 145), color="white", fontsize = 36)
        elif idioma == "ingles":
            screen.draw.text("SETTINGS", center=(300, 40), color="white", fontsize=48)
            screen.draw.text("RESET", center=(433, 145), color="black", fontsize = 36)
            screen.draw.text("Show FPS", center=(410, 240), color="black", fontsize = 30)
            screen.draw.text("Change FPS", center=(435, 340), color="black", fontsize = 36)
            screen.draw.text(f"Played Time: {tiempo_jugado}s", center=(140, 240), color="white", fontsize = 30)
            screen.draw.text("Language", center=(140, 340), color="black", fontsize = 36)
            screen.draw.text(f"Total Clicks: {cantidad_clicks}", center=(140, 145), color="white", fontsize = 36)
        if reiniciar_progreso == True:
            estas_seguro.draw()
            if idioma == "español":
                screen.draw.text("¿Estas Seguro?", center=(300, 135), color="black", fontsize = 36)
                screen.draw.text("Esta accion es irreversible", center=(300, 167), color="black", fontsize = 36)
                si.draw()
                no.draw()
            elif idioma == "ingles":
                screen.draw.text("Are You Sure?", center=(300, 135), color="black", fontsize = 36)
                screen.draw.text("This action is irreversible", center=(300, 167), color="black", fontsize = 36)
                no.draw()
                yes.draw()
        if fpsm == True:
            screen.draw.text(F"FPS: {FPS}", center=(40,20), color="white", fontsize = 25)
        if cfps == True:
            elije_fps.draw()
            treinta.draw()
            sesenta.draw()
            cientoveinte.draw()
            doscuarenta.draw()
            x2.draw()
            if idioma == "español":
                screen.draw.text("Elije los FPS que prefieras", center=(300, 135), color="black", fontsize = 30)
            elif idioma == "ingles":
                screen.draw.text("Choose your preferred FPS", center=(300, 135), color="black", fontsize = 29)
        if click_idioma == True:
            elije_idioma.draw()
            x3.draw()
            if idioma == "español":
                screen.draw.text("Por favor seleccione un idioma",center=(300, 170),color="black",fontsize=30)
                español.draw()
                english.draw()
            elif idioma == "ingles":
                screen.draw.text("Please select a language",center=(300, 170),color="black",fontsize=30)
                ingles.draw()
                spanish.draw()

def for_bonus_1():
    global count
    count+=1
    
def for_bonus_2():
    global count
    count+=15
    
def for_bonus_3():
    global count
    count+=50
    
def for_bonus_4():
    global count
    count+=500

def for_bonus_5():
    global count
    count+=1750

def for_bonus_6():
    global count
    count+=6000

def for_bonus_7():
    global count
    count+=40000

def for_bonus_8():
    global count
    count+=120000

def for_bonus_9():
    global count
    count+=500000
    
def on_mouse_down(button,pos):
    global count, mode, fpsm, idioma, click_idioma, ftext, tiempo_jugado, cfps, FPS, sesenta, cientoveinte, doscuarenta, finb_index, precio_1, precio_2, precio_3, click, new_image, animals, cps,mejoras_1, mejoras_2, mejoras_3, seleccionado, cantidad_clicks, modo_anterior, reiniciar_progreso, nivel_de_mejora, precio_4,precio_5,precio_6,mejoras_4,mejoras_5,mejoras_6, precio_7,precio_8,precio_9,mejoras_7,mejoras_8,mejoras_9,scroll_y,fin_c,comprados, intro_indexin, intro_textsin, finb_textsin, finb_indexin, intro_indexin, outro_indexin

    if (mode == "menu" or mode == "game") and configuracion.collidepoint(pos):
        modo_anterior = mode
        mode = "configuracion"
    
        # SHOP
    if mode == "shop" and hacia_derecha.collidepoint(pos):
        mode = "shop_2"
    elif mode == "shop_2" and hacia_derecha.collidepoint(pos):
        mode = "shop_3"
    elif mode == "shop_3" and hacia_derecha.collidepoint(pos):
        mode = "shop_4"

    elif mode == "shop_2" and hacia_izquierda.collidepoint(pos):
        mode = "shop"
    elif mode == "shop_3" and hacia_izquierda.collidepoint(pos):
        mode = "shop_2"
    elif mode == "shop_4" and hacia_izquierda.collidepoint(pos):
        mode = "shop_3"

    # COLLECTION
    if mode == "collection" and hacia_derecha.collidepoint(pos):
        mode = "collection_2"
    elif mode == "collection_2" and hacia_derecha.collidepoint(pos):
        mode = "collection_3"

    elif mode == "collection_2" and hacia_izquierda.collidepoint(pos):
        mode = "collection"
    elif mode == "collection_3" and hacia_izquierda.collidepoint(pos):
        mode = "collection_2"
        
    if mode == "menu":
        if play.collidepoint(pos):
            mode = "game"

        if shop.collidepoint(pos):
            mode = "shop"
        
        if collection.collidepoint(pos):
            mode = "collection"
    
    if mode == "configuracion":
        if click_idioma:
            if español.collidepoint(pos):
                español.y += 4
                animate(español, tween="bounce_end", duration=0.5, y=250)
                idioma = "español"
            elif ingles.collidepoint(pos):
                ingles.y += 4
                animate(ingles, tween="bounce_end", duration=0.5, y=250)
                idioma = "ingles"
            if spanish.collidepoint(pos):
                español.y += 4
                animate(español, tween="bounce_end", duration=0.5, y=250)
                idioma = "español"
            elif english.collidepoint(pos):
                ingles.y += 4
                animate(ingles, tween="bounce_end", duration=0.5, y=250)
                idioma = "ingles"
            elif x3.collidepoint(pos):
                click_idioma = False
            if idioma == "español":
                play.image = "play"
                shop.image = "tienda"
                collection.image = "coleccion"
                mejorar_mejoras.image = "mejorar_mejoras"
            elif idioma == "ingles":
                play.image = "jugar"
                shop.image = "shop"
                collection.image = "collection"
                mejorar_mejoras.image = "upgrade_upgrades"
        elif cfps:
            if treinta.collidepoint(pos):
                treinta.y += 3
                animate(treinta, tween="bounce_end", duration=0.5, y=185)
                FPS = 30
            elif sesenta.collidepoint(pos):
                sesenta.y += 3
                animate(sesenta, tween="bounce_end", duration=0.5, y=185)
                FPS = 60
            elif cientoveinte.collidepoint(pos):
                cientoveinte.y += 3
                animate(cientoveinte, tween="bounce_end", duration=0.5, y=250)
                FPS = 120
            elif doscuarenta.collidepoint(pos):
                doscuarenta.y += 3
                animate(doscuarenta, tween="bounce_end", duration=0.5, y=250)
                FPS = 240
            elif x2.collidepoint(pos):
                cfps = False

        elif reiniciar_progreso:
            pass
        else:
            if cambiar_fps.collidepoint(pos):
                cambiar_fps.y += 4
                animate(cambiar_fps, tween="bounce_end", duration=0.5, y=340)
                cfps = True
                
            elif reiniciar.collidepoint(pos):
                reiniciar.y += 4
                animate(reiniciar, tween="bounce_end", duration=0.5, y=145)
                reiniciar_progreso = True
                
            elif mostrar_FPS.collidepoint(pos):
                mostrar_FPS.y += 4
                animate(mostrar_FPS, tween="bounce_end", duration=0.5, y=240)
                fpsm = not fpsm
                apagado.image = "encendido" if fpsm else "apagado"
                
            elif idioma2.collidepoint(pos):
                idioma2.y += 4
                animate(idioma2, tween="bounce_end", duration=0.5, y=340)
                click_idioma = True
    if mode == "intro":
        if español.collidepoint(pos):
            idioma = "español"
        if ingles.collidepoint(pos):
            idioma = "ingles"
        if idioma == "español":
            play.image = "play"
            shop.image = "tienda"
            collection.image = "coleccion"
            mejorar_mejoras.image = "mejorar_mejoras"
        elif idioma == "ingles":
            play.image = "jugar"
            shop.image = "shop"
            collection.image = "collection"
            mejorar_mejoras.image = "upgrade_upgrades"
    if mode == "creditos" and scroll_y <= -900:
        if button == mouse.LEFT:
            exit()
    if mode == "configuracion" and reiniciar_progreso:
        if si.collidepoint(pos) or yes.collidepoint(pos):
            count = 0
            click = 1
            cps = 0
            animal.image = "giraffe"
            nivel_de_mejora = 1
            animals.clear()
            comprados.clear()
            seleccionado = "jirafa"
            cantidad_clicks = 0
            mejoras_1 = mejoras_2 = mejoras_3 = mejoras_4 = mejoras_5 = mejoras_6 = mejoras_7 = mejoras_8 = mejoras_9 = 0
            bonus_1.x = bonus_2.x = bonus_3.x = bonus_4.x = bonus_5.x = bonus_6.x = bonus_7.x = bonus_8.x = bonus_9.x = hacia_abajo.x = 450
            precio_1 = 15
            precio_2 = 200
            precio_3 = 600
            precio_4 = 6000
            precio_5 = 20000
            precio_6 = 70000
            precio_7 = 500000
            precio_8 = 1500000
            precio_9 = 5000000
            clock.unschedule(for_bonus_1)
            clock.unschedule(for_bonus_2)
            clock.unschedule(for_bonus_3)
            clock.unschedule(for_bonus_4)
            clock.unschedule(for_bonus_5)
            clock.unschedule(for_bonus_6)
            clock.unschedule(for_bonus_7)
            clock.unschedule(for_bonus_8)
            clock.unschedule(for_bonus_9)
            tiempo_jugado = 0
            reiniciar_progreso = False
            mode = "menu"
            scroll_y = 500
            fin_c = False
            intro_index = 0
            intro_indexin = 0
            outro_index = 0
            outro_indexin = 0
            finb_index = 0
            finb_indexin = 0
            ftext = 200
            caballot2.image = "horse_t2"
            pollitot2.image = "chick_t2"
            serpientet2.image = "snake_t2"
            vacat2.image = "cow_t2"
            elefantet2.image = "elephant_t2"
            osot2.image = "bear_t2"
            fpsm = False
            apagado.image = "apagado"

        if no.collidepoint(pos):
            reiniciar_progreso = False
    
    if button == mouse.LEFT:
        if mode == "shop":
            if cocodrilo.collidepoint(pos):
                cocodrilo.y = 185
                animate(cocodrilo, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop" and count >= 250 and "cocodrilo" not in animals:
                    animals.append("cocodrilo")
                    count -= 250
            
            elif hippo.collidepoint(pos):
                hippo.y = 185
                animate(hippo, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop" and count >= 750 and "hipopotamo" not in animals:
                    animals.append("hipopotamo")
                    count -= 750
                    
            elif walrus.collidepoint(pos):
                walrus.y = 185
                animate(walrus, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop" and count >= 2500 and "morsa" not in animals:
                    animals.append("morsa")
                    count -= 2500
        
        if mode == "shop_2":
            if caballo.collidepoint(pos):
                caballo.y = 185
                animate(caballo, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_2" and count >= 9000 and "caballo" not in animals:
                    animals.append("caballo")
                    count -= 9000
            
            if pollito.collidepoint(pos):
                pollito.y = 185
                animate(pollito, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_2" and count >= 35000 and "pollito" not in animals:
                    animals.append("pollito")
                    count -= 35000
            
            if serpiente.collidepoint(pos):
                serpiente.y = 185
                animate(serpiente, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_2" and count >= 130000 and "serpiente" not in animals:
                    animals.append("serpiente")
                    count -= 130000
        
        if mode == "shop_3":
            if vaca.collidepoint(pos):
                vaca.y = 185
                animate(vaca, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_3" and count >= 500000 and "vaca" not in animals:
                    animals.append("vaca")
                    count -= 500000
            
            if elefante.collidepoint(pos):
                elefante.y = 185
                animate(elefante, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_3" and count >= 2250000 and "elefante" not in animals:
                    animals.append("elefante")
                    count -= 2250000
            
            if oso.collidepoint(pos):
                oso.y = 185
                animate(oso, tween='bounce_end', duration=0.5, y=200)
                if mode == "shop_3" and count >= 10000000 and "oso" not in animals:
                    animals.append("oso")
                    count -= 10000000
        if mode == "shop_4":
            if trofeo.collidepoint(pos):
                trofeo.y = 175
                animate(trofeo, tween="bounce_end", duration=0.5, y=190)
                if count >= 50000000:
                    count -= 50000000
                    mode = "outro"
        if mode == "collection":
            if mode == "collection" and equipar_p.collidepoint(pos):
                equipar_p.y = 33
                animate(equipar_p, tween='bounce_end', duration=0.5, y=40)
                seleccionado = "jirafa"
                animal.image = "giraffe"
                if click != 1:
                    click = 1
            
            if cocodrilo.collidepoint(pos):
                cocodrilo.y -= 15
                animate(cocodrilo, tween='bounce_end', duration=0.5, y=200)
                if "cocodrilo" in animals:
                    seleccionado = "cocodrilo"
                    animal.image = "crocodile"
                    if click != 2:
                        click = 2
            
            if hippo.collidepoint(pos):
                hippo.y -= 15
                animate(hippo, tween='bounce_end', duration=0.5, y=200)
                if "hipopotamo" in animals:
                    seleccionado = "hipopotamo"
                    animal.image = "hippo"
                    if click != 5:
                        click = 5
            
            if walrus.collidepoint(pos):
                walrus.y -= 15
                animate(walrus, tween='bounce_end', duration=0.5, y=200)
                if "morsa" in animals:
                    seleccionado = "morsa"
                    animal.image = "walrus"
                    if click != 15:
                        click = 15
        if mode == "collection_2":
            if caballo.collidepoint(pos):
                caballo.y -= 15
                animate(caballo, tween='bounce_end', duration=0.5, y=200)
                if "caballo" in animals:
                    seleccionado = "caballo"
                    animal.image = "horse_t"
                    if click != 50:
                        click = 50
            
            if pollito.collidepoint(pos):
                pollito.y -= 15
                animate(pollito, tween='bounce_end', duration=0.5, y=200)
                if "pollito" in animals:
                    seleccionado = "pollito"
                    animal.image = "chick_t"
                    if click != 175:
                        click = 175
            
            if serpiente.collidepoint(pos):
                serpiente.y -= 15
                animate(serpiente, tween='bounce_end', duration=0.5, y=200)
                if "serpiente" in animals:
                    seleccionado = "serpiente"
                    animal.image = "snake_t"
                    if click != 600:
                        click = 600
                    
        if mode == "collection_3":
            if vaca.collidepoint(pos):
                vaca.y -= 15
                animate(vaca, tween='bounce_end', duration=0.5, y=200)
                if "vaca" in animals:
                    seleccionado = "vaca"
                    animal.image = "cow_t"
                    if click != 2000:
                        click = 2000
            
            if elefante.collidepoint(pos):
                elefante.y -= 15
                animate(elefante, tween='bounce_end', duration=0.5, y=200)
                if "elefante" in animals:
                    seleccionado = "elefante"
                    animal.image = "elephant_t"
                    if click != 7500:
                        click = 7500
            
            if oso.collidepoint(pos):
                oso.y -= 15
                animate(oso, tween='bounce_end', duration=0.5, y=200)
                if "oso" in animals:
                    seleccionado = "oso"
                    animal.image = "bear_t"
                    if click != 25000:
                        click = 25000
            
        if mode == "game":
            if animal.collidepoint(pos):
                    cantidad_clicks += 1
                    count+=click
                    animal.y = 225
                    animate(animal, tween='bounce_end', duration=0.5, y=250)
                    
            if nivel_de_mejora == 1:
                if bonus_1.collidepoint(pos):
                    bonus_1.y -= 3
                    animate(bonus_1, tween='bounce_end', duration=0.5, y=125)
                    if count >= precio_1:
                            clock.schedule_interval(for_bonus_1, 1)
                            count -= precio_1
                            precio_1 += 15
                            cps += 1
                            mejoras_1 += 1
                            
                if bonus_2.collidepoint(pos):
                    bonus_2.y -= 3
                    animate(bonus_2, tween='bounce_end', duration=0.5, y=220)
                    if count >= precio_2:
                            clock.schedule_interval(for_bonus_2,1)
                            count -= precio_2
                            precio_2 += 200
                            cps += 15
                            mejoras_2 += 1
                            
                if bonus_3.collidepoint(pos):
                    bonus_3.y -= 3
                    animate(bonus_3, tween='bounce_end', duration=0.5, y=320)
                    if count >= precio_3:
                            clock.schedule_interval(for_bonus_3,1)
                            count -= precio_3
                            precio_3 += 600
                            cps += 50
                            mejoras_3 += 1

                if mejorar_mejoras.collidepoint(pos):
                    mejorar_mejoras.y -= 2
                    animate(mejorar_mejoras, tween='bounce_end', duration=0.5, y=40)
                    if count >= 10000 and nivel_de_mejora == 1 and "1" not in comprados:
                        nivel_de_mejora = 2
                        count -= 10000
                        comprados.append("1")
            elif nivel_de_mejora == 2:
                if hacia_arriba.collidepoint(pos):
                    nivel_de_mejora = 1
                elif bonus_4.collidepoint(pos):
                    bonus_4.y -= 3
                    animate(bonus_4, tween='bounce_end', duration=0.5, y=125)
                    if count >= precio_4:
                            clock.schedule_interval(for_bonus_4, 1)
                            count -= precio_4
                            precio_4 += 6000
                            cps += 500
                            mejoras_4 += 1
                            
                elif bonus_5.collidepoint(pos):
                    bonus_5.y -= 3
                    animate(bonus_5, tween='bounce_end', duration=0.5, y=220)
                    if count >= precio_5:
                            clock.schedule_interval(for_bonus_5,1)
                            count -= precio_5
                            precio_5 += 20000
                            cps += 1750
                            mejoras_5 += 1
                            
                elif bonus_6.collidepoint(pos):
                    bonus_6.y -= 3
                    animate(bonus_6, tween='bounce_end', duration=0.5, y=320)
                    if count >= precio_6:
                            clock.schedule_interval(for_bonus_6,1)
                            count -= precio_6
                            precio_6 += 70000
                            cps += 6000
                            mejoras_6 += 1
                elif mejorar_mejoras.collidepoint(pos):
                    if count >= 1000000 and nivel_de_mejora == 2 and "2" not in comprados:
                        nivel_de_mejora = 3
                        count -= 1000000
                        comprados.append("2")
            elif nivel_de_mejora == 3:
                if hacia_arriba.collidepoint(pos):
                    nivel_de_mejora = 2
                elif bonus_7.collidepoint(pos):
                    bonus_7.y -= 3
                    animate(bonus_7, tween='bounce_end', duration=0.5, y=125)
                    if count >= precio_7:
                            clock.schedule_interval(for_bonus_7, 1)
                            count -= precio_7
                            precio_7 += 500000
                            cps += 40000
                            mejoras_7 += 1
                            
                elif bonus_8.collidepoint(pos):
                    bonus_8.y -= 3
                    animate(bonus_8, tween='bounce_end', duration=0.5, y=220)
                    if count >= precio_8:
                            clock.schedule_interval(for_bonus_8,1)
                            count -= precio_8
                            precio_8 += 1500000
                            cps += 120000
                            mejoras_8 += 1
                            
                elif bonus_9.collidepoint(pos):
                    bonus_9.y -= 3
                    animate(bonus_9, tween='bounce_end', duration=0.5, y=320)
                    if count >= precio_9:
                            clock.schedule_interval(for_bonus_9,1)
                            count -= precio_9
                            precio_9 += 5000000
                            cps += 500000
                            mejoras_9 += 1
            if "1" in comprados and "2" in comprados and (nivel_de_mejora == 2 or nivel_de_mejora == 1):
                if hacia_abajo.collidepoint(pos):
                    nivel_de_mejora += 1
    if salida.collidepoint(pos):
        if mode == "configuracion":
            mode = modo_anterior
        else:
            mode = "menu"