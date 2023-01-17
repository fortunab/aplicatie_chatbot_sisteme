from flask import Flask, render_template, request

import functii
import functiiRO
import functiiSRB
import manipulareYaml
import manipulareYamlRO
import manipulareYamlSRB

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/corpus")
def corpusul():
    return "AB"

# -------------------- ENGLISH CHATBOT ----------------------

@app.route("/detectare", methods=["GET"])
def detect_referinte():
    userText = request.args.get('msg')
    if userText.lower() == "q":
        return 'Well, you just saw how things are going. ' \
               'I detected references. It was a strange conversation, between a human and me. I am glad that I met you. ' \
               'Now, I have to work on my abilities. See you soon. ' \
               'If you have more questions or doubts, please comeback to the application. ' \
               'Bye!'
    return functii.referinte(userText)

@app.route("/name", methods=["GET"])
def name():
    userText = request.args.get('msg')
    return functii.nume(userText)
#render_template('nimic.html', userText=userText)

@app.route("/discut")
def dialog():
    userText = request.args.get('msg')
    return functii.convorbireIT(userText)

@app.route("/modificare")
def dialogModif():
    userText = request.args.get('msg')
    return functii.convorbireREF(userText)

@app.route("/ceva", methods=["GET"])
def ceva():
    cv = request.args.get('msg')
    return render_template("index.html", cv=cv)

#-------- CHATBOT LIMBA ROMANA ---------
@app.route('/lromana.html', methods=['GET', 'POST'])
def lromana():
    cv = request.args.get('msg')
    return render_template("lromana.html", cv=cv)

@app.route("/nume", methods=["GET"])
def nume():
    userText = request.args.get('msg')
    return functiiRO.nume(userText)

@app.route("/convers")
def convers():
    userText = request.args.get('msg')
    return functiiRO.convorbireIT(userText)

@app.route("/discut_modif")
def dialogRef():
    userText = request.args.get('msg')
    return functiiRO.convorbireREF(userText)

@app.route("/obtinere")
def raspBotului():
    userText = request.args.get('msg')
    if userText.lower() == "exit":
        return 'Deci, ați văzut cum funcționează lucrurile! ' \
               'Am discutat despre XAI și am purtat o conversație erudită! ' \
               'A fost o conversație destul de stranie pentru mine, deoarece am comunicat cu dumneavoastă, cu un om. ' \
               'Totuși, îmi pare bine că ne-am cunoscut. Data viitoare va trebuie să ne cunoaștem din nou, deoarece uit repede de oameni atunci când nu îi văd. Sunt doar o rațiune, nu și o persoană! ' \
               'Dacă mai aveți dubii, vă rog să reveniți. ' \
               'Ciaaaaaaao!'
    return manipulareYamlRO.convorbireXAI(userText)

@app.route("/detect")
def detectieReferinte():
    userText = request.args.get('msg')
    if userText.lower() == "q":
        return 'Deci, ați văzut cum funcționează lucrurile! ' \
               'Am detectat referințe asociate textului introdus de dumneavoastră. ' \
               'A fost o conversație destul de stranie pentru mine, deoarece am comunicat cu dumneavoastă, cu un om. ' \
               'Totuși, îmi pare bine că ne-am cunoscut. Data viitoare va trebuie să ne cunoaștem din nou, deoarece uit repede de oameni atunci când nu îi văd. Sunt doar o rațiune, nu și o persoană! ' \
               'Dacă mai aveți dubii, vă rog să reveniți. ' \
               'Ciaaaaaaao!'
    return functiiRO.referinte(userText)


# ----------- SRPSKI CHATBOT -------------

@app.route('/srpskijez.html', methods=['GET', 'POST'])
def srpskijez():
    cv = request.args.get('msg')
    return render_template("srpskijez.html", cv=cv)

@app.route("/detekcija")
def referenceDetekcija():
    userText = request.args.get('msg')
    if userText.lower() == "q":
        return 'Videli ste i sami kako funkcionišu stvari. ' \
               'Detektovao sam reference za unešeni tekst. Bio je to jedan pomalo i čudan razgovor između tebe, čoveka, i mene, bota. ' \
               'Ipak, drago mi je da smo se upoznali. ' \
               'Moram Vam reći da ću Vas pitati i naredni put za nadimak, jer slabo pamtim ljude sa kojima razgovaram jer ih ne vidim. ' \
               'Stoga, želim Vam sve najbolje i nadam se da ćeš ponovo da posetiš aplikaciju. ' \
               'Prijatno! Doviđenja!'
    return functiiSRB.referinte(userText)

@app.route("/ime", methods=["GET"])
def ime():
    userText = request.args.get('msg')
    return functiiSRB.nume(userText)
#render_template('nimic.html', userText=userText)

@app.route("/razgovor")
def razgovor():
    userText = request.args.get('msg')
    return functiiSRB.convorbireIT(userText)

@app.route("/izmene")
def dialogRefIzmene():
    userText = request.args.get('msg')
    return functiiSRB.convorbireREF(userText)

@app.route("/dobitak")
def odgovor_bota():
    userText = request.args.get('msg')
    if userText.lower() == "exit":
        return 'Videli ste i sami kako funkcionišu stvari. ' \
               'Upravo smo završili konverzaciju u kojoj smo pokazali da uistinu jesmo erudite. Bio je to jedan pomalo i čudan razgovor između tebe, čoveka, i mene, bota. ' \
               'Ipak, drago mi je da smo se upoznali. ' \
               'Moram Vam reći da ću Vas pitati i naredni put za nadimak, jer slabo pamtim ljude sa kojima razgovaram jer ih ne vidim. ' \
               'Stoga, želim Vam sve najbolje i nadam se da ćeš ponovo da posetiš aplikaciju. ' \
               'Ćaaaaooo! Doviđenja! Čujemo see!!!'
    return manipulareYamlSRB.convorbireXAI(userText)
# -- - - - -
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText.lower() == "exit":
        return 'Well, you just saw how things are going. ' \
               'I just talked with you about XAI and my reason. ' \
               'It was a strange conversation, between a human and me. I am glad that I met you. ' \
               'Now, I have to work on my abilities. See you soon. ' \
               'If you have more questions or doubts, please comeback to the application. ' \
               'Bye!'
    return manipulareYaml.convorbireXAI(userText)

if __name__ == "__main__":
    app.run()