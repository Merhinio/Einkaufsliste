# Tuple sind fasst genau wie listen nur sie sind Immutable und werden mit runden klammer
Liste = ('Banane', 'Mohrrüben', 'Trauben')
print(Liste)

# Schleifen

einkaufsliste = []

while True:
    user_input = input('Möchtest du was hinzufügen, entfernen oder anzeigen lassen? : ')

    if user_input.lower() == 'hinzufügen':
        item = input('was möchtest du hinzufügen? ')
        einkaufsliste.append(item)
        print(item, 'wurde hinzugefügt! ')


    elif user_input.lower() == 'entfernen':
        if not einkaufsliste:
            print('Die Liste ist Leer da gibt es nichts zu entfernen.')
        else:
            item = input('Was möchtest du entfernen ?')
            if item in einkaufsliste:
                einkaufsliste.remove(item)
                print('Artikel wurde gelöscht ')




    elif user_input.lower() == 'anzeigen lassen':
        print('In deiner Einkaufsliste befindet sich :', einkaufsliste, )
    elif user_input.lower() == 'beenden':

        print('Das Programm ist zu Ende :) ')
