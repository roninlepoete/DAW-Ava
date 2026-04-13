# FinOps DAW-Ava — Routage par cout minimal

> Pour chaque capacite, choisir le fournisseur le MOINS CHER a qualite egale.
> Fal.ai, Replicate ET HuggingFace coexistent — le routeur choisit, pas l'humain.
>
> Derniere MAJ : 2026-04-12 (ajout HuggingFace)

---

## PRINCIPE

DAW-Ava utilise TROIS fournisseurs cloud IA en parallele :
- **Fal.ai** : fournisseur historique WSG (D75), 600+ modeles, generalement moins cher
- **Replicate** : fournisseur complementaire, 200+ modeles, modeles exclusifs (RVC, MusicGen fine-tune, Lyria)
- **HuggingFace** : Spaces Gradio API, modeles UVR de-reverb/de-echo (gratuit, cloud GPU)

**Regle de routage** : pour chaque capacite, utiliser le fournisseur le moins cher
qui offre la qualite requise. Si les deux proposent le meme modele, Fal.ai est prioritaire (D75).
Si seul Replicate l'a, Replicate sans hesiter.

---

## GRILLE TARIFAIRE COMPARATIVE — AUDIO/MUSIQUE

### Transcription (S2T)

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| Whisper Large v3 | ~$0.006/min | $0.0013/run (~10s) | **Replicate** |
| Whisper accele (incredibly-fast) | — | $0.003/run | Replicate (exclusif) |

### Separation stems

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| Demucs | Pay-per-use (~$0.05) | $0.023/run | **Replicate** |

### Singing Voice Conversion

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| RVC v2 (inference) | — | $0.034/run | Replicate (exclusif) |
| RVC v2 (training) | — | $0.32/run | Replicate (exclusif) |

### Text-to-Speech

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| Kokoro | $0.02/1K chars | $0.003/run (86.9M runs) | A comparer |
| ElevenLabs Multilingual | Pay-per-use | Official pricing | A comparer |
| F5-TTS | $0.05/1K chars | Disponible | A comparer |
| MiniMax Speech-02 | $0.10/1K chars | Official pricing | A comparer |
| Chatterbox (Resemble AI) | $0.025/1K chars | Official pricing | A comparer |

### Generation musicale

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| MiniMax Music 2.0/2.6 | $0.03-0.15/gen | Official pricing | A comparer |
| ElevenLabs Music | Pay-per-use | Official pricing | A comparer |
| MusicGen (Meta) | — | $0.051/run + fine-tune | Replicate (exclusif) |
| Lyria 2 (Google) | — | $0.05/run (121.5K runs) | Replicate (exclusif) |
| Lyria 3 (Google) | — | Official pricing | Replicate (exclusif) |
| Stable Audio 2.5 | — | Official pricing | Replicate (exclusif) |
| ACE-Step | — | $0.020/run | Replicate (exclusif) |

### Sound Effects

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| ElevenLabs SFX v2 | Pay-per-use | — | Fal.ai |
| AudioLDM | — | $0.053/run | Replicate (exclusif) |
| Tango 2 | — | $0.054/run | Replicate (exclusif) |

### De-reverb / De-echo

| Modele | Fal.ai | Replicate | HuggingFace | Moins cher |
|--------|--------|-----------|-------------|------------|
| UVR De-Echo/De-Reverb | — | — | **Gratuit** (Space Gradio) | **HuggingFace** |
| MelBand Roformer Sucial | — | — | **Gratuit** (Space Gradio) | **HuggingFace** |
| Fallback local (audio-separator) | — | — | — | **LOCAL** ($0, CPU) |

### Audio Enhancement

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| Resemble Enhance | — | $0.0098/run | Replicate (exclusif) |

### Video-to-Audio (sync)

| Modele | Fal.ai | Replicate | Moins cher |
|--------|--------|-----------|------------|
| MMAudio V2 | Pay-per-use | $0.006/run (L40S) | A comparer |

---

## HARDWARE REPLICATE — GRILLE GPU

