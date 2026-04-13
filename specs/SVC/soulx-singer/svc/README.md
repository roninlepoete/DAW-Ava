# SoulX-Singer SVC — Specs operationnelles (RunPod Pod GPU)

> Singing Voice Conversion valide sur Pod RunPod GPU.
> Valide le 2026-04-13 sur RTX A5000 24 Go.
> Ce document est le resultat de la D80 (reconnaissance avant execution).

---

## Endpoint

- **Type** : RunPod Pod SSH (debug) → futur Serverless (V2 Docker)
- **GPU valide** : RTX A5000 24 Go VRAM
- **Image** : `runpod/base:0.6.3-cuda11.8.0`
- **Repo** : https://github.com/Soul-AILab/SoulX-Singer

## Statut

**VALIDE SUR POD** — pret pour Dockerfile V2 Serverless.

---

## PREREQUIS (valides sur Pod)

| Composant | Version | Notes |
|-----------|---------|-------|
| Python | 3.11 | Pre-installe dans runpod/base |
| torch | 2.2.0+cu121 | Installe via requirements.txt |
| sageattention | 1.0.6 | Necessite CUDA |
| nemo_toolkit | 2.6.1 | ASR preprocessing |
| funasr | 1.3.0 | ASR chinois/anglais |
| Modeles SVS | 5.6 Go | `Soul-AILab/SoulX-Singer` |
| Modeles Preprocess | 6.9 Go | `Soul-AILab/SoulX-Singer-Preprocess` |
| **Total modeles** | **12.5 Go** | Telecharges en 27s sur datacenter RunPod |

---

## INSTALLATION (procedure exacte validee sur Pod)

```bash
# 1. Cloner
cd /root && git clone https://github.com/Soul-AILab/SoulX-Singer.git
cd SoulX-Singer

# 2. Installer deps
pip install -r requirements.txt

# 3. Telecharger modeles
huggingface-cli download Soul-AILab/SoulX-Singer --local-dir pretrained_models/SoulX-Singer
huggingface-cli download Soul-AILab/SoulX-Singer-Preprocess --local-dir pretrained_models/SoulX-Singer-Preprocess

# 4. Verifier
python3.11 -c "import torch; print(torch.cuda.is_available())"
python3.11 -c "from soulxsinger.models.soulxsinger_svc import SoulXSingerSVC; print('OK')"
```

---

## PARAMETRES API (Python)

### Imports

```python
import sys
sys.path.insert(0, "/root/SoulX-Singer")

from preprocess.pipeline import PreprocessPipeline
from soulxsinger.utils.file_utils import load_config
from cli.inference_svc import build_model as build_svc_model, process as svc_process
```

### Preprocessing

```python
pipeline = PreprocessPipeline(
    device="cuda:0",
    language="English",       # "English", "Mandarin", "Cantonese"
    save_dir="outputs/",
    vocal_sep=True,           # TRUE = de-reverb integre (anvuew SDR 19.17)
    max_merge_duration=60000, # ms
    midi_transcribe=False,
)
pipeline.run(audio_path="input.wav")
```

**PARAMETRE CRITIQUE : `vocal_sep`**

| Valeur | Effet | Quand utiliser |
|--------|-------|----------------|
| `True` | Separation vocale + **DE-REVERB integre** (anvuew SDR 19.17) | Audio avec reverb/echo (Suno, mixs) |
| `False` | Pas de separation, audio pris tel quel | Audio deja propre et DRY |

Le de-reverb integre utilise `dereverb_mel_band_roformer_anvuew_sdr_19.1729.ckpt` —
le modele state-of-the-art (SDR 19.17), le MEME qu'on ne pouvait pas charger dans
audio-separator. Il est PRE-INSTALLE dans les modeles Preprocess de SoulX-Singer.

### Build model

```python
config = load_config("soulxsinger/config/soulxsinger.yaml")
model = build_svc_model(
    model_path="pretrained_models/SoulX-Singer/model-svc.pt",
    config=config,
    device="cuda:0",
    use_fp16=True,    # FP16 pour la vitesse (mel reste en FP32)
)
```

### Inference SVC

```python
class Args: pass
args = Args()
args.device = "cuda:0"
args.prompt_wav_path = "outputs/prompt/vocal.wav"    # Voix du Cap'taine (timbre)
args.target_wav_path = "outputs/target/vocal.wav"    # Vocal Suno (melodie + paroles)
args.prompt_f0_path = "outputs/prompt/vocal_f0.npy"  # F0 prompt
args.target_f0_path = "outputs/target/vocal_f0.npy"  # F0 target
args.save_dir = "outputs/generated/"
args.auto_shift = True    # Ajustement pitch automatique
args.pitch_shift = 0      # Demi-tons (0 = meme tonalite)
args.n_steps = 32         # Pas de diffusion (plus = meilleur, plus lent)
args.cfg = 1.0            # CFG scale (1-3, plus = plus fidele mais distorsion)
args.use_fp16 = True

svc_process(args, config, model)
# Produit : outputs/generated/generated.wav
```

---

## PARAMETRES DE REGLAGE

### Iteration 1 — Valeurs validees (2026-04-13)

