alphabet = "abcdefghijklmnopqrstuvwxyz"


def vigenere(message, cle):
    def char_position(letter):
        return ord(letter) - 97  # ord et char des fonction de python

    def pos_to_char(index):
        return chr(index + 97)

    chiffrement = ""

    # la on devise le message de position 0 a la taille de la clé , faire cette operation plusieures fois
    # avec la boucle for : i la position sur le message , len(message) la fin du message , len(cle): le pas de la boucle

    message_divise = [
        message[i: i + len(cle)] for i in range(0, len(message), len(cle))
    ]

    for chaque_bloc in message_divise:
        # la chque bloc qu'on a divisé on le fait un parcours lettre par lettre
        j = 0
        for letter in chaque_bloc:
            if(letter==" "):
                chiffrement += " "
            else:
                # on convertit l'index de chaque lettre dans le bloc et dans la clé
                # avec la fonction 'char_position' pour voir sa vrai position dans l'alphabet
                # on additionne les index puis % 26 donc on aura l'index de la lettre chiffré dans l'alphabet
                index = (char_position(letter) + char_position(cle[j])) % len(alphabet)
                chiffrement += pos_to_char(index)
                # convertire l'index a une lettre avec la fonction pos_to_char et additionner le resultat
            j += 1

    return chiffrement


# la on fait le contraire pour le dechiffrement
def dechiffrement_vigenere(cipher, cle):
    def char_position(letter):
        return ord(letter) - 97

    def pos_to_char(index):
        return chr(index + 97)

    m_dechiffrer = ""
    message_chiffre_divise = [
        cipher[i: i + len(cle)] for i in range(0, len(cipher), len(cle))
    ]

    for bloc_chiffre in message_chiffre_divise:
        j = 0
        for letter in bloc_chiffre:
            if (letter == " "):
                m_dechiffrer += " "
            else:
                index = (char_position(letter) - char_position(cle[j])) % len(alphabet)
                m_dechiffrer += pos_to_char(index)
            j += 1

    return m_dechiffrer


def main():
    message = input("entrez votre message : ")
    cle = input("entrez la clé : ")
    message_chiffre = vigenere(message, cle)
    message_dechiffrer = dechiffrement_vigenere(message_chiffre, cle)

    print("le message chiffre est : " + message_chiffre)
    print("dechiffrement  : " + message_dechiffrer)


main()