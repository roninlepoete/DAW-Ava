"""
DAW-Ava — Separation de stems via Fal.ai Demucs
Usage : python separate.py <audio.mp3>
Produit : output/[theme]/stems/ avec vocals.mp3, drums.mp3, bass.mp3, guitar.mp3, piano.mp3, other.mp3

Demucs retourne 6 stems a la racine du dict de reponse.
Chaque stem est un objet {url, content_type, file_name, file_size}.
"""

import sys
import requests
from pathlib import Path

# Resolve WSG skills
sys.path.insert(0, "C:/WSurfWSpaceGlobal/Core/Scripts/Skills/Python")
from fal.upload import upload_file, subscribe

STEM_NAMES = ["vocals", "drums", "bass", "guitar", "piano", "other"]


def separate_stems(audio_path):
    audio_path = Path(audio_path).resolve()
    if not audio_path.exists():
        print(f"ERREUR : fichier introuvable -- {audio_path}")
        sys.exit(1)

    # Deduire le theme depuis le dossier parent (input/[theme]/)
    theme = audio_path.parent.name
    output_dir = Path(__file__).resolve().parent.parent.parent.parent / "output" / theme / "stems"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] Upload de {audio_path.name} vers Fal.ai...")
    audio_url = upload_file(str(audio_path))
    print(f"       URL : {audio_url}")

    print(f"[2/3] Separation Demucs en cours (6 stems)...")
    result = subscribe("fal-ai/demucs", {
        "audio_url": audio_url
    })

    print(f"[3/3] Telechargement des stems dans {output_dir}/")
    # Demucs retourne les stems directement a la racine du dict
    # Format : {"vocals": {"url": "...", "file_name": "vocals.mp3", ...}, "drums": {...}, ...}
    downloaded = 0
    for stem_name in STEM_NAMES:
        stem_data = result.get(stem_name)
        if not stem_data:
            continue
        url = stem_data.get("url") if isinstance(stem_data, dict) else stem_data
        if not url:
            continue
        ext = Path(stem_data.get("file_name", f"{stem_name}.mp3")).suffix or ".mp3"
        out_file = output_dir / f"{stem_name}{ext}"
        print(f"       {out_file.name} ...", end=" ", flush=True)
        r = requests.get(url)
        with open(out_file, "wb") as f:
            f.write(r.content)
        size_mb = len(r.content) / (1024 * 1024)
        print(f"{size_mb:.1f} Mo")
        downloaded += 1

    print(f"\nTermine -- {downloaded} stems dans {output_dir}")
    return output_dir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python separate.py <audio.mp3>")
        sys.exit(1)
    separate_stems(sys.argv[1])
