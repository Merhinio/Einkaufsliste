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
        item = input('was möchtest du entfernen ? ')
        if item in einkaufsliste:
            einkaufsliste.remove(input())
            print('Artikel wurde gelöscht! ')
        else:
            print('Artikel gibt es nicht! ')

    elif user_input.lower() == 'anzeigen lassen':
        print('In deiner Einkaufsliste befindet sich :', einkaufsliste, )
    elif user_input.lower() == 'beenden':
        break
        print('Das Programm ist zu Ende :) ')




