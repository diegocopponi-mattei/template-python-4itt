"""
Modulo principale dell'applicazione.
Punto di partenza standard per le esercitazioni in Python - Classe 4ª ITT.

Autore: Nome Cognome
Data: GG/MM/AAAA
Versione: 1.0
"""


def stampa_intestazione(titolo: str) -> None:
    """Stampa a video un titolo incorniciato adattando la larghezza al testo.

    Args:
        titolo: Il testo da visualizzare come intestazione.
    """
    larghezza = max(41, len(titolo) + 4)
    print("=" * larghezza)
    print(f"  {titolo}")
    print("=" * larghezza)


def main() -> None:
    """Funzione principale (entry point) dell'applicazione."""
    
    stampa_intestazione("Titolo Esercizio")

    # TODO: Inserisci qui il codice dell'esercizio
    # Esempio di input/output:
    # nome = input("Inserisci il tuo nome: ")
    # print(f"Benvenuto/a, {nome}!")


if __name__ == "__main__":
    main()
