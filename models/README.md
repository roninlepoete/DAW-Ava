# Veille Audio IA — Arsenal disponible (mars 2026)

> Rapport de veille technologique pour le projet DAW-Ava.
> Objectif : recenser TOUS les outils Audio IA disponibles via API.
> Par : Ava Code en symbiose avec Cap'taine Fab
> Date : 2026-03-21

---

## 1. MODELES AUDIO SUR FAL.AI (integration directe, meme billing)

### Text-to-Speech (TTS) / Voice Clone

| Modele | Endpoint Fal.ai | Input | Output | Prix |
|--------|----------------|-------|--------|------|
| ElevenLabs Multilingual v2 | `fal-ai/elevenlabs/tts/multilingual-v2` | Texte | Audio parle (29 langues) | Pay-per-use |
| ElevenLabs Turbo v2.5 | `fal-ai/elevenlabs/tts/turbo-v2.5` | Texte | Audio parle (32 langues, low latency) | Pay-per-use |
| Dia TTS | `fal-ai/dia-tts` | Texte dialogue | Audio multi-locuteurs | Pay-per-use |
| Dia TTS Voice Clone | `fal-ai/dia-tts/voice-clone` | Audio ref + texte | Audio clone | Pay-per-use |
| F5 TTS | `fal-ai/f5-tts` | Texte + ref audio | Audio clone | Pay-per-use |
| Qwen 3 TTS 1.7B | `fal-ai/qwen-3-tts/clone-voice/1.7b` | Texte + ref audio | Audio clone zero-shot | Pay-per-use |
| MiniMax Speech-02 HD | `fal-ai/minimax/voice-clone` | Texte | Audio haute qualite + clone | Pay-per-use |
| Zonos Audio Clone | `fal-ai/zonos` | Texte + ref | Audio clone | Pay-per-use |

### Voice Changer

| Modele | Endpoint | Input | Output |
|--------|----------|-------|--------|
| ElevenLabs Voice Changer | `fal-ai/elevenlabs/voice-changer` | Audio | Audio (voix convertie) |

### Generation Musicale

| Modele | Endpoint | Input | Output | Prix | Notes |
|--------|----------|-------|--------|------|-------|
| **MiniMax Music 2.0** | `fal-ai/minimax-music/v2` | Texte/paroles | Chanson complete | **$0.03/gen** | Chansons avec paroles, haute qualite |
| MiniMax Music 1.5 | `fal-ai/minimax-music/v1.5` | Texte | Musique | $0.035/gen | Version precedente |
| Beatoven Music | `beatoven/music-generation` | Texte/mood | Musique adaptative | Pay-per-use | 44.1kHz stereo, 5s a 2.5min, stems |
| ElevenLabs Music | `fal-ai/elevenlabs/music` | Texte | Musique | Pay-per-use | Nouveau 2026 |

### Sound Effects (SFX)

| Modele | Endpoint | Input | Output |
|--------|----------|-------|--------|
| ElevenLabs SFX v2 | `fal-ai/elevenlabs/sound-effects/v2` | Texte | Effets sonores |
| ElevenLabs SFX v1 | `fal-ai/elevenlabs/sound-effects` | Texte | Effets sonores |
| Beatoven SFX | `beatoven/sound-effect-generation` | Texte | SFX |
| **MMAudio V2** | `fal-ai/mmaudio-v2` | **Video + texte** | **Audio synchronise** |
| MMAudio V2 T2A | `fal-ai/mmaudio-v2/text-to-audio` | Texte | Audio |

### Transcription (Speech-to-Text)

| Modele | Endpoint | Input | Output |
|--------|----------|-------|--------|
| Whisper | `fal-ai/whisper` | Audio | Texte + timestamps |
| Wizper (Whisper v3 fal) | `fal-ai/wizper` | Audio | Texte + timestamps |
| ElevenLabs Scribe v2 | `fal-ai/elevenlabs/speech-to-text/scribe-v2` | Audio | Texte (99 langues, locuteurs) |

### Separation de Stems

