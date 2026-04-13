# SVC — Singing Voice Conversion

> Comparatif des fournisseurs SVC pour DAW-Ava.
> Details de chaque fournisseur dans son sous-repertoire respectif.
>
> Derniere MAJ : 2026-04-12

---

## CAS D'USAGE

Remplacer la voix chantee generee par Suno par la voix reelle du Cap'taine,
en preservant melodie, rythme, vibrato, expression et timing.
Qualite production musicale professionnelle exigee.

---

## FOURNISSEURS DOCUMENTES

| Fournisseur | Dossier | Type | Statut |
|-------------|---------|------|--------|
| **Voice-Swap** | `Voice-Swap/` | Commercial, VST + credits | CANDIDAT (workflow DAW) |
| **RVC v2/v3** | `RVC/` | Open source, API cloud pay-as-you-go | CANDIDAT (cout minimal) |
| **Seed-VC** | `Seed-vc/` | Open source, zero-shot | BACKUP (test rapide) |
| Kits.ai | `Kits-ai/` | Commercial, abonnement | REJETE |
| Musicfy | `Musicfy/` | Commercial, abonnement | A EVALUER |
| Revocalize | `Revocalize/` | Commercial, VST $49 | A EVALUER |

---

## COMPARATIF — COMMERCIAUX

| Critere | Voice-Swap | Kits.ai | Musicfy | Revocalize |
|---------|------------|---------|---------|------------|
| Concu pour le chant | OUI | OUI | OUI (covers) | OUI |
| API REST publique | Enterprise gate | Self-service | OUI | OUI |
| Plugin DAW (VST/AU) | OUI (gratuit) | NON | NON | OUI ($49) |
| **Pay-as-you-go** | **OUI (£11.99/75 cr.)** | NON | NON | Free 5 min |
| Abonnement | £6.99-£39.99/mois | $10-$60/mois | $9.99-$69.99/mois | Non public |
| Voice Blending | NON | OUI | NON | Non documente |
| Copyright integre | OUI (BMAT) | NON | NON | NON |
| Credibilite | Fondateurs producteurs | Marketing > realite | Hobbyiste | Signaux positifs |
| **Trustpilot** | Pas de page | **1.4/5 (94% 1 etoile)** | Non verifie | Non verifie |
| **Test Cap'taine** | A tester | **REJETE** | Non teste | Non teste |

## COMPARATIF — OPEN SOURCE

| Critere | Seed-VC | RVC v2/v3 | HQ-SVC (AAAI 2026) |
|---------|---------|-----------|---------------------|
| Zero-shot | OUI (10-30s ref) | NON (entrainement) | OUI |
| Mode chant dedie | OUI (44.1 kHz, F0) | Via communaute (48 kHz) | OUI (44.1 kHz) |
| GPU requis | ~6 Go VRAM | ~8 Go VRAM | Consumer-grade |
| Entrainement | AUCUN | 10-60 min audio, ~3j GPU | AUCUN |
| Maintenance | Archive (nov 2025) | ACTIF (v3) | Tres recent (dec 2025) |
| Communaute | Moyenne | La plus large | Quasi inexistante |
| Deploiement API | FastAPI adaptable | Replicate $0.034/run | Gradio |

---

## CONSTAT FAL.AI — AVRIL 2026

Aucun modele SVC sur Fal.ai. Le pipeline SVC necessite un fournisseur externe
ou un deploiement self-hosted.

---

## COMPARATIF ECONOMIQUE

| Fournisseur | 1er morceau | 10 morceaux | 50 morceaux | Abonnement |
|-------------|-------------|-------------|-------------|------------|
| **RVC Replicate** | **$0.35** | **$0.66** | **$2.02** | **NON** |
| RVC Eachlabs | ~$0.33 | ~$0.63 | ~$1.83 | NON |
| Voice-Swap (pack) | ~$15 | ~$60 | ~$225 | NON (ou £6.99+/mois) |
| Kits.ai Starter | $10/mois | $10/mois | $10/mois | OUI |
| Seed-VC | $0 (GPU propre) | $0 | $0 | NON |

---

## STRATEGIE RECOMMANDEE

```
Etape 1 : Voice-Swap (£11.99, pay-as-you-go, VST DAW)
          → Ideal si workflow dans le DAW du Cap'taine
          → Si qualite OK : pipeline operationnel

Etape 2 : RVC v2 via Replicate ($0.35 premiere chanson, $0.03 les suivantes)
          → API REST cle en main, zero abonnement, zero infra
          → Training cloud en 6 min ($0.32, une seule fois)
          → Le moins cher de tous sur le volume

Etape 3 : Seed-VC zero-shot (gratuit, 10-30s de voix)
          → Test rapide sans entrainement
          → Deploiement VPS ou RunPod
```

---

## ECHANTILLON VOCAL — RESSOURCE PARTAGEE

**Repertoire** : `sample-myVoice/` a la racine du projet — ressource partagee par tout DAW-Ava.

| Fichier | Usage | Fournisseurs |
|---------|-------|-------------|
| `chant-30s.wav` | Reference zero-shot | Seed-VC |
| `chant-complet.wav` | Entrainement modele | Voice-Swap, RVC |
| `parole-30s.wav` | Reference parole | Seed-VC, ElevenLabs |

**Statut** : EN ATTENTE — le Cap'taine doit enregistrer.

---

*Veille DAW-Ava — "La voix du Cap'taine est sacree. Pas de compromis."*