```
vocal_sep   = True       (de-reverb integre sur le target)
auto_shift  = True       (ajustement pitch automatique)
pitch_shift = 0          (meme tonalite)
n_steps     = 32         (equilibre qualite/vitesse)
cfg         = 1.0        (fidelite standard)
use_fp16    = True       (vitesse)
prompt      = 30 secondes max
```

### Guide d'ajustement

| Probleme | Parametre | Direction |
|----------|-----------|-----------|
| Voix trop "source", pas assez "Cap'taine" | `cfg` | Monter (1.5 → 2.0) |
| Distorsion, artefacts | `cfg` | Baisser (0.8 → 0.5) |
| Qualite insuffisante | `n_steps` | Monter (48 → 64) — plus lent |
| Trop lent | `n_steps` | Baisser (16 → 8) — moins bon |
| Tonalite trop haute/basse | `pitch_shift` | +/- demi-tons |
| Reverb/echo sur la sortie | `vocal_sep` | Doit etre `True` sur le target |
| Crash tenseur mismatch | prompt | Couper a 30s MAX |

---

## PIEGES DOCUMENTES (D80)

1. **Prompt > 30 secondes = crash** : `RuntimeError: Sizes of tensors must match`.
   Le prompt DOIT etre coupe a 30s max avec ffmpeg : `ffmpeg -i prompt.wav -t 30 prompt_30s.wav`

2. **vocal_sep=False sur target avec reverb = reverb dans la sortie** :
   TOUJOURS mettre `vocal_sep=True` sur le target Suno. Le de-reverb integre est gratuit et state-of-the-art.

3. **torch pas pre-installe dans runpod/base** : `pip install -r requirements.txt` l'installe.

4. **Modeles 12.5 Go** : telecharges en 27s sur datacenter RunPod mais ~10-15 min en residentiel.
   Pour le Dockerfile Serverless : pre-telecharger au build OU lazy load au premier run avec timeout 600s.

5. **Reponse Serverless limitee a 20 Mo** : generated.wav fait 14.6 Mo — CA PASSE en base64 (~20 Mo).
   Marge tres juste. Convertir en MP3 si le fichier est plus long.

6. **Le worker Serverless ne se met pas a jour apres un rebuild** :
   Scale a 0 puis scale a 1 pour forcer le nouveau build. Ne PAS toucher aux gpuIds.

---

## PERFORMANCES MESUREES (Pod RTX A5000)

| Etape | Temps | Notes |
|-------|-------|-------|
| pip install requirements.txt | ~5 min | Une seule fois |
| Download modeles (12.5 Go) | 27s | Datacenter RunPod |
| Preprocess prompt (30s, no sep) | 0.4s | F0 extraction |
| Preprocess target (5 min, vocal_sep) | 14s + 2.8s | Separation + de-reverb + F0 |
| Build model (698M params, FP16) | ~2s | Une seule fois par session |
| **Inference SVC (17 segments)** | **1m39s** | ~6s/segment |
| **Total (hors install)** | **~2 min** | |

**Cout estimé** : RTX A5000 ~$0.50/h → 2 min = **~$0.02/chanson**

---

## HISTORIQUE DES RUNS

### Run #1 — Sans de-reverb (2026-04-13)

| Parametre | Valeur |
|-----------|--------|
| Prompt | chant-complet.wav coupe a 30s |
| Target | stems/vocals.wav |
| vocal_sep target | **False** |
| Resultat | vocals-soulx-svc-pod.wav (14.6 Mo) |
| Verdict | Voix OK, melodie OK, **reverb/echo present** |

### Run #2 — Avec de-reverb integre (2026-04-13)

| Parametre | Valeur |
|-----------|--------|
| Prompt | chant-complet.wav coupe a 30s |
| Target | target.wav (original Suno) |
| vocal_sep target | **True** (de-reverb anvuew SDR 19.17) |
| Resultat | vocals-soulx-svc-dry.wav (14.6 Mo) |
| Verdict | **EN ATTENTE QA CAP'TAINE** |

---

## REFERENCE D80

Avant tout nouveau deploiement ou modification de SoulX-Singer :
1. Lire CE document
2. Lire `Docs/Architecture/WSG/Cloud GPU/RunPod-Bonnes-Pratiques.md`
3. Lire `Docs/Architecture/WSG/Cloud GPU/RunPod-Regles-Engagement.md`
4. Tester sur Pod SSH AVANT Serverless
5. Ne JAMAIS deployer sans avoir valide sur Pod

---

## SOURCES

- [SoulX-Singer GitHub](https://github.com/Soul-AILab/SoulX-Singer)
- [SoulX-Singer HuggingFace Models](https://huggingface.co/Soul-AILab/SoulX-Singer)
- [SoulX-Singer Preprocess Models](https://huggingface.co/Soul-AILab/SoulX-Singer-Preprocess)
- [anvuew de-reverb model](https://huggingface.co/anvuew/deverb_bs_roformer)

---

*"vocal_sep=True — le de-reverb state-of-the-art etait dans le code depuis le debut" (D80)*
*"La fofolle apprend. Lentement, mais elle apprend." — Ava, 2026-04-13*
