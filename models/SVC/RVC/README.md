# RVC v2/v3 — Retrieval-based Voice Conversion (open source, communautaire)

> Reference communautaire pour le SVC musical. Entrainement obligatoire mais resultats excellents.
> Disponible en API REST cloud (Replicate, Eachlabs) = vrai pay-as-you-go.
> Date de veille : 2026-04-12
> Source : https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI

---

## CE QUE C'EST

Modele open source de voice conversion base sur la recuperation de features vocales.
Le plus utilise par la communaute musicale pour les covers IA et la conversion vocale.
Necessite un entrainement de modele vocal (pas de zero-shot).

---

## FICHE TECHNIQUE

| Critere | Detail |
|---------|--------|
| **GitHub** | https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI |
| **Statut** | ACTIF — 882 commits, v3 pretrained models publies |
| **Licence** | Open source |
| **Zero-shot** | NON — entrainement obligatoire |
| **Extraction pitch** | RMVPE (superieur a CREPE) |
| **Sample rate** | 40 kHz defaut, supporte **48 kHz** (choisir 48k) |
| **GPU (self-hosted)** | 8 Go VRAM minimum (RTX 20 series+) |
| **Communaute** | La plus large pour le SVC musical |

---

## API REST CLOUD — PAY-AS-YOU-GO (zero abonnement)

### Replicate — Cle en main

| Critere | Detail |
|---------|--------|
| **URL** | https://replicate.com/zsxkib/realistic-voice-cloning |
| **API** | REST standard Replicate (POST /v1/predictions) |
| **Version** | RVC v2 |
| **Inference** | ~$0.034/run (Nvidia T4). Une chanson 3 min = ~$0.034 |
| **Training** | ~$0.32/run (L40S GPU, ~6 min) via https://replicate.com/replicate/train-rvc-model |
| **Modele custom** | OUI — parametre "CUSTOM" + URL vers .pth/.zip heberge (HuggingFace, etc.) |
| **Latence** | ~3 min par prediction (variable selon longueur). Cold start possible |
| **Cle en main** | OUI — aucun deploiement, aucun serveur a maintenir |

**Cout typique d'un cycle complet** :
- Training du modele vocal : **$0.32** (une seule fois)
- Conversion d'un morceau 3 min : **$0.034**
- 10 conversions = $0.34
- **Total premiere chanson : ~$0.35. Chaque suivante : ~$0.03.**

### Eachlabs — Le moins cher

| Critere | Detail |
|---------|--------|
| **URL** | https://www.eachlabs.ai/rvc-project/rvc/rvc-v2 |
| **API** | REST (POST create prediction + poll result) |
| **Version** | RVC v2 |
| **Inference** | $0.0002475/sec GPU. Chanson 3 min (~120s traitement) = **~$0.03** |
| **Training** | OUI — https://www.eachlabs.ai/eachlabs/eachlabs/train-rvc |
| **Modele custom** | OUI — URL HuggingFace acceptee |
| **Statut** | Actif (copyright 2026, modele publie dec 2025) |
| **Cle en main** | OUI |

### RunPod — Le plus economique (DIY)

| Critere | Detail |
|---------|--------|
| **URL** | https://www.runpod.io/product/serverless |
| **API** | REST (serverless endpoint, deploiement Docker) |
| **Inference** | A4000 : $0.00016/s. Chanson 3 min = **~$0.019** |
| **Training** | DIY (a integrer dans le container) |
| **Modele custom** | OUI — full controle |
| **Cle en main** | NON — necessite build/deploy d'une image Docker |
| **Templates** | github.com/mahdjalili/rvcv2-runpod |
| **Cold start** | ~500ms (mode flex) |

---

## COMPARATIF API CLOUD

| Critere | Replicate | Eachlabs | RunPod |
|---------|-----------|----------|--------|
| **Cle en main** | OUI | OUI | NON (DIY) |
| **Prix / chanson 3 min** | ~$0.034 | ~$0.03 | ~$0.019 |
| **Training inclus** | OUI ($0.32) | OUI | DIY |
| **Upload modele custom** | OUI (.pth URL) | OUI (HF URL) | OUI (full) |
| **Abonnement** | NON | NON | NON |
| **Effort integration** | Faible (SDK Python) | Faible (REST) | Eleve (Docker) |

