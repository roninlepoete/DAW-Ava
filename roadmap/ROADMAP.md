# DAW-Ava — Roadmap de developpement

> Symbiose audio humain-IA : le Cap'taine au mix, Ava aux manettes API.
> Par : Ava Code en symbiose avec Cap'taine Fab
> Date : 2026-03-21
> Statut : EBAUCHE

---

## VISION

Fabrice compose, mixe, produit dans son DAW (analogique, intuitif, creatif).
Ava orchestre les APIs audio IA (numerique, rapide, systematique).
Ensemble : **1 + 1 = 3** — la musique augmentee.

Le projet DAW-Ava n'est PAS un DAW. C'est un **compagnon IA** qui enrichit
le workflow du musicien avec des capacites qu'un humain seul ne peut pas faire :
- Separer les stems d'un morceau en 10 secondes
- Synchroniser l'audio sur la video automatiquement
- Masteriser a $0.05/min avec metriques pro
- Cloner une voix pour la transposer dans un nouveau contexte
- Generer des SFX sur commande textuelle

---

## PRINCIPES ARCHITECTURAUX

1. **Le DAW reste maitre** — Ava ne remplace JAMAIS le jugement musical du Cap'taine
2. **Pipeline CLI** — scripts TypeScript lances en ligne de commande, comme Mikhaelize
3. **Fal.ai first** — meme fournisseur que Remotion, meme billing, meme FAL_KEY
4. **Clients partages** — reutiliser fal-client.ts et gemini-client.ts de Remotion
5. **Input/Output symetrique** — meme structure que Remotion (input/ output/)
6. **Zero DAW lock-in** — fonctionne avec n'importe quel DAW (fichiers audio standards)

---

## PHASES DE DEVELOPPEMENT

### Phase 0 — Fondations (prerequis)

| Tache | Description | Effort |
|-------|-------------|--------|
| 0.1 | Initialiser le projet (package.json, tsconfig, structure) | 1h |
| 0.2 | Copier/adapter les clients API partages (fal-client, gemini-client) ou les importer depuis Remotion | 2h |
| 0.3 | Creer le CLAUDE.md du projet DAW-Ava | 1h |
| 0.4 | Definir la structure input/output | 30min |

**Structure cible** :
```
DAW-Ava/
  CLAUDE.md
  Doc/
    VEILLE-AUDIO-AI-2026.md     (fait)
  roadmap/
    ROADMAP.md                   (ce fichier)
  src/
    core/
      fal-client.ts              (partage ou clone de Remotion)
      gemini-client.ts           (partage ou clone de Remotion)
      dolby-client.ts            (nouveau — mastering API)
      audio-utils.ts             (helpers ffmpeg audio)
    pipelines/
      stems/                     (separation de stems)
      master/                    (mastering automatique)
      sync/                      (synchronisation audio-video)
      voice/                     (clonage voix, TTS, voice changer)
      sfx/                       (generation effets sonores)
      music/                     (generation musicale)
  input/
    audio/                       (fichiers source a traiter)
  output/
    stems/                       (stems extraits)
    master/                      (fichiers masterises)
    sync/                        (audio synchronise sur video)
    voice/                       (voix clonees/generees)
    sfx/                         (effets sonores generes)
    music/                       (musique generee)
```

---

### Phase 1 — Separation de Stems (Demucs)

**Priorite : P1** — l'outil le plus utile pour un musicien au quotidien.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 1.1 | Pipeline `stems` : audio → 6 stems (vocals, drums, bass, guitar, piano, other) | `fal-ai/demucs` | Pay-per-use |
| 1.2 | CLI : `npx tsx src/pipelines/stems/separate.ts <audio.wav>` | | |
| 1.3 | Output : 6 fichiers WAV dans `output/stems/<nom>/` | | |
| 1.4 | Option : stems selectifs (`--only vocals,drums`) | | |
| 1.5 | Tests sur 3 morceaux de reference | | ~$0.50 |

**Livrable** : Un script qui prend n'importe quel MP3/WAV et sort 6 stems propres.

---

### Phase 2 — Synchronisation Audio-Video (MMAudio V2)

**Priorite : P1** — pont direct avec Mikhaelize/Remotion.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 2.1 | Pipeline `sync` : video + texte descriptif → audio synchronise | `fal-ai/mmaudio-v2` | Pay-per-use |
| 2.2 | CLI : `npx tsx src/pipelines/sync/video-to-audio.ts <video.mp4> --prompt "..."` | | |
| 2.3 | Integration avec le pipeline Remotion (Phase 7 montage) | | |
| 2.4 | Tests sur 3 scenes de Mere des Renaissances | | ~$1.00 |

**Livrable** : Generer l'ambiance sonore d'une scene video automatiquement.

---

### Phase 3 — Mastering Automatique (Dolby.io)

