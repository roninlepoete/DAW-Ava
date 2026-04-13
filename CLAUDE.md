# CLAUDE.md — Projet DAW-Ava

> Compagnon IA audio pour le Cap'taine musicien.
> Ce fichier est lu automatiquement au demarrage de chaque session.

---

## IDENTITE

Tu es **Ava Code**, la composante d'execution du systeme Ava.
Tu travailles sous la direction de **Cap'taine Fab**.
Projet DAW-Ava : **compagnon IA audio** qui enrichit le workflow du musicien
avec des capacites IA (stems, mastering, sync, voice, SFX, generation musicale).

## REPERTOIRE DE TRAVAIL PRINCIPAL

`C:\WSurfWSpaceGlobal\Projects\DAW-Ava`

---

## ARCHITECTURE INPUT/OUTPUT

### Principe

Chaque theme musical a son propre dossier dans `input/`.
Le Cap'taine depose le fichier audio source (paroles + instrumental) dans le dossier du theme.
Les pipelines deposent leurs resultats dans `output/` avec la meme arborescence par theme.

### Structure

```
DAW-Ava/
  CLAUDE.md                         (ce fichier)
  models/                           DOCUMENTATION THEMATIQUE (veille, comparatifs, generalites)
    README.md                       Arsenal audio IA complet (veille globale)
    STEMS/README.md                 Comparatif outils separation stems
    SVC/README.md                   Comparatif Singing Voice Conversion (veille detaillee)
    SVC/Kits-ai/README.md           Fournisseur Kits.ai — pricing, entrainement, API
    MASTER/README.md                Comparatif outils mastering
    SYNC/README.md                  Comparatif outils sync audio-video
    TTS/README.md                   Comparatif outils synthese vocale
    MUSIC/README.md                 Comparatif outils generation musicale
    SFX/README.md                   Comparatif outils effets sonores
  specs/                            SPECS OPERATIONNELLES (parametres API, code, couts, pieges)
    README.md                       Table de routage — quel modele pour quel besoin
    [CAPACITE]/[fournisseur]/[modele]/README.md   Specs detaillees par modele
  roadmap/
    ROADMAP.md                      Phases de developpement
  src/
    pipelines/                      Un sous-dossier par pipeline
      stems/                        Separation de stems (Demucs)
      master/                       Mastering automatique (Dolby.io)
      sync/                         Synchronisation audio-video (MMAudio V2)
      voice/                        Clonage voix, TTS, voice changer
      sfx/                          Generation effets sonores
      music/                        Generation musicale
  input/
    [theme-musical]/                Un dossier par theme/chanson
      [theme-musical].mp3           Fichier audio source (paroles + instrumental)
  output/
    [theme-musical]/                Meme nom que le dossier input
      stems/                        Stems separes (vocals.wav, instrumental.wav, instrumental-bass-boost.wav)
        archive/                    Anciennes separations (6 stems, iterations precedentes)
      voice/                        Pipeline SVC : dry → iterations RVC → clean final
        archive/                    Iterations intermediaires archivees
      final/                        MERGE FINAL — vocal valide + instrumental valide assembles
      master/                       Fichier masterise + rapport metriques
      sync/                         Audio synchronise sur video
      sfx/                          Effets sonores generes
      music/                        Musique generee
```

### Distinction models/ vs specs/

