# RVC v2 — Parametres d'Inference (Replicate)

> Suivi des parametres de conversion vocale et de leurs resultats.
> Endpoint : `zsxkib/realistic-voice-cloning`
> Version : `0a9c7c558af4c0f20667c1bd1260ce32a2879944a0b9e44e1398660c077b1550`
> Chaque run est documente avec ses parametres et le verdict du Cap'taine.

---

## SCHEMA API COMPLET (verifie sur OpenAPI schema)

| Parametre | Type | Defaut | Description |
|-----------|------|--------|-------------|
| `song_input` | string (file) | — | Audio source (la voix a remplacer) |
| `rvc_model` | enum | `Squidward` | Preset ou `CUSTOM` pour modele perso |
| `custom_rvc_model_download_url` | string | — | URL du modele .zip entraine |
| `pitch_change` | enum/string | `no-change` | Transposition. Valeur = `no-change` ou autre preset |
| `pitch_change_all` | number | `0` | Ajustement fin en demi-tons (float) |
| `pitch_detection_algorithm` | enum | `rmvpe` | Extraction pitch. `rmvpe` = meilleur pour le chant |
| `index_rate` | number | `0.5` | Poids timbre entraine vs source (0.0-1.0) |
| `filter_radius` | integer | `3` | Lissage pitch (0-7) |
| `rms_mix_rate` | number | `0.25` | Balance volume source vs modele (0.0-1.0) |
| `protect` | number | `0.33` | Protection consonnes S/T/P (0.0-0.5) |
| `output_format` | enum | `mp3` | `mp3` ou `wav` |
| `reverb_size` | number | `0.15` | Taille reverb |
| `reverb_damping` | number | `0.7` | Amortissement reverb |
| `reverb_dryness` | number | `0.8` | Ratio signal sec |
| `reverb_wetness` | number | `0.2` | Ratio signal reverbe |
| `crepe_hop_length` | integer | `128` | Hop length pour CREPE (si f0=crepe) |
| `main_vocals_volume_change` | number | `0` | Ajustement volume voix principale (dB) |
| `instrumental_volume_change` | number | `0` | Ajustement volume instrumental (dB) |
| `backup_vocals_volume_change` | number | `0` | Ajustement volume choeurs (dB) |

### PIEGES DE TYPES (ne pas repeter)

- `pitch_change` = **string/enum** (pas integer). Utiliser `"no-change"` pour aucun changement
- `pitch_change_all` = **number** pour l'ajustement fin en demi-tons
- `filter_radius` = **integer**
- Tous les autres numeriques = **number** (float)
- `output_format` = **string enum** (`"mp3"` ou `"wav"`)
- La version du modele change regulierement. Toujours utiliser `model.latest_version.id`

---

## GUIDE DE REGLAGE PAR ETAPE

### Iteration 1 — Valeurs conservatrices (premier test)

```
pitch_change              = "no-change"
pitch_change_all          = 0
pitch_detection_algorithm = "rmvpe"
index_rate                = 0.5
filter_radius             = 3
rms_mix_rate              = 0.25
protect                   = 0.33
output_format             = "wav"
```

### Iteration 2+ — Ajustements selon le verdict du Cap'taine

| Probleme entendu | Parametre a ajuster | Direction |
|-----------------|---------------------|-----------|
| Voix trop "source", pas assez "moi" | `index_rate` | Monter (0.6 - 0.8) |
| Voix trop "moi", perd la melodie | `index_rate` | Baisser (0.3 - 0.4) |
| Pitch instable, wobbly | `filter_radius` | Monter (5 - 7) |
| Artefacts sur S, T, P | `protect` | Monter (0.4 - 0.5) |
| Trop de souffle/bruit | `rms_mix_rate` | Monter (0.5 - 0.7) |
| Dynamiques ecrasees | `rms_mix_rate` | Baisser (0.1 - 0.0) |
| Tonalite trop haute/basse | `pitch_change_all` | Ajuster (+2 ou -2) |
| Veut de la reverb | `reverb_wetness` | Monter (0.3 - 0.5) |

---

## HISTORIQUE DES RUNS

### Run #1 — Iteration 1 (2026-04-12)

| Parametre | Valeur |
|-----------|--------|
| **Source** | `output/DestinyInYouAndMe/stems/vocals.mp3` |
| **Modele** | `captaine-fab.zip` (training run #1, 50 epochs, 121 clips) |
| **pitch_change** | `no-change` |
| **pitch_change_all** | `0` |
| **pitch_detection_algorithm** | `rmvpe` |
| **index_rate** | `0.5` |
| **filter_radius** | `3` |
| **rms_mix_rate** | `0.25` |
| **protect** | `0.33` |
| **output_format** | `wav` |
| **Resultat** | `output/DestinyInYouAndMe/voice/vocals-rvc-iter1.wav` (58.3 Mo) |
| **Verdict Cap'taine** | **EN ATTENTE** |

---

*Specs DAW-Ava — inference RVC v2 sur Replicate*
*"Le Cap'taine est le juge, Ava tourne les boutons."*
