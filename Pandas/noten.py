import argparse
import pandas as pd
import os
import re

def main():
    parser = argparse.ArgumentParser(description='noten.py by Emir Cajlakovic / HTL Rennweg')
    # Positionales Argument
    parser.add_argument('outfile', type=str, help='4-stellige Nummer), Da-')

    # Optionale Argumente
    parser.add_argument('-n', type=str, default=None, help='Setze N')
    parser.add_argument('-s', type=str, default=None, help='Setze S')
    parser.add_argument('-m', type=str, default="Nummer", help='Setze M')
    parser.add_argument('-f', type=str, default="SEW", help='Setze F')

    # Exklusive Gruppe für verbose/quiet
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true', help='Gibt die Daten auf der Kommandozeile aus')
    group.add_argument('-q', '--quiet', action='store_true', help='Keine Textausgabe')

    args = parser.parse_args()

    # check that args.n and s are set
    if args.n is None or args.s is None:
        print("Error: -n and -s must be set")
        return

    # Daten aus CSV-Datei einlesen
    df = pd.read_xml(args.n, sep=';')

    # Funktion zum Einlesen der XML-Datei aufrufen
    df_schueler = pd.read_xml(args.s)
    if args.f != "all":
        df = df[[args.f, args.m]]

    df = pd.merge(df, df_schueler, on=args.m)

    df.to_csv(args.outfile, sep=';', index=False)

    # write the data to a csv file
    if args.verbose:
        print(df)

def read_xml(filename: str) -> pd.DataFrame:
    """
    Liest die XML-Datei ein und extrahiert die Schülerdaten.

    Parameters:
    filename (str): Der Dateiname der XML-Datei.

    Returns:
    pd.DataFrame: Ein DataFrame mit den extrahierten Schülerdaten.
    """
    with open(filename, 'r') as f:
        xml_content = f.read().replace("\n", "")
        pattern = re.compile("<Schueler>.*?</Schueler>", flags=re.DOTALL)
        result = re.findall(pattern, xml_content)
        # Konvertiere die gefundenen Schülerdaten in ein DataFrame
        schueler_data = []
        for schueler_xml in result:
            nummer = re.search("<Nummer>(.*?)</Nummer>", schueler_xml).group(1)
            anrede = re.search("<Anrede>(.*?)</Anrede>", schueler_xml).group(1)
            vorname = re.search("<Vorname>(.*?)</Vorname>", schueler_xml).group(1)
            nachname = re.search("<Nachname>(.*?)</Nachname>", schueler_xml).group(1)
            geburtsdatum = re.search("<Geburtsdatum>(.*?)</Geburtsdatum>", schueler_xml).group(1)
            schueler_data.append([nummer, anrede, vorname, nachname, geburtsdatum])

        # Erstelle ein DataFrame aus den extrahierten Schülerdaten
        df_schueler = pd.DataFrame(schueler_data, columns=['Nummer', 'Anrede', 'Vorname', 'Nachname', 'Geburtsdatum'])
        return df_schueler

if __name__ == "__main__":
    main()

