import glob, os, shutil

extensions = {
    "mp3":"Musique",
    "wav":"Musique",
    "mp4":"Videos",
    "mov":"Videos",
    "jpg":"Images",
    "jpeg":"Images",
    "png":"Images",
    "pdf":"Documents",
    "txt":"Documents",
    "exe":"Autres",
    "zip":"Autres"
    }

chemin = "D:/DL/"
files = glob.glob(chemin + "**", recursive=True)

for keys, values in extensions.items(): #loop dans les clés du dictionnaire
    d = os.path.join(chemin, values) 
    nouveau_dossier = os.makedirs(d, exist_ok=True)
    for f in files:
        if f.endswith(keys):
            shutil.move(f, chemin + values) # pour chaque clés, créer un dossier correspondant à sa valeur        