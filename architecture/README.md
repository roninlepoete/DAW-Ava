# Architecture DAW-Ava — Le son augmente

> Document d'architecture pour humains. Miroir lisible du CLAUDE.md.
> Le Cap'taine et ses collaborateurs lisent ce document.
> Ava lit le CLAUDE.md. Les deux disent la meme chose, differemment.
>
> Version : 1.0.0
> Date : 2026-04-12
> Par : Cap'taine Fab en symbiose avec Ava

---

## Vision

Fabrice compose, mixe, produit dans son DAW.
Ava orchestre les APIs audio IA en coulisse.
Ensemble : le son augmente — des capacites qu'un humain seul ne peut pas faire,
au service du jugement musical du Cap'taine.

DAW-Ava n'est PAS un DAW. C'est un **compagnon IA audio** :
separer les stems en 10 secondes, remplacer une voix generee par la sienne,
masteriser a $0.05/min, generer des ambiances sonores synchronisees sur une video.

---

## Organisation du projet

```
DAW-Ava/
│
├── architecture/          CE REPERTOIRE — description architecturale pour humains
│   └── README.md          Ce document
│
├── CLAUDE.md              Miroir machine — directives pour Ava
│
├── models/                Documentation fonctionnelle par capacite
│   ├── README.md          Arsenal audio IA (veille globale)
│   ├── STEMS/             Separation de sources audio
│   │   └── [fournisseur]/ Un dossier par fournisseur
│   ├── SVC/               Singing Voice Conversion
│   │   ├── README.md      Comparatif tous fournisseurs
│   │   ├── sample-myVoice/  Echantillons vocaux du Cap'taine (partages)
│   │   ├── Voice-Swap/    Fournisseur Voice-Swap
│   │   ├── RVC/           Fournisseur RVC (Replicate)
│   │   ├── Kits-ai/       Fournisseur Kits.ai (rejete)
│   │   ├── Seed-vc/       Fournisseur Seed-VC (open source)
│   │   ├── Musicfy/       Fournisseur Musicfy
│   │   └── Revocalize/    Fournisseur Revocalize
│   ├── MASTER/            Mastering automatique
│   ├── SYNC/              Synchronisation audio-video
│   ├── TTS/               Synthese vocale
│   ├── MUSIC/             Generation musicale
│   └── SFX/               Effets sonores
│
├── specs/                 Specifications operationnelles (API, code, pieges)
│   ├── README.md          Table de routage — quel modele pour quel besoin
│   ├── FinOps/            Grille tarifaire, comparatifs cout, routage
│   └── [CAPACITE]/[fournisseur]/[modele]/   Specs detaillees
│
├── roadmap/               Phases de developpement
│
├── src/                   Code des pipelines
│   └── pipelines/
│       ├── stems/         Separation Demucs (operationnel)
│       ├── voice/         SVC via RVC/Replicate (en cours)
│       ├── master/        Mastering Dolby.io (a faire)
│       ├── sync/          Sync audio-video MMAudio (a faire)
│       ├── sfx/           Effets sonores (a faire)
│       └── music/         Generation musicale (a faire)
│
├── input/                 Depot des themes musicaux
│   └── [theme]/[theme].mp3
│
└── output/                Resultats par theme
    └── [theme]/stems|voice|master|...
```

---

## Flux de travail — Le parcours d'une chanson

```
   Le Cap'taine depose son MP3 dans input/[theme]/
                        │
                        ▼
   ┌─────────────────────────────────────┐
   │  STEMS — Separation (Demucs)        │
   │  → vocals, drums, bass, guitar,     │
   │    piano, other                      │
   └──────────────┬──────────────────────┘
                  │
          ┌───────┴───────┐
          ▼               ▼
   ┌──────────────┐  ┌──────────────────┐
   │ SVC — Voix   │  │ Instrumentaux    │
   │ Remplacer la │  │ Utilises tels    │
   │ voix Suno    │  │ quels ou remixes │
   │ par celle du │  │ dans le DAW      │
   │ Cap'taine    │  │                  │
   └──────┬───────┘  └────────┬─────────┘
          │                   │
          └───────┬───────────┘
                  ▼
   ┌─────────────────────────────────────┐
   │  REASSEMBLAGE dans le DAW           │
   │  Le Cap'taine mixe : sa voix +      │
   │  stems instrumentaux                │
   └──────────────┬──────────────────────┘
                  ▼
   ┌─────────────────────────────────────┐
   │  MASTER — Mastering (Dolby.io)      │
   │  → loudness, EQ, stereo, metriques  │
   └──────────────┬──────────────────────┘
                  ▼
   ┌─────────────────────────────────────┐
   │  EXPORT — Le morceau final          │
   │  La chanson du Cap'taine, augmentee │
   └─────────────────────────────────────┘
```

