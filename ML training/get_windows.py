import cv2
import os
import random
import uuid

def generar_finestres(path_input, path_output, res=64, num_crops=10):
    # Crear carpeta de sortida si no existeix
    if not os.path.exists(path_output):
        os.makedirs(path_output)
        print(f"Carpeta creada: {path_output}")

    # Extensions d'imatge vàlides
    extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    imatges = [f for f in os.listdir(path_input) if f.lower().endswith(extensions)]

    if not imatges:
        print("No s'han trobat imatges a la carpeta d'entrada.")
        return

    print(f"Processant {len(imatges)} imatges...")

    for nom_fitxer in imatges:
        img_path = os.path.join(path_input, nom_fitxer)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Error llegint: {nom_fitxer}")
            continue

        h, w = img.shape[:2]

        # Comprovar si la imatge és prou gran per a la finestra
        if h < res or w < res:
            print(f"Imatge massa petita: {nom_fitxer} ({w}x{h})")
            continue

        for i in range(num_crops):
            # Generar coordenades aleatòries (evitant sortir dels marges)
            x = random.randint(0, w - res)
            y = random.randint(0, h - res)

            # Fer el retall (crop)
            crop = img[y:y+res, x:x+res]

            # Generar un nom únic per evitar sobreescriure si es repeteixen noms originals
            nom_sortida = f"crop_{uuid.uuid4().hex[:8]}_{nom_fitxer}"
            cv2.imwrite(os.path.join(path_output, nom_sortida), crop)

    print(f"Fet! Els retalls s'han guardat a: {path_output}")

# --- CONFIGURACIÓ ---
path_entrada = './originals/negatives'  # Canvia-ho pel teu path
path_sortida = './all_filtered/negatives' # On es guardaran els retalls
resolucio = 256                    # Mida de la finestra (64x64)
crops_per_foto = 158               # Quants trossets agafar de cada imatge

# Executar
generar_finestres(path_entrada, path_sortida, resolucio, crops_per_foto)