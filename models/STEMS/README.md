# STEMS — Separation de sources audio

> Isoler les composantes d'un mix : voix, batterie, basse, guitare, piano, autres.

---

## Outils disponibles

| Outil | Fournisseur | Acces | Forces |
|-------|-------------|-------|--------|
| **Demucs** | Fal.ai | `fal-ai/demucs` | 6 stems, reference Meta, pay-per-use |
| ElevenLabs Audio Isolation | Fal.ai | `fal-ai/elevenlabs/audio-isolation` | Isole la voix uniquement (retire bruit/musique) |
| Kits.ai Vocal Separation | Kits.ai | API beta | Integre au pipeline SVC Kits.ai |

## Choix DAW-Ava

**Demucs** — operationnel, 6 stems, qualite reference. Voir `specs/STEMS/fal-ai/demucs/`.

## Cas d'usage

1. Extraire le stem vocal d'un morceau Suno pour le remplacer par la voix du Cap'taine (SVC)
2. Extraire les stems instrumentaux pour remixer dans le DAW
3. Isoler la batterie pour analyser le pattern rythmique
