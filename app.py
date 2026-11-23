"""
Modulo principale dell'applicazione.
Punto di partenza standard per le esercitazioni in Python per la classe 4ª ITT.

Autore: Nome Cognome
Versione: 1.0
"""

def stampa_intestazione(titolo: str) -> None:
    """
    Funzione di utilità che stampa a video un titolo incorniciato.

    :param titolo: Il testo da visualizzare come intestazione.
    """
    print("=" * 41)
    print(f"  {titolo}")
    print("=" * 41)


def main() -> None:
    """
    Funzione principale (entry point) dell'applicazione.
    """
    stampa_intestazione("Titolo Esercizio")

    # TODO: Inserisci qui il codice dell'esercizio
    # Esempio di lettura da tastiera:
    # nome = input("Inserisci il tuo nome: ")
    # print(f"Benvenuto/a, {nome}!")


if __name__ == "__main__":
    main()