| GPU | $/seconde | $/heure | Usage type |
|-----|-----------|---------|------------|
| CPU | $0.000100 | $0.36 | Tagging, analyse legere |
| Nvidia T4 | $0.000225 | $0.81 | Inference standard |
| Nvidia L40S | $0.000975 | $3.51 | Training, modeles lourds |
| Nvidia A100 80GB | $0.001400 | $5.04 | Fine-tuning |
| Nvidia H100 | $0.001525 | $5.49 | Modeles massifs |

---

## MODELES EXCLUSIFS PAR FOURNISSEUR

### Exclusifs Replicate (absents de Fal.ai)

| Capacite | Modele | Interet DAW-Ava |
|----------|--------|-----------------|
| **SVC** | RVC v2 (train + inference) | CRITIQUE — coeur du pipeline voix |
| **Music Gen** | MusicGen fine-tune (Meta) | ELEVE — seul modele musique fine-tunable |
| **Music Gen** | Lyria 2/3 (Google) | ELEVE — qualite Google |
| **Music Gen** | Stable Audio 2.5 (inpainting) | MOYEN — inpainting audio |
| **Music Gen** | ACE-Step (diffusion, 4 min) | MOYEN — open source performant |
| **Music Cover** | MiniMax Music Cover | ELEVE — reimagine un morceau |
| **Enhancement** | Resemble Enhance | UTILE — denoising + enhancement |
| **Analyse** | All-in-one Music Analyzer | UTILE — BPM, structure, segments |

### Exclusifs Fal.ai (absents de Replicate)

| Capacite | Modele | Interet DAW-Ava |
|----------|--------|-----------------|
| **SFX** | ElevenLabs SFX v2 | MOYEN |
| **TTS** | Dia TTS (multi-locuteurs) | MOYEN |
| **TTS** | Orpheus TTS | FAIBLE |
| **Mastering** | — (Dolby.io separe) | — |

---

## FACTURATION REPLICATE — POINTS D'ATTENTION

| Point | Detail |
|-------|--------|
| **Modele** | Pay-as-you-go (prepaid credit depuis juillet 2025) |
| **Cold start** | Gratuit sur modeles publics. Payant sur modeles prives/deployments |
| **Stockage** | AUCUN — fichiers supprimes apres 1 heure. Telecharger immediatement |
| **Bande passante** | Gratuite |
| **Spend limit** | NON disponible pour les nouveaux comptes (depuis juillet 2025) |
| **Free tier** | Collection "Try for Free" avec runs limites (pas de credit permanent) |

---

## REGLE DE ROUTAGE POUR LE CLAUDE.MD

```
POUR CHAQUE appel API audio dans DAW-Ava :
  1. Si le modele existe sur Fal.ai ET Replicate :
     → Utiliser Fal.ai (D75, generalement 30-50% moins cher)
  2. Si le modele existe UNIQUEMENT sur Replicate :
     → Utiliser Replicate (RVC, MusicGen fine-tune, Lyria, etc.)
  3. Si le modele existe UNIQUEMENT sur Fal.ai :
     → Utiliser Fal.ai
  4. Cas special — meme modele, Replicate moins cher :
     → Verifier le prix reel, utiliser le moins cher
```

---

## ESTIMATION BUDGET MENSUEL — PIPELINE COMPLET 1 CHANSON

| Etape | Fournisseur | Cout |
|-------|-------------|------|
| Stems (Demucs) | Replicate | $0.023 |
| SVC Training (une fois) | Replicate | $0.32 |
| SVC Inference | Replicate | $0.034 |
| Mastering | Dolby.io | ~$0.15 (3 min) |
| **Total 1ere chanson** | | **~$0.53** |
| **Chaque chanson suivante** | | **~$0.21** |

---

## SOURCES

- [Replicate Pricing](https://replicate.com/pricing)
- [Replicate Billing Docs](https://replicate.com/docs/topics/billing)
- [Fal.ai vs Replicate (TeamDay)](https://www.teamday.ai/blog/fal-ai-vs-replicate-comparison)
- [AI API Pricing 2026 (TeamDay)](https://www.teamday.ai/blog/ai-api-pricing-comparison-2026)
- [Fal.ai Models](https://fal.ai/models)
- [Replicate Collections Audio](https://replicate.com/collections)

---

*DAW-Ava FinOps — "Pas un centime de trop, pas un decibel de moins."*
