"""Build IT->ES starter Mochi deck for a true-beginner Italian speaker.

Direction is REVERSED from Daniel's: front = Italian, back = Spanish,
example = Spanish sentence. Deck names in Italian (her source language).

Wipes data/working.json (backups exist) and packs data/import.mochi.
Run: python3 scripts/build_gf_deck.py
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mochi_edit import save, add_to, add_deck, inventory


REPO = Path(__file__).resolve().parent.parent


def fresh_skeleton():
    """Empty deck-set with the same Basic Flashcard template Daniel uses."""
    current = json.load(open(REPO / "data" / "working.json"))
    return {
        "~:version": current["~:version"],
        "~:templates": current["~:templates"],
        "~:schema/version": current["~:schema/version"],
        "~:decks": [],
    }


# (front-italian, back-spanish, example-spanish)
DECKS = {
    "Verbi essenziali": [
        ("essere", "ser (identidad/permanente) / estar (estado/ubicación)",
         "Soy Ana. / Estoy en casa. (italiano fonde ser y estar en «essere»)"),
        ("avere", "tener (posesión) / haber (aux: he comido)",
         "Tengo una casa. / He comido. (italiano «avere» cubre ambos)"),
        ("stare", "estar (estado/ubicación) — a veces «quedarse»",
         "¿Cómo estás?"),
        ("andare", "ir",
         "Voy al trabajo en bici."),
        ("venire", "venir",
         "¿Cuándo vienes a verme?"),
        ("fare", "hacer",
         "Hago la cena todas las noches."),
        ("dire", "decir",
         "Dime la verdad."),
        ("sapere", "saber (hechos, cómo) — NO «conocer a alguien»",
         "Sé que vienes mañana."),
        ("conoscere", "conocer (a personas/lugares) — requiere «a» ante persona",
         "Conozco a María desde niña."),
        ("potere", "poder",
         "No puedo dormir."),
        ("volere", "querer",
         "Quiero un café, por favor."),
        ("dovere", "tener que (obligación) / deber (moral)",
         "Tengo que trabajar. / Debes estudiar más."),
        ("chiamare", "llamar (¡+ «a» ante persona!)",
         "Llamo a María. (NO «llamo María»)"),
        ("guardare", "mirar — NO «guardar» (falso amigo: guardar = tenere/conservare)",
         "Mira esa película conmigo."),
        ("aspettare", "esperar (¡+ «a» ante persona!)",
         "Espero a Juan en la estación."),
        ("mangiare", "comer",
         "Como pasta casi cada día."),
        ("bere", "beber / tomar (bebidas)",
         "Bebo agua con las comidas."),
        ("dormire", "dormir",
         "Duermo ocho horas cada noche."),
        ("piacere", "gustar (invertido: «mi piace» = me gusta)",
         "Me gusta la pizza. / Me gustan las manzanas."),
        ("parlare", "hablar",
         "Hablo español e italiano."),
    ],

    "Connettivi": [
        ("e", "y (por defecto) / e (ante palabra que empieza por i-/hi-)",
         "Pedro y Ana. / Madre e hija."),
        ("ma", "pero (por defecto) / sino (contraste tras negación)",
         "Es caro pero bueno. / No es rojo, sino azul."),
        ("o", "o (por defecto) / u (ante palabra que empieza por o-/ho-)",
         "¿Café o té? / Siete u ocho."),
        ("però", "sin embargo / pero (a menudo al final)",
         "Es tarde; sin embargo, salgo."),
        ("perché", "porque (respuesta) / por qué (pregunta)",
         "Vengo porque quiero. / ¿Por qué no viniste?"),
        ("quindi", "así que / entonces / por (lo) tanto",
         "Era tarde, así que me fui a dormir."),
        ("se", "si (condicional)",
         "Si quieres, voy contigo."),
        ("anche se", "aunque (+ indicativo si el hecho es real)",
         "Aunque llueve, salgo igual."),
        ("mentre", "mientras",
         "Cocino mientras tú hablas."),
        ("quando", "cuando",
         "Cuando llegues, llámame."),
        ("allora", "entonces / pues (conector de consecuencia o discurso)",
         "Entonces, ¿qué hacemos?"),
        ("cioè", "o sea / es decir",
         "Llego tarde, o sea, sobre las ocho."),
    ],

    "Aspetto e Frequenza": [
        ("sempre", "siempre",
         "Siempre llego tarde al trabajo."),
        ("mai", "nunca / jamás (en español no lleva doble negación obligatoria si va antes: «Nunca como carne»)",
         "Nunca como carne. / No como carne nunca."),
        ("spesso", "a menudo / muchas veces",
         "Vengo a menudo a este bar."),
        ("di solito", "normalmente / por lo general",
         "Normalmente me despierto a las siete."),
        ("ancora", "todavía / aún",
         "¿Todavía estás aquí?"),
        ("già", "ya",
         "Ya he terminado la tarea."),
        ("ogni tanto", "de vez en cuando",
         "De vez en cuando salimos a cenar."),
        ("a volte", "a veces",
         "A veces no entiendo nada."),
        ("quasi mai", "casi nunca",
         "Casi nunca veo la tele."),
    ],

    "Riferimenti Temporali": [
        ("oggi", "hoy",
         "Hoy no trabajo."),
        ("ieri", "ayer",
         "Ayer llovió todo el día."),
        ("domani", "mañana",
         "Mañana te llamo, ¿vale?"),
        ("adesso / ora", "ahora",
         "Ahora no puedo, estoy ocupada."),
        ("dopo", "después / luego",
         "Después nos vemos, ¿te parece?"),
        ("prima", "antes",
         "Antes vivía en Roma."),
        ("stasera", "esta noche",
         "Esta noche salimos a cenar."),
        ("stamattina", "esta mañana",
         "Esta mañana me he levantado tarde."),
        ("l'anno scorso", "el año pasado",
         "El año pasado fui a México."),
        ("il mese prossimo", "el mes que viene / el próximo mes",
         "El mes que viene empieza el curso."),
    ],

    "Discorso e Riempitivi": [
        ("dai", "venga / vamos (ánimo o incredulidad)",
         "¡Venga, vamos ya!"),
        ("boh", "ni idea / yo qué sé (encogimiento de hombros)",
         "—¿Dónde está? —Ni idea."),
        ("ecco", "aquí está / he aquí (al presentar algo)",
         "Aquí está tu café."),
        ("insomma", "en fin / vamos / bueno (resumen o duda)",
         "En fin, no vino nadie a la fiesta."),
        ("magari", "ojalá (+ subjuntivo) / a lo mejor (posibilidad)",
         "¡Ojalá fuera verdad! / A lo mejor viene mañana."),
        ("davvero?", "¿de verdad? / ¿en serio?",
         "—Me caso. —¿De verdad?"),
        ("figurati", "no te preocupes / qué va / imagínate",
         "—Gracias. —No te preocupes."),
    ],

    "Falsi Amici": [
        ("burro", "mantequilla — ¡en español «burro» = asino/donkey!",
         "La mantequilla está en la nevera."),
        ("salire", "subir — ¡en español «salir» = uscire!",
         "Sube la escalera con cuidado."),
        ("aceto", "vinagre — ¡español «aceite» = olio!",
         "Pon vinagre en la ensalada."),
        ("largo", "ancho — ¡en español «largo» = lungo!",
         "La calle es muy ancha."),
        ("gamba", "pierna — ¡en español «gamba» = gambero!",
         "Me duele la pierna izquierda."),
        ("caldo", "caliente — ¡en español «caldo» = brodo!",
         "El café está muy caliente."),
        ("imbarazzata", "avergonzada — ¡español «embarazada» = incinta!",
         "Estoy avergonzada por lo que dije."),
        ("guardare", "mirar — ¡español «guardar» = tenere/conservare!",
         "Mira qué bonito el atardecer."),
        ("nonna", "abuela — no confundir con «nona» (novena)",
         "Mi abuela vive en el pueblo."),
        ("prossimo", "próximo / siguiente — ¡español «prójimo» sólo = «vecino» moral/religioso!",
         "El próximo tren sale a las nueve."),
        ("primo", "primero — ¡en español «primo» = cugino!",
         "Soy el primero de la fila."),
        ("tenere", "sujetar / mantener — ¡español «tener» = avere (posesión)!",
         "Sujétame la puerta un momento."),
        ("portare", "llevar / traer — español «portar» apenas se usa (llevar armas)",
         "Lleva el vino a la fiesta."),
        ("pronto", "listo (adj.) / diga, dígame (al teléfono) — ¡español «pronto» = presto!",
         "Ya está listo. / (al teléfono) ¿Diga?"),
        ("vaso", "jarrón / maceta — ¡español «vaso» (de beber) = bicchiere!",
         "El jarrón de flores está sobre la mesa."),
        ("macchina", "coche / carro — español «máquina» sólo = aparato mecánico",
         "El coche está aparcado en la calle."),
        ("sembrare", "parecer — ¡español «sembrar» = seminare (plantar)!",
         "Parece cansado hoy."),
        ("topo", "ratón — ¡español «topo» = talpa (animal que cava)!",
         "Hay un ratón en la cocina."),
    ],

    "Saluti e Cortesia": [
        ("ciao", "hola (al llegar) / adiós (al despedirse) — informal",
         "¡Hola! ¿Qué tal?"),
        ("salve", "hola (neutro, ni muy formal ni muy informal)",
         "Salve — Hola, ¿qué tal?"),
        ("buongiorno", "buenos días / buenas tardes (hasta media tarde)",
         "Buenos días, ¿cómo está usted?"),
        ("buonasera", "buenas tardes / buenas noches (al llegar, a partir de la tarde)",
         "Buenas tardes, señor."),
        ("buonanotte", "buenas noches (sólo al despedirse antes de dormir)",
         "Buenas noches, hasta mañana."),
        ("arrivederci", "adiós / hasta luego",
         "Adiós, nos vemos pronto."),
        ("a domani", "hasta mañana",
         "¡Hasta mañana!"),
        ("a dopo / a più tardi", "hasta luego / hasta después",
         "Hasta luego, tengo que irme."),
        ("per favore / per piacere", "por favor",
         "Un café, por favor."),
        ("grazie", "gracias",
         "Muchas gracias por todo."),
        ("prego", "de nada / por favor (invitando) / dígame",
         "—Gracias. —De nada."),
        ("scusa (tú) / mi scusi (usted)", "perdona (tú) / perdone (usted)",
         "Perdona, ¿qué hora es?"),
        ("come stai? / come sta?", "¿cómo estás? / ¿cómo está? / ¿qué tal?",
         "Hola, ¿cómo estás?"),
        ("piacere (di conoscerti)", "encantado/a (de conocerte)",
         "—Me llamo Ana. —Encantada."),
        ("come ti chiami?", "¿cómo te llamas?",
         "¿Cómo te llamas? Yo soy Marco."),
        ("mi chiamo…", "me llamo…",
         "Me llamo Sofía, ¿y tú?"),
    ],

    "Quantità e Grado": [
        ("molto", "mucho (con sustantivo/verbo) / muy (ante adjetivo o adverbio)",
         "Tengo mucha hambre. / Es muy alta."),
        ("poco", "poco",
         "Como poco por la noche."),
        ("troppo", "demasiado",
         "Es demasiado tarde para salir."),
        ("abbastanza", "bastante / suficiente",
         "Es bastante bueno, gracias."),
        ("quasi", "casi",
         "Casi termino, dame un minuto."),
        ("più", "más",
         "Quiero más agua, por favor."),
        ("meno", "menos",
         "Hoy hace menos frío que ayer."),
    ],
}


def build():
    d = fresh_skeleton()
    for name, cards in DECKS.items():
        add_deck(d, name)
        add_to(d, name, cards)

    working = REPO / "data" / "working.json"
    save(d, working)
    print(f"wrote {working}")
    inventory(d)


if __name__ == "__main__":
    build()
