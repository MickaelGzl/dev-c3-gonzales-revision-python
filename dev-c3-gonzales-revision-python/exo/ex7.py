import os

filePath = os.path.join(os.path.dirname(__file__), '../file/')

def readFile(filename):
    try:
        file = open(filePath + filename, 'r', encoding='utf8')
        content = file.read()
        newFile = open(filePath + "result.txt", "a")
        newFile.write(f"Il y a {len(content.split(' '))} mots dans votre fichier texte \n")
        newFile.write("Contenu: " + content + '\n \n')
        print('Ecriture du nombre de mots et du contenu dans un nouveau fichier réussi.')
    except Exception as e:
        print(f'Aucun fichier trouvé nommé {filename}')

readFile(input('Entrez le nom de votre fichier: '))