# Specifications Operationnelles — DAW-Ava

> Catalogue des modeles utilises dans DAW-Ava, organises par type d'operation.
> Chaque modele a son README avec parametres API, code, couts et pieges connus.
> La documentation thematique (veille, comparatifs) est dans `models/`.

Date : 2026-04-11
Par : Ava Code en symbiose avec Cap'taine Fab

---

## Glossaire audio DAW-Ava

| Acronyme | Entree | Sortie | Description |
|----------|--------|--------|-------------|
| **STEMS** | 1 audio mix | 6 stems (vocals, drums, bass, guitar, piano, other) | Separation de sources audio |
| **SVC** | 1 audio chante + ref voix cible | 1 audio chante avec voix cible | Singing Voice Conversion — remplacer la voix |
| **MASTER** | 1 audio mix | 1 audio masterise + metriques | Mastering automatique (loudness, EQ, stereo) |
| **SYNC** | 1 video + texte | 1 audio synchronise | Generation audio synchronise sur video |
| **TTS** | texte + voix cible | 1 audio parle | Text-to-Speech, synthese vocale |
| **SFX** | texte descriptif | 1 audio effet sonore | Generation d'effets sonores |
| **MUSIC** | texte/paroles | 1 audio musique | Generation musicale |

---

## Table de routage — quel modele pour quel besoin

| Capacite | Modele actif | Endpoint | Statut | Specs |
|----------|-------------|----------|--------|-------|
| STEMS | Demucs | `fal-ai/demucs` | OPERATIONNEL | `specs/STEMS/fal-ai/demucs/` |
| SVC | A determiner | — | EN VEILLE | `specs/SVC/` |
| MASTER | Dolby.io | Dolby.io REST | A INTEGRER | `specs/MASTER/dolby-io/` |
| SYNC | MMAudio V2 | `fal-ai/mmaudio-v2` | A INTEGRER | `specs/SYNC/fal-ai/mmaudio-v2/` |
| TTS | Kokoro / ElevenLabs | `fal-ai/kokoro` / `fal-ai/elevenlabs/tts` | A INTEGRER | `specs/TTS/fal-ai/` |
| SFX | ElevenLabs SFX v2 | `fal-ai/elevenlabs/sound-effects/v2` | A INTEGRER | `specs/SFX/fal-ai/elevenlabs-sfx/` |
| MUSIC | MiniMax Music 2.0 | `fal-ai/minimax-music/v2` | A INTEGRER | `specs/MUSIC/fal-ai/minimax/` |

---

## Structure des specs

```
specs/
  README.md                          (ce fichier — table de routage)
  STEMS/
    fal-ai/demucs/README.md          OPERATIONNEL
  SVC/
    elevenlabs/                      A tester (voice changer via Fal.ai)
    seed-vc/                         A deployer (zero-shot, 44kHz chant)
    kits-ai/                         A demander acces API (specialiste SVC)
  MASTER/
    dolby-io/                        A integrer
  SYNC/
    fal-ai/mmaudio-v2/               A integrer
  TTS/
    fal-ai/                          A integrer
  MUSIC/
    fal-ai/minimax/                  A integrer
  SFX/
    fal-ai/elevenlabs-sfx/           A integrer
  FinOps/                            Suivi budgetaire (a creer)
```
