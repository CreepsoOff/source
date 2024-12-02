import os
import requests
import json
from urllib.parse import urlparse, unquote

# Liste des URLs
urls = [
    "https://esign.yyyue.xyz/app.json",
    "https://raw.githubusercontent.com/vizunchik/AltStoreRus/master/apps.json",
    "https://qnblackcat.github.io/AltStore/apps.json",
    "https://randomblock1.com/altstore/apps.json",
    "https://wuxu1.github.io/wuxu-complete-plus.json",
    "https://wuxu1.github.io/wuxu-complete.json",
    "https://ipa.cypwn.xyz/cypwn.json",
    "https://driftywinds.github.io/AltStore/apps.json",
    "https://hann8n.github.io/JackCracks/MovieboxPro.json",
    "https://raw.githubusercontent.com/TheNightmanCodeth/chromium-ios/master/altstore-source.json",
    "https://repo.apptesters.org/",
    "https://aio.yippee.rip/repo.json",
    "https://community-apps.sidestore.io/sidecommunity.json",
    "https://raw.githubusercontent.com/arichornloverALT/arichornloveralt.github.io/main/apps2.json",
    "https://raw.githubusercontent.com/arichornloveralt/arichornloveralt.github.io/main/apps.json",
    "https://raw.githubusercontent.com/lo-cafe/winston-altstore/main/apps.json",
    "https://qingsongqian.github.io/all.html",
    "https://tiny.one/SpotC",
    "https://theodyssey.dev/altstore/odysseysource.json",
    "https://provenance-emu.com/apps.json",
    "https://repo.starfiles.co/",
    "https://ish.app/altstore.json",
    "https://raw.githubusercontent.com/Balackburn/YTLitePlusAltstore/main/apps.json",
    "https://ipa.cypwn.xyz/cypwn_ts.json",
    "https://raw.githubusercontent.com/whoeevee/EeveeSpotify/swift/repo.json",
    "https://altstore.oatmealdome.me/",
    "https://alts.lao.sb/",
    "https://xitrix.github.io/iTorrent/AltStore.json",
    "https://driftywinds.github.io/repos/esign.json",
    "https://github.com/khcrysalis/Feather/raw/main/app-repo.json",
    "https://apps.nabzclan.vip/repos/esign.php",
    "https://flyinghead.github.io/flycast-builds/altstore.json",
    "https://alt.crystall1ne.dev/",
    "https://apps.sidestore.io/",
    "https://repos.yattee.stream/alt/apps.json",
    "https://alt.thatstel.la/"
]

def parse_folder_and_file(url):
    response = requests.head(url, allow_redirects=True)
    final_url = response.url
    parsed_url = urlparse(final_url)
    
    # Construire le chemin du dossier
    domain_parts = parsed_url.netloc.split(".")
    path_parts = parsed_url.path.strip("/").split("/")
    
    folder_parts = domain_parts + path_parts[:-1]  # Exclure le fichier s'il est explicite
    folder_name = "-".join([unquote(part) for part in folder_parts])
    
    # Identifier le fichier
    file_name = unquote(path_parts[-1]) if "." in path_parts[-1] else "apps.json"
    file_name = file_name.replace(" ", "-")
    
    return folder_name, file_name

def fetch_and_save_file(url):
    folder, file_name = parse_folder_and_file(url)
    response = requests.get(url, allow_redirects=True)
    if response.status_code != 200:
        print(f"Erreur : impossible de télécharger {url}")
        return
    
    content = response.text.strip()
    try:
        # Vérifier si le contenu est du JSON valide
        json.loads(content)
        is_json = True
    except json.JSONDecodeError:
        is_json = False

    # Sauvegarder uniquement si le contenu est du JSON valide
    if is_json:
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Fichier JSON sauvegardé : {file_path}")
    else:
        print(f"Le contenu de {url} n'est pas du JSON valide, ignoré.")

def main():
    for url in urls:
        fetch_and_save_file(url)

if __name__ == "__main__":
    main()