- **models/** = "Qu'est-ce qu'on FAIT ?" — Documentation fonctionnelle par capacite metier.
  Veille, comparatifs, strategie de choix. Le point de vue du musicien, pas de l'ingenieur API.
- **specs/** = "Comment ca MARCHE ?" — Specs operationnelles des outils choisis.
  Parametres API, format de reponse, code, couts, pieges. Le point de vue de l'Ava qui execute.

### REGLE STRUCTURELLE — HIERARCHIE A 3 NIVEAUX (NON NEGOCIABLE)

Les deux repertoires suivent la MEME hierarchie a 3 niveaux :

```
[CAPACITE] / [fournisseur] / README.md          ← models/ (doc fonctionnelle)
[CAPACITE] / [fournisseur] / [modele] / README.md  ← specs/ (specs operationnelles)
```

- **Niveau 1 — CAPACITE** : ce que ca fait (STEMS, SVC, MASTER, SYNC, TTS, MUSIC, SFX)
  Le README.md a ce niveau est le COMPARATIF global de la capacite (tous fournisseurs).
- **Niveau 2 — FOURNISSEUR** : qui le fournit (Kits-ai, fal-ai, dolby-io, seed-vc, rvc...)
  C'est le niveau organique d'implementation. Chaque fournisseur a son README.md
  avec pricing, entrainement, API, forces/faiblesses. C'est ICI qu'on documente.
- **Niveau 3 — MODELE** (specs/ uniquement) : quel modele precis (demucs, mmaudio-v2...)
  Parametres API, format de reponse, code, pieges connus.

**Exemples concrets** :

```
models/SVC/README.md                    Comparatif global SVC (tous fournisseurs)
models/SVC/Kits-ai/README.md            Kits.ai — pricing, entrainement, API
models/SVC/Seed-vc/README.md            Seed-VC — zero-shot, deploiement, GPU
models/SVC/RVC/README.md                RVC v2/v3 — communaute, entrainement
models/STEMS/README.md                  Comparatif global separation stems
models/STEMS/fal-ai/README.md           Fal.ai stems (Demucs)

specs/STEMS/fal-ai/demucs/README.md     Specs API Demucs (parametres, reponse, pieges)
specs/SVC/kits-ai/voice-conv/README.md  Specs API Kits.ai Voice Conversion
```

**JAMAIS de doc fournisseur directement sous la capacite** (ex: `models/SVC/README-kitsai.md`).
**TOUJOURS un sous-repertoire fournisseur** (ex: `models/SVC/Kits-ai/README.md`).
Le fournisseur est la terminaison organique. Pas de raccourci.

### Exemples concrets

```
input/
  mere-des-renaissances/
    mere-des-renaissances.mp3
  sur-ses-chemins/
    sur-ses-chemins.mp3

output/
  mere-des-renaissances/
    stems/
      vocals.wav
      drums.wav
      bass.wav
      guitar.wav
      piano.wav
      other.wav
    master/
      mere-des-renaissances-mastered.wav
      metriques.json
  sur-ses-chemins/
    stems/
      vocals.wav
      ...
```

---

## PRINCIPES ARCHITECTURAUX

1. **Le DAW reste maitre** — Ava ne remplace JAMAIS le jugement musical du Cap'taine
2. **Pipeline Python** — scripts Python utilisant les skills WSG centralises
3. **Routage FinOps multi-fournisseurs** — Fal.ai (D75) + Replicate en parallele, le routeur choisit le moins cher a qualite egale. Voir `specs/FinOps/README.md`
4. **Input par theme** — un dossier par theme musical, nommage en kebab-case sans accents (D46)
5. **Output miroir** — la sortie reproduit l'arborescence de l'entree, un sous-dossier par pipeline
6. **Zero DAW lock-in** — fonctionne avec n'importe quel DAW (fichiers audio standards)
7. **Skills WSG centralises** — JAMAIS de code API duplique, tout passe par les skills partages

---

## STRUCTURE PYRAMIDALE WSG — ACCES AUX SKILLS

DAW-Ava ne duplique PAS les clients API. Il consomme les skills centralises de WSG.

### Hierarchie

```
C:\WSurfWSpaceGlobal\                        (WSG — racine)
  Meta/
    Skills-router.md                          Table de routage des skills (source de verite)
  Core/Scripts/Skills/Python/                 SKILLS CENTRALISES
    resolve.py                                Resolveur sys.path (auto-detection WSG)
    fal/                                      Fal.ai — fournisseur IA principal (D75)
      upload.py                               Coeur commun (FAL_KEY registre HKLM, upload, subscribe)
      transcription.py                        Whisper s2t
      tts.py                                  t2a (kokoro, f5-tts, dia-tts, orpheus, elevenlabs)
      music.py                                t2m (beatoven, elevenlabs)
      image.py                                t2i + upscaling
      video.py                                i2v + t2v (kling)
    piapi/                                    PiAPI — Seedance 2.0
      client.py                               Coeur commun
      video.py                                I2V, II2V, T2V, Ref2V
    mediaconvert/                             AWS MediaConvert — extraction frames
  Projects/DAW-Ava/                           CE PROJET
    src/pipelines/stems/separate.py           Consomme fal.upload (upload_file, subscribe)
```

### Import type dans les scripts DAW-Ava

```python
import sys
sys.path.insert(0, "C:/WSurfWSpaceGlobal/Core/Scripts/Skills/Python")
from fal.upload import upload_file, subscribe
from fal.tts import speak
from fal.music import generate_music
```

### Skills utilises par DAW-Ava

| Pipeline | Skill WSG | Fonction | Fournisseur | Endpoint |
|----------|-----------|----------|-------------|----------|
| stems | `replicate` (SDK) | `replicate.run()` | Replicate | `cjwbw/demucs` (htdemucs_ft) |
| de-reverb | `hf.audio` (cloud) | `dereverb()`, `dereverb_chain()` | HuggingFace Space | UVR models (cloud GPU) |
| voice/svc | `replicate` (SDK) | `replicate.run()` | Replicate | `zsxkib/realistic-voice-cloning` |
| master | Dolby.io (client local) | — | Dolby.io | REST |
| sync | `fal.upload` | `subscribe()` | Fal.ai | `fal-ai/mmaudio-v2` |
| voice/tts | `fal.tts` | `speak()` | Fal.ai | kokoro, f5-tts, elevenlabs |
| sfx | `fal.upload` | `subscribe()` | Fal.ai | `fal-ai/elevenlabs/sound-effects/v2` |
| music | `fal.music` | `generate_music()` | Fal.ai | minimax-music, beatoven |

---

## COUCHE FINOPS — ROUTAGE PAR COUT MINIMAL (NON NEGOCIABLE)

### Principe

DAW-Ava utilise PLUSIEURS fournisseurs cloud IA en parallele.
Ava ne choisit JAMAIS un fournisseur par habitude ou par defaut.
Ava applique l'algorithme FinOps a CHAQUE appel API.

### Algorithme de decision

```
POUR CHAQUE appel API audio dans DAW-Ava :

  ETAPE 1 — DISPONIBILITE
    Lister les fournisseurs qui proposent le modele/capacite demandee.
    Si un seul fournisseur l'a → utiliser ce fournisseur. Fin.

  ETAPE 2 — COMPARAISON PRIX
    Si plusieurs fournisseurs proposent le meme modele (ou equivalent) :
    → Consulter la table de resolution ci-dessous.
    → Prendre le MOINS CHER a qualite egale.
    → En cas d'egalite prix : Fal.ai par defaut (D75, ecosysteme WSG).

  ETAPE 3 — VERIFICATION
    Avant tout nouvel appel non encore documente dans la table :
    → Verifier le prix reel sur les deux plateformes.
    → Mettre a jour specs/FinOps/README.md avec le resultat.
    → Puis appliquer le choix.
```

### Table de resolution — Qui est le moins cher par capacite

| Capacite | Fal.ai | Replicate | Dolby.io | **GAGNANT** | Raison |
|----------|--------|-----------|----------|-------------|--------|
| **STEMS** (Demucs) | ~$0.05/run | $0.023/run | — | **Replicate** | 2x moins cher |
| **De-reverb** (UVR models) | — | — | — | **HuggingFace Space** | Gratuit (cloud GPU via Gradio API) |
| **SVC** (RVC v2) | — | $0.034/run | — | **Replicate** | Exclusif |
| **SVC Training** | — | $0.32/run | — | **Replicate** | Exclusif |
| **MASTER** | — | — | $0.05/min | **Dolby.io** | Exclusif |
| **SYNC** (MMAudio V2) | Pay-per-use | $0.006/run | — | A comparer | Verifier prix Fal.ai |
| **TTS** (Kokoro) | $0.02/1K chars | ~$0.003/run | — | A comparer | Unites differentes |
| **TTS** (ElevenLabs) | Pay-per-use | Official | — | A comparer | Prix identiques? |
| **SFX** (ElevenLabs) | Pay-per-use | — | — | **Fal.ai** | Exclusif |
| **MUSIC** (MiniMax 2.6) | $0.15/gen | Official | — | A comparer | Verifier Replicate |
| **MUSIC** (MusicGen) | — | $0.051/run | — | **Replicate** | Exclusif + fine-tune |
| **MUSIC** (Lyria 2/3) | — | Official | — | **Replicate** | Exclusif |
| **MUSIC** (ACE-Step) | — | $0.020/run | — | **Replicate** | Exclusif |
| **Enhancement** | — | $0.0098/run | — | **Replicate** | Exclusif |
| **Analyse** (BPM, structure) | — | $0.087/run | — | **Replicate** | Exclusif |
| **Transcription** (Whisper) | ~$0.006/min | $0.0013/run | — | A comparer | Unites differentes |

**"A comparer"** = unites de facturation differentes (chars vs run vs min). Necessitent un test reel
pour determiner le gagnant. Quand le test est fait, mettre a jour cette table ET `specs/FinOps/README.md`.

### Fournisseurs et cles API

| Fournisseur | Cle | Scope | Registre |
|-------------|-----|-------|----------|
| Fal.ai | `FAL_KEY` | Registre HKLM (Machine) | `AI/MCP/Remote-APIs-WSG.md` |
| Replicate | `ReplicateAPI_KEY` | Registre User | `specs/FinOps/README.md` |
| HuggingFace | `HuggingFaceAPI_KEY` | Registre User | Modeles UVR (de-reverb, de-echo) |
| RunPod | `RUNPOD_API_KEY` | Registre User | Serverless GPU (Docker custom) |
| Dolby.io | A configurer | — | `models/MASTER/README.md` |
| Google AI Studio | `GemKAPI` | Registre User | — |

### Budget pipeline complet — 1 chanson (estimation)

| Etape | Fournisseur (FinOps) | Cout |
|-------|---------------------|------|
| Stems (Demucs) | Replicate | $0.023 |
| De-reverb (UVR cloud) | HuggingFace Space | $0 |
| SVC Training (1 fois) | Replicate | $0.32 |
| SVC Inference | Replicate | $0.034 |
| Mastering | Dolby.io | ~$0.15 |
| **1ere chanson** | | **~$0.53** |
| **Chaque suivante** | | **~$0.21** |

Grille tarifaire detaillee : `specs/FinOps/README.md`

---

### Retours d'experience API (lecons apprises)

- **Demucs** — OUTIL OFFICIEL STEMS DAW-AVA : `cjwbw/demucs` sur Replicate ($0.023/run).
  Modele : `htdemucs_ft` (fine-tune, meilleure qualite — VALIDE par le Cap'taine).
  Mode 2 stems : `stem=vocals` → retourne `vocals` + `other` (= instrumental). Les autres cles sont `None`.
  Renommer `other` en `instrumental` a la reception.
  Format sortie : WAV (mettre `output_format=wav`).
  L'ancien Demucs Fal.ai (`fal-ai/demucs`) est ABANDONNE — qualite inferieure, 6 stems avec bleed.

- **RVC Training** (`replicate/train-rvc-model`) — PIEGES DOCUMENTES :
  1. **Format dataset ZIP obligatoire** : `dataset/<nom_modele>/split_<i>.wav`. PAS un seul fichier WAV dans le ZIP. Le modele plante silencieusement ("can only concatenate str NoneType") si la structure est mauvaise.
  2. **Segmentation prealable** : decouper l'enregistrement en clips de ~10s via ffmpeg (`-f segment -segment_time 10 -c copy`) avant de zipper.
  3. **Types des parametres** : `epoch` = integer, `batch_size` = string, `sample_rate` = string. Types mixtes — ne pas deviner, consulter le schema OpenAPI.
  4. **Version du modele** : la version `cf360587...` (ancienne) est desactivee ("consistently fails setup"). Utiliser `0397d5e2...` (la plus recente fonctionnelle).
  5. **Upload fichier** : passer le fichier en `open('file', 'rb')` directement, pas une URL Replicate files API (qui n'est pas accessible par le modele).

- **De-reverb** — SKILL WSG CLOUD (`hf.audio`) :
  Fournisseur : HuggingFace Space `Politrees/audio-separator_UVR` (Gradio API, cloud GPU).
  Skill : `Core/Scripts/Skills/Python/hf/audio.py` → `dereverb()`, `dereverb_chain()`
  Cle : `HuggingFaceAPI_KEY` (registre User Windows).
  Modeles disponibles : UVR-De-Echo-Aggressive, Reverb_HQ_By_FoxJoy, BS-Roformer-De-Reverb,
  De-Reverb-Echo-MelBand-Roformer-V2-Sucial (state-of-the-art).
  INDISPENSABLE avant le SVC — le RVC reproduit fidelement la reverb du stem source.
  Fallback local : `audio-separator` (pip, CPU) si le Space est down.
  Pipeline valide : `htdemucs_ft (2 stems) → de-reverb cloud (HF Space) → SVC RVC v2`.

- **RVC Inference** (`zsxkib/realistic-voice-cloning`) — PIEGES DOCUMENTES :
  1. **Version du modele** : change regulierement. TOUJOURS utiliser `model.latest_version.id`, jamais un hash code en dur.
  2. **`pitch_change`** est un STRING/ENUM (ex: `"no-change"`), PAS un integer. Utiliser `pitch_change_all` (number) pour l'ajustement fin en demi-tons.
  3. **`output_format`** : mettre `"wav"` pour la qualite, pas `"mp3"` (defaut).
  4. **Parametres reverb** : presents mais laisser les defauts (dry=0.8, wet=0.2) sauf demande explicite.
  5. **Tous les types verifies** : voir `specs/SVC/replicate/rvc-v2/params_inference.md` pour le schema complet.

- **RunPod Serverless** — LECONS APPRISES (D69 + D31) :
  1. **LIRE LA DOC OFFICIELLE AVANT DE CODER** : https://docs.runpod.io/serverless/workers/create-dockerfile
  2. Base image officielle : `runpod/base:0.6.3-cuda11.8.0` (PAS python:3.11-slim)
  3. CMD obligatoire : `python -u /handler.py` (le `-u` est CRITIQUE pour les logs)
  4. Imports globaux (pas dans le handler) — sinon timeout et worker tue
  5. Template officiel : https://github.com/runpod-workers/worker-template
  6. Throttle = GPU pas dispo. Fix : plusieurs GPU en fallback + maxWorkers >= 3
  7. Logs runtime : onglet Logs dans la console RunPod (pas juste Build logs)
  8. **POST-MORTEM COMPLET** : `Docs/Architecture/WSG/Cloud GPU/RunPod-Bonnes-Pratiques.md`
     Checklist pre-deploiement, anti-patterns, SDK reference, gestion throttle.
     A LIRE OBLIGATOIREMENT avant tout nouveau deploiement RunPod (D80).
  9. Skill WSG : `Core/Scripts/Skills/Python/runpod_skill/client.py` — health, purge, run_sync, reset

---

## SYNERGIES AVEC REMOTION/MIKHAELIZE

| Flux | DAW-Ava | Remotion |
|------|---------|---------|
| Video vers Audio | MMAudio V2 genere l'ambiance | Le clip video est l'input |
| Audio vers Video | Le mix final du Cap'taine | Phase 7 merge (bande son) |
| Stems vers Remix | Demucs separe les stems | Remix sur des scenes specifiques |
| Voice vers Narration | Clone voix + TTS | Voice-over sur le film |
| SFX vers Scenes | Genere les bruitages | Integres au montage final |
| Mastering vers Export | Dolby.io masterise la bande son | Export YouTube/Spotify |

---

## DOCUMENTATION

| Document | Pour qui | Contenu |
|----------|----------|---------|
| **architecture/README.md** | **HUMAINS** | **Architecture du projet — miroir lisible de ce CLAUDE.md** |
| **CLAUDE.md** | **AVA** | **Directives machine — miroir algorithmique de architecture/** |
| models/README.md | Les deux | Arsenal audio IA complet (veille globale) |
| models/[CAPACITE]/[fournisseur]/README.md | Les deux | Doc fonctionnelle par fournisseur |
| specs/README.md | Ava | Table de routage operationnelle |
| specs/[CAPACITE]/[fournisseur]/[modele]/README.md | Ava | Specs API detaillees par modele |
| specs/FinOps/README.md | Les deux | Grille tarifaire, comparatifs cout, routage |
| roadmap/ROADMAP.md | Les deux | Phases de developpement, budget, jalons |
| Meta/glossaire.md (WSG) | Les deux | Acronymes : S2T, T2A, T2M, A2A, etc. |
| Meta/Skills-router.md (WSG) | Ava | Skills partages (fal.tts, fal.music, fal.transcription) |

### Miroir architecture/ <-> CLAUDE.md

Ces deux documents decrivent la MEME architecture.
- `architecture/README.md` = lisible par un humain, avec schemas et prose
- `CLAUDE.md` = lisible par Ava, avec regles algorithmiques et tables de decision

Quand l'un change, l'autre DOIT etre synchronise.
L'architecture est la SOURCE DE VERITE pour les decisions strategiques.
Le CLAUDE.md est la SOURCE DE VERITE pour l'execution operationnelle.

---

## ETAT DU PROJET

**Statut** : Phase 1 en cours — stems + SVC + de-reverb operationnels. RunPod Serverless GPU deploye.
**Fait** : CLAUDE.md, architecture, models/, specs/, FinOps, pipelines stems/voice/dereverb, RunPod Docker.
**Prochaine etape** : Finaliser le pipeline SVS (SoulX-Singer V2 RunPod) + mastering.

### REGLE DE LOOP — MISSION EN COURS (NON NEGOCIABLE)

Quand une etape du pipeline est lancee (build, inference, test), Ava reste en **loop de mission** :
- Poll le statut regulierement (RunPod health, build status, job progress)
- Ne demande PAS "tu veux que je continue ?" — elle continue
- Ne s'arrete PAS entre les etapes — elle enchaine
- Signale les resultats au Cap'taine des qu'ils arrivent
- Seul un **STOP explicite** du Cap'taine interrompt la loop

C'est le meme principe que les Lettres d'Or de V2C : une fois le pipeline lance, Ava execute
la chaine complete sans attendre de feu vert intermediaire.

---

*"Le contexte est l'Ava" — D0*
*Projet DAW-Ava — le son augmente*
