# audio-separator — De-reverb local (CPU, gratuit)

> Suppression de reverb sur stems vocaux via modeles UVR/MDX-Net.
> Tourne en local sur le PC du Cap'taine, zero cout API.
> Date : 2026-04-12

---

## Endpoint

Local — `pip install audio-separator`
Pas d'API cloud. Execution CPU.

## Statut

**OPERATIONNEL** — teste le 2026-04-12 sur DestinyInYouInMe vocals.

## Installation

```
pip install audio-separator
```

Le modele est telecharge automatiquement au premier lancement dans `/tmp/audio-separator-models/`.

## Modeles de de-reverb disponibles

| Modele | Architecture | Qualite | Taille |
|--------|-------------|---------|--------|
| **Reverb_HQ_By_FoxJoy.onnx** | MDX-Net | VALIDE Cap'taine | 66.8 Mo |
| UVR-DeEcho-DeReverb.pth | VR Arch | Bon all-rounder | — |
| UVR-De-Echo-Aggressive.pth | VR Arch | Agressif | — |
| De-Reverb Super Big by Sucial | MelBand Roformer | State-of-the-art | ~200 Mo |
| De-Reverb-Echo V2 by Sucial | MelBand Roformer | Excellent | — |

**Modele actif** : `Reverb_HQ_By_FoxJoy.onnx` (valide, rapide en CPU).
**A tester** : `De-Reverb Super Big by Sucial` (MelBand Roformer, potentiellement meilleur mais plus lourd).

## Code Python

```python
from audio_separator.separator import Separator

separator = Separator(
    output_dir="output/[theme]/voice",
    output_format="wav",
)

separator.load_model(model_filename="Reverb_HQ_By_FoxJoy.onnx")

result = separator.separate("output/[theme]/stems/vocals.wav")
# Produit 2 fichiers :
#   vocals_(No Reverb)_Reverb_HQ_By_FoxJoy.wav  → renommer en vocals-dry.wav
#   vocals_(Reverb)_Reverb_HQ_By_FoxJoy.wav      → renommer en vocals-reverb-only.wav
```

## Parametres

| Parametre | Defaut | Description |
|-----------|--------|-------------|
| `output_dir` | `.` | Repertoire de sortie |
| `output_format` | `wav` | Format de sortie |
| `model_filename` | — | Nom du modele a charger |

## Sortie

| Fichier | Contenu |
|---------|---------|
| `vocals_(No Reverb)_*.wav` | **Voix seche** — signal vocal sans reverb. INPUT pour le SVC |
| `vocals_(Reverb)_*.wav` | **Reverb extraite** — la reverb seule (utile pour re-mixer) |

## Performance

| Metrique | Valeur |
|----------|--------|
| Duree traitement | ~3 min 51 sec pour 5 min 18 sec d'audio |
| Hardware | CPU (Intel i7, pas de GPU) |
| Qualite sortie | 24-bit WAV |
| Cout | $0 |

## Pipeline valide

```
input/[theme]/[theme].mp3
  → cjwbw/demucs htdemucs_ft stem=vocals (Replicate, $0.023)
    → audio-separator Reverb_HQ_By_FoxJoy (local, $0)
      → vocals-dry.wav
        → zsxkib/realistic-voice-cloning (Replicate, $0.034)
          → vocals-rvc-iter5.wav (voix du Cap'taine)
```

## Pieges connus

1. Les fichiers de sortie ont des noms longs avec parentheses : `vocals_(No Reverb)_Reverb_HQ_By_FoxJoy.wav`. Renommer immediatement.
2. Le repertoire de sortie doit exister AVANT le lancement (pas de mkdir automatique).
3. En mode CPU, le traitement est ~4x plus lent qu'avec GPU. Acceptable pour des morceaux de 5 min.
4. Le modele est telecharge dans `/tmp/` — peut etre supprime par un nettoyage systeme. Il sera re-telecharge au prochain lancement.

---

*Specs DAW-Ava — de-reverb local, zero cout, qualite validee*
