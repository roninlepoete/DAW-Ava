# Seed-VC — Zero-shot Singing Voice Conversion (open source)

> Meilleur SVC zero-shot open source. Pas d'entrainement, 10-30s de reference suffisent.
> Date de veille : 2026-04-12
> Source : https://github.com/Plachtaa/seed-vc

---

## CE QUE C'EST

Modele open source de voice conversion base sur des diffusion transformers.
Mode singing dedie a 44.1 kHz avec conditionnement F0 (pitch).
Zero-shot : pas d'entrainement de modele, juste un echantillon de reference.

---

## FICHE TECHNIQUE

| Critere | Detail |
|---------|--------|
| **GitHub** | https://github.com/Plachtaa/seed-vc |
| **Statut** | ARCHIVE (nov 2025) — code fonctionnel, plus maintenu |
| **Licence** | Open source |
| **Zero-shot** | OUI — 10 a 30 secondes de voix reference |
| **Mode chant** | OUI — mode singing dedie, conditionnement F0 |
| **Sample rate** | 22050 Hz (parole), **44100 Hz (chant)** |
| **Pitch shift** | Par demi-tons (transposition) |
| **Vocoder** | BigVGAN (optimise voix aigues) |
| **GPU** | RTX 3060 suffisant (~6 Go VRAM) |
| **Latence** | ~150ms/chunk en inference |
| **Benchmarks** | Surpasse RVC v2 en similarite vocale et intelligibilite (zero-shot) |
| **Demo** | https://huggingface.co/spaces/Plachta/Seed-VC |

---

## ECHANTILLON VOCAL REQUIS

| Parametre | Valeur |
|-----------|--------|
| **Duree** | 10 a 30 secondes |
| **Format** | WAV ou MP3 |
| **Contenu** | Voix chantee seule (idealement) ou parlee |
| **Qualite** | Propre, sans bruit de fond, sans reverb |
| **Entrainement** | AUCUN — le modele generalise a partir de la reference |

---

## DEPLOIEMENT

| Option | Detail |
|--------|--------|
| VPS Linux (31.220.84.152) | Si GPU disponible (~6 Go VRAM) |
| RunPod | GPU cloud a la demande |
| HuggingFace Space | Demo en ligne (pas pour production) |
| FastAPI wrapper | `app_svc.py` adaptable en API REST |

---

## VERDICT POUR DAW-AVA

**Statut : BACKUP OPEN SOURCE**

**Forces** :
- Zero-shot (10-30s de voix suffisent — test immediat)
- Mode singing dedie 44.1 kHz
- Gratuit
- Surpasse RVC v2 en benchmarks zero-shot

**Faiblesses** :
- Archive (plus de mises a jour)
- Self-hosted uniquement (pas de cloud API managee)
- Necessite GPU (pas possible sur WSG Windows sans GPU)
- Pas de retours terrain de producteurs pro
- Qualite potentiellement inferieure a un modele entraine (RVC, Voice-Swap)

---

## SOURCES

- [Seed-VC GitHub](https://github.com/Plachtaa/seed-vc)
- [Demo HuggingFace](https://huggingface.co/spaces/Plachta/Seed-VC)

---

*Veille DAW-Ava — fournisseur SVC open source*
