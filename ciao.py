print("\nCiao mondo, sono Ron!😊")

messaggio_simpatico = "Oggi me sento particolarmente bene!"
print(messaggio_simpatico)

cibo_preferito = "il mascarpone"
print("\nIl mio cibo preferito è " + cibo_preferito)

print("\nHey tu come ti chiami?")
nome = input()
print("\nCiao" + nome + "dispiacere di conoscerti")

if(nome == "Roney"):
    print("\nMa che bel nome!!!")
else:
    print("\nbellissimo nome, complimenti ai tuoi genitori...(adottivi)")

lunghezza_nome = len(nome)
lunghezza_nome_stringa = str(lunghezza_nome)
print("il tuo nome ha" + lunghezza_nome_stringa + "lettre")

anno_di_nascita = input("In che anno sei nato?")
anno_di_nascita_int = int(anno_di_nascita)
anno_corrente = input("in che anno ci troviamo?")
anno_corrente_int = int(anno_corrente)
eta = anno_corrente_int - anno_di_nascita_int
print(nome + "hai esattamente" + str(eta) + "anni...")

if(eta < 18):
    print("...beato te!")
    anni_da_compiere = eta + 1
    print("\nL'anno prossimo avrai " + str(anni_da_compiere) + "anni")
else:
    print("...sei proprio un vecchieto! :P")
    eta_silente = 150
    print("tra" + str(eta_silente - eta) + "anni, sarai vecchio come Albus Silente")
  
risposta = ""
while(risposta != "chi è?"):
    print("\ntoc toc...")
    risposta = input()
print("\nSono Francesco!")
  
animali = ["gatto", "canne", "topignao", "cleopardo", "catoblepa"]
print("\nQual è il tuo animale preferito?")
for animale in animali:
    print(animale)
print("...Indicalo con un numero di 0 a 4")
numero_animale = int(input())
if(numero_animale < 0 or numero_animale > 4):
    print("Non hai capito una se*****")
else:
    animale_scelto = animali[numero_animale]
    print(animale_scelto + "...ottima scelta!!")
