
import chatterREFsrb

def nume(text):
    discutie = 'Drago mi je što se upoznajemo! ' + text + ', sjajno! U ovoj sesiji ću Vam pokazati svoje sposobnosti. ' \
                                                          'Iskreno se nadam da ćemo naučiti ponešto jedno od drugog. '
    return discutie

def convorbireIT(userText):
    if userText.lower() == "da":
        raspuns = "Počnimo! Molim Vas, unesite reč, sintagmu ili rečenicu kako bih mogao odgovoriti Vam. " \
                  "Napišite EXIT u slučaju da želite da napustite razgovor."
    elif userText.lower() == "ne":
        raspuns = "U redu, razumem, Čekaću! Ukucajte DA kada budete bili spremni. U suprotnome, razgovor će biti završen."
    else:
        raspuns = "Izvinite me, ali nisam siguran da sam razumeo! Ukucajte DA ili NE. " \
                  "Čekam na Vaš odgovor, ali se iskreno nadam da ćemo uskoro početi razgovor. Razgovor će u suprotnom biti završen."
    return raspuns

def convorbireREF(userText):
    if userText.lower() == "da":
        raspuns = "Počnimo! Molim Vas, unesite reč, sintagmu ili rečenicu kako bih mogao detektovati odgovarajuću referencu. " \
                  "Napišite Q u slučaju da želite da napustite razgovor."
    elif userText.lower() == "ne":
        raspuns = "U redu, razumem, Čekaću! Ukucajte DA kada budete bili spremni. U suprotnome, razgovor će biti završen."
    else:
        raspuns = "Izvinite me, ali nisam siguran da sam razumeo! Ukucajte DA ili NE. " \
                  "Čekam na Vaš odgovor, ali se iskreno nadam da ćemo uskoro početi razgovor. Razgovor će u suprotnom biti završen."
    return raspuns

def referinte(userText):
    return chatterREFsrb.response(userText)