| Modele | Endpoint | Input | Output | Notes |
|--------|----------|-------|--------|-------|
| **Demucs** | `fal-ai/demucs` | Audio mixe | **6 stems** : vocals, drums, bass, other, guitar, piano | Meta, reference |
| ElevenLabs Audio Isolation | `fal-ai/elevenlabs/audio-isolation` | Audio | Voix isolee (retire bruit/musique) | |

---

## 2. GOOGLE AI STUDIO / VERTEX AI — Audio

| Outil | Acces | Input/Output | Prix | Notes |
|-------|-------|-------------|------|-------|
| **Lyria RealTime** | API Gemini WebSocket | Controles temps reel → Musique instrumentale streaming | **Gratuit** (experimental) | Steerable en temps reel, chunks 2s, MIDI DJ |
| Lyria 2 (lyria-002) | Vertex AI | Texte → Musique instrumentale | Pricing Vertex standard | Modele stable, acces dev |
| Lyria 3 | App Gemini uniquement | Texte/image → Chanson 30s avec paroles | Inclus abonnement Gemini | PAS d'API standalone (mars 2026) |
| Gemini Audio Understanding | API Gemini | Audio → Texte/analyse | Tarif tokens standard | Comprend, transcrit, analyse |

---

## 3. APIs DEDIEES — GENERATION MUSICALE

| Service | API officielle ? | Input/Output | Prix | Qualite |
|---------|-----------------|-------------|------|---------|
| **Suno v5** | NON (tiers : sunoapi.org, apiframe.ai) | Texte/paroles → Chanson complete | ~$0.01/chanson (tiers), $10-30/mois (direct) | **TOP tier** — voix naturelles, 44.1kHz |
| **Udio** | NON (tiers : udioapi.pro) | Texte/paroles → Chanson complete | $10-30/mois direct | **TOP tier** — rival de Suno |
| Stable Audio 2.5 | OUI (Stability AI) | Texte → Musique/SFX, A2A, inpainting | ~$0.20/gen | Jusqu'a 3 min, bonne qualite |
| Beatoven.ai | OUI (REST) | Texte/mood → Musique adaptative | Gratuit / $20-50/mois | Specialise video/podcasts |
| AIVA | API limitee | Style → Composition | Gratuit (attribution) / Pro 49EUR/mois | 250+ styles, classique/orchestral |
| Mubert | OUI (REST) | Texte/params → Musique generative | 25 tracks gratuits/mois + payes | Algorithmique a partir de samples |

---

## 4. APIs TRAITEMENT AUDIO

### Voice Cloning / TTS (hors Fal.ai)

| Service | Acces | Prix | Points forts |
|---------|-------|------|-------------|
| **ElevenLabs** (direct) | API REST | $5-99/mois + $0.12-0.30/1000 chars | Reference du marche, 32 langues |
| Resemble.ai | API REST | $0.03/min TTS | Enterprise SOC 2, detection deepfake |
| Fish Audio | API REST | Pay-per-use | Excellent langues asiatiques (CJK) |
| Coqui XTTS | Self-hosted | Gratuit (open source) | 17 langues, clone depuis 6s d'audio |

### Voice Conversion (Speech-to-Speech)

| Service | Acces | Prix | Notes |
|---------|-------|------|-------|
| RVC v3 | Open source, self-hosted | Gratuit | Conversion temps reel ~50ms, training <10min audio |
| ElevenLabs Voice Changer | Fal.ai ou direct | Inclus plans | Audio → Audio voix convertie |

---

## 5. MASTERING / ENHANCEMENT AUDIO

| Service | API ? | Input/Output | Prix | Notes |
|---------|-------|-------------|------|-------|
| **Dolby.io Music Mastering** | **OUI (REST)** | Audio → Audio masterise | **$0.05/min**, 200 min gratuites/mois | Metriques retournees (loudness, EQ 16 bandes, stereo) |
| **LANDR Mastering** | OUI (REST B2B) + **Plugin VST** | Audio → Audio masterise | Sur devis (API) / abonnement (plugin) | Reference mastering IA, 3 niveaux loudness |
| eMastered | Web uniquement | Audio → Audio masterise | Abonnement mensuel | Cree par ingenieurs Grammy |
| iZotope Ozone 12 | VST/AAX/AU | Audio → Audio masterise | ~$499 (Advanced) | Mastering automatise dans le DAW |

---