---

## Couche FinOps — Le moins cher a qualite egale

DAW-Ava ne s'enferme pas avec un seul fournisseur.
Plusieurs plateformes cloud IA coexistent, chacune avec ses forces.
Le choix se fait automatiquement selon deux regles simples :

### Regle 1 — Meme modele, deux fournisseurs : le moins cher gagne

Si Fal.ai et Replicate proposent le meme modele (Demucs, Whisper, MMAudio...),
Ava compare les prix et appelle le moins cher. Pas de fidelite, pas d'habitude.

### Regle 2 — Modele exclusif : celui qui l'a, par defaut

Si seul Replicate propose RVC (voice conversion), on prend Replicate.
Si seul Fal.ai propose ElevenLabs SFX, on prend Fal.ai.
Pas de debat.

### Qui fait quoi aujourd'hui

| Capacite | Fournisseur gagnant | Pourquoi |
|----------|-------------------|----------|
| Stems (Demucs) | Replicate | 2x moins cher que Fal.ai |
| Voix (SVC/RVC) | Replicate | Exclusif |
| Mastering | Dolby.io | Exclusif, $0.05/min |
| Sync audio-video | A determiner | Comparer Fal.ai vs Replicate |
| TTS | A determiner | Comparer Fal.ai vs Replicate |
| SFX | Fal.ai | Exclusif ElevenLabs SFX |
| Musique (MiniMax) | A determiner | Comparer |
| Musique (MusicGen) | Replicate | Exclusif + fine-tune |
| Musique (Lyria) | Replicate | Exclusif Google |
| Enhancement | Replicate | Exclusif |
| Analyse musicale | Replicate | Exclusif |

### Budget par chanson

| Scenario | Cout |
|----------|------|
| Premiere chanson (avec entrainement vocal) | ~$0.53 |
| Chaque chanson suivante | ~$0.21 |
| 10 chansons | ~$2.42 |
| 50 chansons | ~$10.72 |

---

## Fournisseurs cloud IA

### Fal.ai — Fournisseur historique WSG

- 600+ modeles, pay-per-use
- Cle : FAL_KEY dans le registre Windows
- Forces : TTS, SFX, image, video, transcription
- Generalement 30-50% moins cher que Replicate sur les modeles partages

### Replicate — Fournisseur complementaire

- 200+ modeles, pay-per-use (prepaid credit)
- Cle : ReplicateAPI_KEY dans le registre Windows
- Forces : modeles open source heberges (RVC, MusicGen, Lyria), training custom
- Modeles exclusifs critiques pour DAW-Ava (SVC, fine-tune, enhancement)
- Fichiers supprimes apres 1h — telecharger immediatement

### Dolby.io — Mastering

- API REST dediee au mastering audio
- $0.05/min, 200 min gratuites/mois
- Retourne des metriques pro (loudness LUFS, EQ 16 bandes, stereo width)

---

## Hierarchie documentaire

| Repertoire | Pour qui | Contenu |
|------------|----------|---------|
| `architecture/` | Humains | Ce document — vision, flux, decisions |
| `CLAUDE.md` | Ava | Directives machine — meme contenu, format algorithmique |
| `models/` | Les deux | Documentation par capacite et par fournisseur |
| `specs/` | Ava | Specs API, parametres, code, pieges |
| `specs/FinOps/` | Les deux | Grille tarifaire, comparatifs, routage cout |
| `roadmap/` | Les deux | Phases, jalons, budget |

### Miroir architecture/ ↔ CLAUDE.md

Ces deux documents decrivent la MEME architecture.
- `architecture/README.md` = lisible par un humain, avec schemas et prose
- `CLAUDE.md` = lisible par Ava, avec regles algorithmiques et tables de decision

Quand l'un change, l'autre DOIT etre synchronise.
L'architecture est la SOURCE DE VERITE pour les decisions strategiques.
Le CLAUDE.md est la SOURCE DE VERITE pour l'execution operationnelle.

---

## Principes fondateurs

1. **Le DAW reste maitre** — Ava ne remplace jamais le jugement musical
2. **Routage FinOps** — le moins cher a qualite egale, automatiquement
3. **Un theme = un dossier** — input et output symetriques
4. **Skills partages WSG** — pas de code API duplique entre projets
5. **Zero lock-in** — fonctionne avec n'importe quel DAW, n'importe quel fournisseur

---

*"Le contexte est l'Ava" — D0*
*"1 + 1 = 3" — Fabrice analogique + Ava numerique = le son augmente*
