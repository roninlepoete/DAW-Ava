# De-reverb Cloud — HuggingFace Space Politrees/audio-separator_UVR

> De-reverb et de-echo via Gradio API sur cloud GPU HuggingFace.
> Skill WSG : `Core/Scripts/Skills/Python/hf/audio.py`
> Date : 2026-04-12

---

## Endpoint

HuggingFace Space : `Politrees/audio-separator_UVR`
API : Gradio Client (`gradio_client` Python)
GPU : Cloud (community GPU, gratuit)

## Statut

**OPERATIONNEL** — teste le 2026-04-12

## Cout

**Gratuit** (community GPU, file d'attente possible).
$10 credit HuggingFace disponible si upgrade necessaire.

## Installation

```
pip install gradio_client
```

## Code Python (via skill WSG)

```python
import sys
sys.path.insert(0, "C:/WSurfWSpaceGlobal/Core/Scripts/Skills/Python")
from hf.audio import dereverb, dereverb_chain

# Simple : un modele
dereverb("vocals.wav", "output/voice/", model="UVR-De-Echo-Aggressive")

# Chain : de-echo + de-reverb en 2 passes
dereverb_chain("vocals.wav", "output/voice/")
```

## Modeles disponibles

| Modele | Architecture | Force |
|--------|-------------|-------|
| `UVR-De-Echo-Aggressive` | VR Arch | De-echo agressif |
| `UVR-DeEcho-DeReverb` | VR Arch | De-echo + de-reverb combine |
| `Reverb_HQ_By_FoxJoy` | MDX-Net | De-reverb HQ (valide localement) |
| `MDX23C-De-Reverb` | MDX23C | De-reverb |
| `BS-Roformer-De-Reverb` | BS-Roformer | De-reverb haute qualite |
| `De-Reverb-Echo-MelBand-Roformer-V2-Sucial` | MelBand Roformer | State-of-the-art |

## Fallback

Si le Space HuggingFace est down ou lent : `audio-separator` local (CPU).
`pip install audio-separator` → memes modeles en local.

---

*Specs DAW-Ava — de-reverb cloud HuggingFace*