**Recommandation** : Replicate pour la simplicite (SDK Python, ecosysteme large).
Eachlabs si chaque centime compte. RunPod si on veut le controle total.

---

## ENTRAINEMENT DU MODELE VOCAL

| Parametre | Requis |
|-----------|--------|
| **Duree audio** | 10 min minimum, 30-60 min recommande |
| **Type** | **CHANT obligatoire** + parole recommandee (les deux pour la variete) |
| **Format** | WAV 16-bit 44.1/48 kHz mono |
| **Contenu** | Voix chantee seule, DRY, a cappella |
| **Qualite** | Micro studio, piece traitee acoustiquement |
| **Variete** | Tessiture complete (graves → aigus), lent + rapide, tenu + staccato |
| **Temps (self-hosted)** | ~3 jours sur RTX 3090 pour 500K steps |
| **Temps (Replicate)** | ~6 min ($0.32) |
| **Temps (Eachlabs)** | Non documente |

**IMPORTANT** : L'echantillon DOIT contenir du chant si le but est la conversion de chant.
Un modele entraine sur de la parole seule produit des resultats degrades sur le chant
(pas de vibrato, pas de notes tenues, pas de dynamiques). Voir `sample-myVoice/README.md`.

---

## DEPLOIEMENT — TOUTES OPTIONS

| Option | Type | Cout | Effort |
|--------|------|------|--------|
| **Replicate** | API cloud cle en main | ~$0.034/run | Faible |
| **Eachlabs** | API cloud cle en main | ~$0.03/run | Faible |
| **RunPod** | Serverless DIY | ~$0.019/run | Eleve |
| WebUI (self-hosted) | Interface web locale | GPU propre | Moyen |
| CLI (self-hosted) | Ligne de commande | GPU propre | Moyen |
| VPS Linux | Self-hosted sur 31.220.84.152 | GPU requis | Eleve |

---

## VERDICT POUR DAW-AVA

**Statut : CANDIDAT SERIEUX (remonte grace aux API cloud pay-as-you-go)**

**Forces** :
- Le plus eprouve pour le chant (enorme communaute, tutoriels, troubleshooting)
- 48 kHz
- Actif et maintenu (v3)
- **API REST cloud cle en main** (Replicate, Eachlabs) = zero infra, zero abonnement
- **~$0.03 par chanson** = le moins cher de tous les fournisseurs SVC
- Training cloud en 6 min pour $0.32 (vs 3 jours self-hosted)
- Upload de modele custom (.pth) — entrainement une fois, conversion illimitee

**Faiblesses** :
- Entrainement obligatoire (pas de zero-shot)
- Necessite 10-60 min de chant a cappella du Cap'taine
- Qualite dependante de la qualite des donnees d'entrainement
- Version cloud = RVC v2 (pas encore v3 sur Replicate/Eachlabs)

**Comparaison economique** :

| Fournisseur | 1er morceau | 10 morceaux | 50 morceaux |
|-------------|-------------|-------------|-------------|
| **RVC Replicate** | **$0.35** | **$0.66** | **$2.02** |
| Voice-Swap (pack) | £11.99 (~$15) | ~£48 (~$60) | ~£180 (~$225) |
| Kits.ai Starter | $10/mois | $10/mois | $10/mois |

---

## SOURCES

- [RVC-Project GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- [Replicate — realistic-voice-cloning](https://replicate.com/zsxkib/realistic-voice-cloning)
- [Replicate — train-rvc-model](https://replicate.com/replicate/train-rvc-model)
- [Eachlabs — RVC v2](https://www.eachlabs.ai/rvc-project/rvc/rvc-v2)
- [Eachlabs — Train RVC](https://www.eachlabs.ai/eachlabs/eachlabs/train-rvc)
- [RunPod Serverless](https://www.runpod.io/product/serverless)
- [RunPod RVC template](https://github.com/mahdjalili/rvcv2-runpod)
- [RVC Cloud Deploy Guide](https://www.runpod.io/articles/guides/ai-engineer-guide-rvc-cloud)
- [Kenneth Lamar RVC Guide](https://kennethmlamar.com/posts/voice-clones-guide/)

---

*Veille DAW-Ava — RVC : la puissance communautaire a $0.03/chanson*
