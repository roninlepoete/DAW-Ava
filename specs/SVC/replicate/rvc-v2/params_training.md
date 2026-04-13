# RVC v2 — Parametres de Training (Replicate)

> Suivi des parametres d'entrainement et de leurs resultats.
> Endpoint : `replicate/train-rvc-model:0397d5e2...`
> Chaque run est documente avec ses parametres et son verdict qualite.

---

## SCHEMA API COMPLET

| Parametre | Type | Requis | Defaut | Valeurs | Description |
|-----------|------|--------|--------|---------|-------------|
| `dataset_zip` | file | OUI | — | ZIP | Structure : `dataset/<nom>/split_<i>.wav` |
| `sample_rate` | string | NON | `48k` | `40k`, `48k` | 48k = plus de detail aigus |
| `version` | string | NON | `v2` | `v1`, `v2` | v2 recommande |
| `f0method` | string | NON | `rmvpe_gpu` | `pm`, `dio`, `harvest`, `rmvpe`, `rmvpe_gpu` | Extraction pitch. `rmvpe_gpu` = meilleur pour le chant |
| `epoch` | integer | NON | `10` | 1-500 | Passes sur le dataset. Plus = mieux, mais risque surapprentissage |
| `batch_size` | string | NON | `7` | — | Taille des lots. 7 = optimum Replicate |

## PIEGES TYPES (ne pas repeter)

1. `batch_size` est un STRING, pas un integer
2. `epoch` est un INTEGER, pas un string
3. Le ZIP doit contenir `dataset/<nom>/split_<i>.wav` — PAS un seul WAV a la racine
4. Segmenter en clips ~10s via ffmpeg avant de zipper
5. Version `cf360587...` desactivee — utiliser `0397d5e2...`
6. Passer le fichier via `open('file', 'rb')`, pas une URL files API

---

## PREPARATION DU DATASET

```
1. Enregistrer 20+ min de chant + parole (WAV 44.1/48 kHz, 16-bit, mono, DRY)
2. Segmenter : ffmpeg -i chant-complet.wav -f segment -segment_time 10 -c copy split_%03d.wav
3. Zipper : dataset/<nom_modele>/split_000.wav ... split_NNN.wav
4. Upload direct via open() dans replicate.run()
```

---

## HISTORIQUE DES RUNS

### Run #1 — Cap'taine Fab (2026-04-12)

| Parametre | Valeur |
|-----------|--------|
| **Source audio** | `sample-myVoice/chant-complet.wav` (20 min 05 sec, 44100 Hz, 16-bit, mono) |
| **Clips** | 121 clips x 10 sec |
| **sample_rate** | `48k` |
| **version** | `v2` |
| **f0method** | `rmvpe_gpu` |
| **epoch** | `50` |
| **batch_size** | `7` |
| **Cout** | En attente |
| **Duree** | En attente |
| **Modele produit** | En attente |
| **Verdict qualite** | En attente — a evaluer sur DestinyInYouInMe stems vocals |

---

*Specs DAW-Ava — training RVC v2 sur Replicate*