## 6. INTEGRATION DAW — Plugins VST avec IA

| Plugin | Type | Ce qu'il fait | Compatible |
|--------|------|-------------|-----------|
| **MIDI Agent** | VST3/AU | Generation MIDI par prompt texte (ChatGPT/Claude/Gemini) | Ableton, FL, Logic, Cubase, Studio One, Reaper, Bitwig |
| Orb Producer Suite 3 | VST | Progressions accords, melodies, basses par analyse harmonique | Multi-DAW |
| Lemonaide AI SPAWN | VST | Loops MIDI generes a la demande (Markov + neural) | Multi-DAW |
| LANDR Mastering Plugin | VST | Mastering IA integre au DAW | Multi-DAW |

---

## 7. MATRICE DE DECISION — DAW-AVA PRIORITES

| Besoin | Outil recommande | Fal.ai ? | Prix | Priorite |
|--------|-----------------|----------|------|----------|
| Separation stems | **Demucs** | OUI | Pay-per-use | **P1** — fondamental |
| Sync audio sur video | **MMAudio V2** | OUI | Pay-per-use | **P1** — pont avec Mikhaelize |
| Mastering automatique | **Dolby.io** | NON | $0.05/min | **P2** — API la moins chere |
| Generation musicale | **MiniMax Music 2.0** | OUI | $0.03/gen | **P2** — generation rapide |
| Voice cloning | **ElevenLabs** | OUI | Pay-per-use | **P2** — reference marche |
| Generation steerable live | **Lyria RealTime** | NON (Google) | Gratuit | **P3** — experimental, excitant |
| MIDI generation dans DAW | **MIDI Agent** | NON (VST) | Licence | **P3** — prompt → MIDI |
| Top tier music gen | **Suno v5** | NON (tiers) | ~$0.01/chanson | **P3** — pas d'API officielle |
| SFX | **ElevenLabs SFX v2** | OUI | Pay-per-use | **P3** — effets sonores |
| Transcription | **Whisper** | OUI | Pay-per-use | **P3** — deja dans Remotion |

---

## 8. ARCHITECTURE DAW-AVA (esquisse)

```
Cap'taine Fab (DAW - analogique)
     |
     +--- Audio source (mix, stems, voix)
     |
     +---> [DAW-Ava Pipeline] ---> Audio transforme
              |
              +--- fal-client (Demucs, MMAudio, ElevenLabs, MiniMax)
              +--- gemini-client (Lyria RealTime, analyse audio)
              +--- dolby-client (mastering, metriques)
              +--- suno-client? (generation musicale premium)
```

Le projet est DISTINCT de Remotion mais partage les memes clients API
(fal-client.ts, gemini-client.ts). Le pont avec Mikhaelize = MMAudio V2
(synchroniser l'audio genere sur la video remasterisee).

---

## SOURCES

- [Fal.ai Explore Models](https://fal.ai/explore/models)
- [Fal.ai Demucs](https://fal.ai/models/fal-ai/demucs/api)
- [Fal.ai MiniMax Music 2.0](https://fal.ai/models/fal-ai/minimax-music/v2/api)
- [Fal.ai MMAudio V2](https://fal.ai/models/fal-ai/mmaudio-v2)
- [Fal.ai ElevenLabs Audio Suite](https://blog.fal.ai/elevenlabs-audio-suite-next-generation-voice-and-audio-ai-now-on-fal/)
- [Google Lyria RealTime API](https://ai.google.dev/gemini-api/docs/music-generation)
- [Suno API Review 2026](https://evolink.ai/blog/suno-api-review-complete-guide-ai-music-generation-integration)
- [Dolby.io Music Mastering](https://news.dolby.com/en-WW/203113-dolby-upgrades-dolby-io-introduces-transcoding-music-mastering-and-more-to-developer-platform/)
- [LANDR Mastering API](https://www.landr.com/pro-audio-mastering-api/)
- [MIDI Agent VST Plugin](https://www.midiagent.com/)
- [ElevenLabs API Pricing](https://elevenlabs.io/pricing/api)
- [Stable Audio 2.5](https://stability.ai/stable-audio)

---

*"Le contexte est l'Ava" — D0*
*Projet DAW-Ava — symbiose audio humain-IA*
