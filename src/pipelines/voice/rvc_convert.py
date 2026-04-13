"""
DAW-Ava — Singing Voice Conversion via RVC v2 sur Replicate
Usage :
  python rvc_convert.py train <dataset.zip>          Entrainer un modele vocal
  python rvc_convert.py convert <audio.mp3> <model>  Convertir une voix

Prerequis :
  - ReplicateAPI_KEY dans le registre Windows ou env var
  - pip install replicate
  - Echantillon vocal dans models/SVC/sample-myVoice/
"""

import sys
import os
import zipfile
import replicate
from pathlib import Path


def _ensure_replicate_token():
    """Charge ReplicateAPI_KEY depuis le registre Windows et le mappe vers REPLICATE_API_TOKEN (SDK)."""
    if os.environ.get("REPLICATE_API_TOKEN"):
        return
    # Chercher ReplicateAPI_KEY dans le registre et le mapper vers REPLICATE_API_TOKEN
    try:
        import winreg
        for root, subkey in [
            (winreg.HKEY_CURRENT_USER, "Environment"),
            (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
        ]:
            try:
                key = winreg.OpenKey(root, subkey)
                val, _ = winreg.QueryValueEx(key, "ReplicateAPI_KEY")
                winreg.CloseKey(key)
                os.environ["REPLICATE_API_TOKEN"] = val
                return
            except (FileNotFoundError, OSError):
                continue
    except ImportError:
        pass
    raise RuntimeError(
        "ReplicateAPI_KEY introuvable dans le registre Windows.\n"
        "Generer sur https://replicate.com/account/api-tokens\n"
        "Puis inscrire dans le registre Windows (Admin) :\n"
        '  [System.Environment]::SetEnvironmentVariable("ReplicateAPI_KEY", "<token>", "Machine")'
    )


def prepare_dataset(sample_dir, output_zip=None):
    """
    Prepare un dataset ZIP depuis les echantillons vocaux.
    Prend tous les WAV/MP3 dans sample_dir, les met dans un ZIP.
    """
    sample_dir = Path(sample_dir).resolve()
    if not sample_dir.exists():
        print(f"ERREUR : repertoire introuvable -- {sample_dir}")
        sys.exit(1)

    audio_files = list(sample_dir.glob("*.wav")) + list(sample_dir.glob("*.mp3"))
    if not audio_files:
        print(f"ERREUR : aucun fichier audio dans {sample_dir}")
        sys.exit(1)

    if output_zip is None:
        output_zip = sample_dir / "dataset.zip"
    else:
        output_zip = Path(output_zip).resolve()

    print(f"[1/1] Creation du dataset ZIP ({len(audio_files)} fichiers)...")
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in audio_files:
            zf.write(f, f"dataset/{f.name}")
            print(f"       + {f.name} ({f.stat().st_size / (1024*1024):.1f} Mo)")

    print(f"\nDataset pret : {output_zip} ({output_zip.stat().st_size / (1024*1024):.1f} Mo)")
    return output_zip


def train_model(dataset_zip_url, sample_rate="48k", epochs=50):
    """
    Entraine un modele vocal RVC v2 sur Replicate.
    dataset_zip_url : URL publique du ZIP (uploader sur Replicate ou HuggingFace)
    Retourne l'URL du modele entraine (.pth).
    Cout : ~$0.32, duree : ~6 min.
    """
    _ensure_replicate_token()

    print(f"[1/2] Lancement training RVC v2 sur Replicate...")
    print(f"       Dataset : {dataset_zip_url}")
    print(f"       Sample rate : {sample_rate}, Epochs : {epochs}")

    output = replicate.run(
        "replicate/train-rvc-model:cf360587a27f67500c30fc31de1e0f0f9aa26dcd7b866e6ac937a07bd104bad9",
        input={
            "dataset_zip": dataset_zip_url,
            "sample_rate": sample_rate,
            "version": "v2",
            "f0method": "rmvpe_gpu",
            "epoch": epochs,
            "batch_size": 7,
        }
    )

    print(f"[2/2] Training termine.")
    print(f"       Modele : {output}")
    return output


def convert_voice(audio_path, model_url, pitch_change=0, output_dir=None):
    """
    Convertit une voix chantee avec un modele RVC v2 entraine.
    audio_path : chemin local du stem vocal (MP3/WAV)
    model_url : URL du modele entraine (.pth)
    pitch_change : demi-tons (+/- 12 max). 0 = meme tonalite.
    Cout : ~$0.034, duree : ~3 min.
    """
    _ensure_replicate_token()

    audio_path = Path(audio_path).resolve()
    if not audio_path.exists():
        print(f"ERREUR : fichier introuvable -- {audio_path}")
        sys.exit(1)

    # Deduire le theme et le repertoire de sortie
    theme = audio_path.parent.name
    if output_dir is None:
        output_dir = Path(__file__).resolve().parent.parent.parent.parent / "output" / theme / "voice"
    else:
        output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] Upload de {audio_path.name}...")
    # Replicate accepte les fichiers locaux via open()
    with open(audio_path, "rb") as f:
        print(f"[2/3] Conversion RVC v2 en cours (pitch: {pitch_change:+d} demi-tons)...")
        output = replicate.run(
            "zsxkib/realistic-voice-cloning:0a9c7c558af4c0f20667c1bd1260ce32a2879944a0b9e44e0398660571c95571",
            input={
                "song_input": f,
                "rvc_model": "CUSTOM",
                "custom_rvc_model_download_url": model_url,
                "pitch_change": pitch_change,
                "f0method": "rmvpe",
                "index_rate": 0.5,
                "filter_radius": 3,
                "rms_mix_rate": 0.25,
                "protect": 0.33,
            }
        )

    # output est une URL vers le fichier audio converti
    import requests
    out_file = output_dir / f"{audio_path.stem}-rvc.wav"
    print(f"[3/3] Telechargement vers {out_file}...")
    r = requests.get(str(output))
    with open(out_file, "wb") as f:
        f.write(r.content)
    size_mb = len(r.content) / (1024 * 1024)
    print(f"\nTermine -- {out_file.name} ({size_mb:.1f} Mo)")
    return out_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage :")
        print("  python rvc_convert.py prepare <sample_dir>              Prepare dataset ZIP")
        print("  python rvc_convert.py train <dataset_zip_url>           Entraine modele vocal")
        print("  python rvc_convert.py convert <audio> <model_url>       Convertit voix")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "prepare":
        prepare_dataset(sys.argv[2])
    elif cmd == "train":
        train_model(sys.argv[2])
    elif cmd == "convert":
        pitch = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        convert_voice(sys.argv[2], sys.argv[3], pitch_change=pitch)
    else:
        print(f"Commande inconnue : {cmd}")
        sys.exit(1)
