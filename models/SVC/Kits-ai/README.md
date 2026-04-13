# Kits.ai — Singing Voice Conversion (specialiste musique)

> Leader du marche SVC musical. Plateforme entierement dediee a la production musicale.
> Date de veille : 2026-04-12
> Source : https://kits.ai

---

## CE QUE C'EST

Plateforme SVC concue pour les musiciens et producteurs.
Permet de convertir une voix chantee en une autre (modele entraine sur ta voix)
tout en preservant melodie, rythme, vibrato, expression et timing.

---

## FONCTIONNALITES CLES

| Fonction | Description |
|----------|-------------|
| **Voice Conversion** | Remplacer la voix source par le modele vocal entraine |
| **Voice Blending** | Mixer deux voix (ex: 70% toi + 30% source pour naturalness) |
| **Voice Model Training** | Entrainer un modele vocal custom sur tes echantillons |
| **Vocal Separation** | Separation stems integree (alternative a Demucs) |
| **Instant Voice Clone** | Clonage rapide (plan Starter+) |
| **Professional Voice Clone** | Clonage haute qualite (plan Producer+) |
| **Singing Voice Synthesizer** | Synthese vocale chantee (plan Producer+) |
| **Choir Tool** | Outil chorale (plan Starter+) |

---

## PRICING — ABONNEMENT UNIQUEMENT

**Modele de facturation : abonnement mensuel ou annuel. PAS de pay-as-you-go. PAS de credits.**

| Plan | Prix/mois | Prix/an (-20%) | Conversions | Downloads | Voice slots |
|------|-----------|----------------|-------------|-----------|-------------|
| **Free** | $0 | — | 15 min | 0 min | 0 |
| **Starter** | $10 | $8/mois | Illimite | 15 min/mois | 2 |
| **Producer** | $30 | $24/mois | Illimite | 60 min/mois | Illimite |
| **Professional** | $60 | $48/mois | Illimite | Illimite | Illimite |

### Goulot d'etranglement : les minutes de DOWNLOAD

- Les conversions sont illimitees sur tous les plans payes
- Ce qui est limite = le telechargement du resultat
- Starter = 15 min/mois → ~4-5 morceaux de 3 min
- Producer = 60 min/mois → ~20 morceaux de 3 min
- Les minutes non utilisees sont reportees au mois suivant (rollover)

### API

- Acces API disponible avec token generable depuis le portail
- Tarif API entree de gamme : $14.99/mois (legerement different du plan web)
- Pas de tarif pay-per-use public pour l'API
- Pas de documentation detaillee sur les rate limits API

### Annulation

- Les modeles vocaux custom sont GELES (pas supprimes) a l'annulation
- Ils se reactiveront au renouvellement

---

## ENTRAINEMENT DU MODELE VOCAL

| Parametre | Requis |
|-----------|--------|
| **Duree audio** | 30 a 60 minutes de voix chantee |
| **Format** | WAV 16-bit |
| **Contenu** | Voix seule, DRY (sans reverb, sans delay, sans effets) |
| **Monophonique** | OUI — une seule voix, pas d'harmonies ni de doublages |
| **Pas de musique** | Voix a cappella uniquement |
| **Style** | Un modele = un style (pop, rock, etc. separement) |
| **Temps d'entrainement** | 30 min a plusieurs heures |

---

## API — ENDPOINTS CONNUS

| Endpoint | Fonction |
|----------|----------|
| Voice Conversion | Convertir un audio avec un modele vocal |
| Voice Model | Gestion des modeles vocaux (create, list, delete) |
| Vocal Separation | Separation stems |
| TTS | **DEPRECIE depuis sept 2025** |

**Token** : generer depuis https://kits.ai → portail API → "New Token"

---

## RETOURS D'EXPERIENCE (terrain + Trustpilot)

**Trustpilot : 1.4/5 (47 avis, 94% une etoile)** — avril 2026.

Retours authentiques recurrents :
- Voix robotiques, pitch qui craque sur les aigus
- Artefacts frequents sur les sibilantes (S, T) et les souffles
- Timing decale par rapport a l'original
- Clonage vocal souvent inutilisable
- ~60% des outputs estimes utilisables (et encore, avec post-production)
- Paywalling agressif de fonctions anciennement gratuites (apres rachat par Splice)

**Test Cap'taine Fab** : essaye et juge "pas fort, voire plutot nul".

**Estimation** : qualite sur le papier, decevant en pratique.

---

## VERDICT POUR DAW-AVA

**Statut : NON RETENU — qualite insuffisante, confirmee par test terrain + Trustpilot.**

**Forces theoriques** :
- Voice Blending (concept interessant)
- API REST documentee
- Tout-en-un (conversion + separation + entrainement)

**Faiblesses redibitoires** :
- **Qualite reelle decevante** (1.4/5 Trustpilot, test Cap'taine negatif)
- Abonnement obligatoire (pas de pay-as-you-go)
- 15 min download/mois sur le Starter ($10) = juste si beaucoup d'iterations
- API a $14.99/mois en entree = cout fixe meme pour un usage ponctuel
- Hors ecosysteme Fal.ai (client Python a creer)

**Recommandation** :
- Pour tester : plan Free (15 min de conversion, pas de download → ecouter en ligne)
- Pour produire : plan Producer ($30/mois, 60 min download, Professional Voice Clone)
- L'API necessite un nouveau skill WSG : `Core/Scripts/Skills/Python/kitsai/`

---

## SOURCES

- [Kits.ai](https://kits.ai)
- [Kits.ai Pricing](https://kits.ai/pricing)
- [Kits.ai API](https://kits.ai/api)

---

*Veille DAW-Ava — "La voix du Cap'taine est sacree"*
