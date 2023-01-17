
import chatterREFro


def nume(text):
    discutie = 'Îmi pare bine să te cunosc, ' + text + '. Acum că ne cunoaștem, îți voi prezenta abilitățile mele.'
    return discutie

def convorbireIT(userText):
    if userText.lower() == "da":
        raspuns = "Să începem atunci! V-aș ruga să introduceți un cuvânt, o sintagmă sau o propoziție. Tastați EXIT pentru a termina această conversație!"
    elif userText.lower() == "nu":
        raspuns = "Înteleg, voi aștepta! Tastați DA dacă sunteți pregătiți. Dacă nu, semnalați-mi, vă rog, " \
                  "acest lucru și conversația va fi terminată. Astfel, vă voi lăsa să vă adresați atunci când sunteți disponibili."
    else:
        raspuns = "Îmi cer scuze, dar nu am înțeles! Tastați cu DA sau NU. " \
                  "Voi aștepta răspunsul dumneavoastră, însă, sincer, mă aștept să acceptați. În caz contrar, conversația se va termina."
    return raspuns

def convorbireREF(userText):
    if userText.lower() == "da":
        raspuns = "Să începem atunci! V-aș ruga să introduceți un cuvânt, o sintagmă sau o propoziție pentru ca să pot găsi referința. Tastați Q pentru a termina această conversație!"
    elif userText.lower() == "nu":
        raspuns = "Înteleg, voi aștepta! Tastați DA dacă sunteți pregătiți. Dacă nu, semnalați-mi, vă rog, " \
                  "acest lucru și conversația va fi terminată. Astfel, vă voi lăsa să vă adresați atunci când sunteți disponibili."
    else:
        raspuns = "Îmi cer scuze, dar nu am înțeles! Tastați cu DA sau NU. " \
                  "Voi aștepta răspunsul dumneavoastră, însă, sincer, mă aștept să acceptați. În caz contrar, conversația se va termina."
    return raspuns

def referinte(userText):
    return chatterREFro.response(userText)