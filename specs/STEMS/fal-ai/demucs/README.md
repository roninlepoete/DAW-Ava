# Demucs — Separation de stems (Fal.ai)

## Endpoint
`fal-ai/demucs`

## Statut
**OPERATIONNEL** — teste le 2026-04-11 sur DestinyInYouInMe.mp3

## Parametres API

| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `audio_url` | string | OUI | URL du fichier audio (upload via `fal.upload.upload_file()`) |

## Format de reponse

Demucs retourne les 6 stems **directement a la racine** du dict (pas dans un sous-objet) :

```json
{
  "vocals":  {"url": "https://...", "content_type": "audio/mpeg", "file_name": "vocals.mp3",  "file_size": 12744664},
  "drums":   {"url": "https://...", "content_type": "audio/mpeg", "file_name": "drums.mp3",   "file_size": 12744664},
  "bass":    {"url": "https://...", "content_type": "audio/mpeg", "file_name": "bass.mp3",    "file_size": 12744664},
  "other":   {"url": "https://...", "content_type": "audio/mpeg", "file_name": "other.mp3",   "file_size": 12744664},
  "guitar":  {"url": "https://...", "content_type": "audio/mpeg", "file_name": "guitar.mp3",  "file_size": 12744664},
  "piano":   {"url": "https://...", "content_type": "audio/mpeg", "file_name": "piano.mp3",   "file_size": 12744664}
}
```

**Attention** : le format de sortie est MP3 (pas WAV). Chaque stem a la meme taille (~12.2 Mo pour un morceau de 3 min).

## Code Python (DAW-Ava)

```python
import sys
sys.path.insert(0, "C:/WSurfWSpaceGlobal/Core/Scripts/Skills/Python")
from fal.upload import upload_file, subscribe

audio_url = upload_file("input/DestinyInYouAndMe/DestinyInYouInMe.mp3")
result = subscribe("fal-ai/demucs", {"audio_url": audio_url})

for stem_name in ["vocals", "drums", "bass", "guitar", "piano", "other"]:
    url = result[stem_name]["url"]
    # telecharger url vers output/[theme]/stems/[stem_name].mp3
```

## Script pipeline

`src/pipelines/stems/separate.py`

## Cout

Pay-per-use Fal.ai. Test du 2026-04-11 : ~$0.05 pour un MP3 de 7 Mo (3 min).

## Pieges connus

1. Les stems sont a la racine du dict, pas dans `result["stems"]`
2. Le format de sortie est MP3, pas WAV
3. Chaque stem fait la meme taille (meme si le contenu est quasi-silencieux)