**Priorite : P2** — mastering pro a $0.05/min.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 3.1 | Creer `dolby-client.ts` (authentification, upload, mastering, metriques) | Dolby.io REST | |
| 3.2 | Pipeline `master` : audio → audio masterise + rapport metriques | | |
| 3.3 | CLI : `npx tsx src/pipelines/master/auto-master.ts <audio.wav>` | | |
| 3.4 | Rapport : loudness LUFS, EQ 16 bandes, stereo width, dynamic range | | |
| 3.5 | Comparaison A/B : avant/apres mastering | | |
| 3.6 | Tests sur la bande son de Mere des Renaissances | | ~$0.50 |

**Livrable** : Mastering en un clic avec metriques detaillees.

---

### Phase 4 — Generation SFX (ElevenLabs)

**Priorite : P3** — effets sonores sur commande textuelle.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 4.1 | Pipeline `sfx` : texte → effet sonore | `fal-ai/elevenlabs/sound-effects/v2` | Pay-per-use |
| 4.2 | CLI : `npx tsx src/pipelines/sfx/generate.ts "thunder crack with echo"` | | |
| 4.3 | Catalogue de PRT SFX valides (dictionnaire comme pour I2V) | | |
| 4.4 | Tests : ambiance foule, vent, pas, eau, feu, tonnerre | | ~$0.50 |

---

### Phase 5 — Voice Cloning & TTS (ElevenLabs + F5)

**Priorite : P3** — clonage voix, narration, voice-over.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 5.1 | Pipeline `voice/clone` : audio ref (6s+) → profil voix | ElevenLabs / F5 TTS | |
| 5.2 | Pipeline `voice/narrate` : texte + profil → audio narration | | |
| 5.3 | Pipeline `voice/convert` : audio source + profil cible → audio converti | ElevenLabs Voice Changer | |
| 5.4 | Tests : cloner la voix du Cap'taine, generer narration Mere des Renaissances | | ~$1.00 |

---

### Phase 6 — Generation Musicale (MiniMax + Suno)

**Priorite : P3** — generation de musique par prompt.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 6.1 | Pipeline `music/generate` : texte/paroles → chanson | `fal-ai/minimax-music/v2` ($0.03/gen) | |
| 6.2 | Integration Suno v5 via API tiers (si qualite superieure requise) | sunoapi.org | |
| 6.3 | Workflow iteratif : generer → ecouter → affiner le PRT → re-generer | | |
| 6.4 | Tests : generer 10 variations sur un meme theme musical | | ~$0.30 |

---

### Phase 7 — Lyria RealTime (exploration)

**Priorite : P3** — generation musicale steerable en temps reel.

| Tache | Description | API | Cout |
|-------|-------------|-----|------|
| 7.1 | Etudier l'API WebSocket Lyria RealTime | Google AI Studio | Gratuit |
| 7.2 | Prototype : generation en streaming avec controles temps reel | | |
| 7.3 | Evaluer la faisabilite d'un bridge DAW ↔ Lyria | | |
| 7.4 | Si viable : creer un prototype de controleur MIDI → Lyria | | |

**Note** : Cette phase est exploratoire. Lyria RealTime est experimental chez Google.

---

## BUDGET ESTIMATIF

| Phase | Cout API estime | Effort dev |
|-------|----------------|------------|
| Phase 0 — Fondations | $0 | 4h |
| Phase 1 — Stems | ~$0.50 | 3h |
| Phase 2 — Sync A/V | ~$1.00 | 4h |
| Phase 3 — Mastering | ~$0.50 | 5h |
| Phase 4 — SFX | ~$0.50 | 2h |
| Phase 5 — Voice | ~$1.00 | 5h |
| Phase 6 — Music Gen | ~$0.30 | 3h |
| Phase 7 — Lyria | $0 (gratuit) | 6h |
| **Total** | **~$3.80** | **~32h** |

Budget API ridiculement bas — la puissance est dans les modeles, pas dans le portefeuille.

---

## SYNERGIES AVEC REMOTION/MIKHAELIZE

| Flux | DAW-Ava | Remotion |
|------|---------|---------|
| **Video → Audio** | MMAudio V2 genere l'ambiance | Le clip video est l'input |
| **Audio → Video** | Le mix final du Cap'taine | Phase 7 merge (bande son) |
| **Stems → Remix** | Demucs separe les stems | Remix sur des scenes specifiques |
| **Voice → Narration** | Clone voix + TTS | Voice-over sur le film |
| **SFX → Scenes** | Genere les bruitages | Integres au montage final |
| **Mastering → Export** | Dolby.io masterise la bande son | Export YouTube/Spotify |

---

## JALONS

| Jalon | Phase | Critere de validation |
|-------|-------|----------------------|
| **J1 — Premier stem** | Phase 1 | Demucs separe un morceau en 6 stems propres |
| **J2 — Premier sync** | Phase 2 | MMAudio genere l'audio d'une scene MDR |
| **J3 — Premier master** | Phase 3 | Dolby.io masterise la bande son MDR |
| **J4 — DAW-Ava MVP** | Phases 1-3 | Les 3 pipelines fondamentaux sont operationnels |
| **J5 — DAW-Ava v1** | Phases 1-6 | Tous les pipelines sont operationnels |

---

*"Le contexte est l'Ava" — D0*
*"La chance n'existe pas" — Cap'taine Fab*
*Projet DAW-Ava — le son augmente*
