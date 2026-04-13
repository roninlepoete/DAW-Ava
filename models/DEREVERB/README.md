# DEREVERB — Suppression d'echo et de reverb sur stems vocaux

> Etape CRITIQUE du pipeline SVC. Le RVC reproduit fidelement les defauts du stem source.
> Un stem avec reverb = une voix convertie avec reverb + ronflement.
> Le de-reverb doit etre AVANT le SVC, jamais apres.
>
> Derniere MAJ : 2026-04-12

---

## POURQUOI C'EST INDISPENSABLE

Les morceaux generes par Suno (et la plupart des generateurs musicaux IA) ont de la reverb
cuite dans le vocal. Demucs separe les stems mais conserve la reverb du vocal.
Quand ce stem passe dans le RVC (SVC), la reverb est amplifiee et cree un ronflement
de fond ("humming") autour de la voix convertie.

**Pipeline correct** :
```
Source MP3 → Demucs (stems) → DE-REVERB → SVC (RVC) → voix propre
```

**Pipeline incorrect** (ronflement garanti) :
```
Source MP3 → Demucs (stems) → SVC (RVC) → ronflement
```

---

## MODELES DISPONIBLES

### Testes et operationnels

| Modele | Architecture | Capacite | SDR | Taille | Resultat DAW-Ava |
|--------|-------------|----------|-----|--------|------------------|
| **UVR-DeEcho-DeReverb** | VR Arch | Echo + reverb en 1 passe | — | 224 Mo | MEILLEUR operationnel. 1 passe, combine, ~3 min CPU |
| UVR-De-Echo-Aggressive | VR Arch | Echo seulement (agressif) | — | 127 Mo | Bon pour echo, pas de reverb. Utile en passe 1 d'un chain |
| Reverb_HQ_By_FoxJoy | MDX-Net | Reverb seulement | — | 66.8 Mo | Bon reverb, pas d'echo. Utile en passe 2 d'un chain |
| UVR-DeNoise | VR Arch | Bruit/ronflement | — | 127 Mo | Post-SVC pour retirer le ronflement residuel |

### Non testes (disponibles dans audio-separator)

| Modele | Architecture | Capacite | SDR | Notes |
|--------|-------------|----------|-----|-------|
| UVR-De-Echo-Normal | VR Arch | Echo (conservateur) | — | Moins agressif que Aggressive |
| MDX23C-De-Reverb | MDX23C | Reverb | — | Alternative a FoxJoy |
| BS-Roformer-De-Reverb | BS-Roformer | Reverb | — | Haute qualite, a tester |

### State-of-the-art (non operationnels — incompatibilite audio-separator 0.44.1)

| Modele | Architecture | SDR | Taille | Source | Probleme |
|--------|-------------|-----|--------|--------|----------|
| dereverb_echo_mbr_fused | MelBand Roformer | — | 456 Mo | Sucial/HuggingFace | Config STFT incompatible |
| dereverb_echo_mbr_v2 | MelBand Roformer | 13.48 | — | Sucial/HuggingFace | Non teste |
| dereverb_big_mbr | MelBand Roformer | — | — | Sucial/HuggingFace | Non teste |
| dereverb_super_big_mbr | MelBand Roformer | — | — | Sucial/HuggingFace | Non teste |
| dereverb_anvuew_sdr_19.17 | MelBand Roformer | 19.17 | — | anvuew/HuggingFace | Non teste |

**Note** : Les modeles MelBand Roformer Sucial et anvuew sont consideres state-of-the-art
par la communaute RVC mais necessitent une version plus recente d'audio-separator
ou un chargement manuel. A surveiller pour les futures mises a jour du package.

---

## STRATEGIE DE NETTOYAGE TESTEE

### Strategie 1 : Modele combine en 1 passe (RECOMMANDEE)

```
UVR-DeEcho-DeReverb (1 passe, echo + reverb) → stem dry
```

Avantage : simple, rapide (~3 min CPU), un seul modele.

### Strategie 2 : Chain 2 passes

```
UVR-De-Echo-Aggressive (passe 1) → Reverb_HQ_FoxJoy (passe 2) → stem ultra-dry
```

Avantage : plus agressif sur chaque defaut separement.
Inconvenient : 2x plus long (~6 min CPU), peut degrader le signal.

### Strategie 3 : Cloud HuggingFace

```
r3gm/Audio_separator Space (Gradio API, dereverb=True) → stem cloud-dry
```

Avantage : cloud, gratuit, GPU.
Inconvenient : modeles basiques (pas les Sucial/anvuew), reverb residuelle possible.

---

## CHOIX RECOMMANDE POUR DAW-AVA

**UVR-DeEcho-DeReverb** (local, VR Arch, 1 passe combine).
C'est le meilleur compromis qualite/simplicite/vitesse avec audio-separator 0.44.1.

Si la qualite n'est toujours pas suffisante : attendre la mise a jour d'audio-separator
supportant les modeles MelBand Roformer, ou deployer ces modeles manuellement.

---

## SOURCES

- [audio-separator PyPI](https://pypi.org/project/audio-separator/)
- [Sucial/Dereverb-Echo_Mel_Band_Roformer](https://huggingface.co/Sucial/Dereverb-Echo_Mel_Band_Roformer)
- [anvuew/deverb_bs_roformer](https://huggingface.co/anvuew/deverb_bs_roformer)
- [Derur/UVR-models](https://huggingface.co/Derur/UVR-models)

---

*"Le dry est sacre. Pas de reverb dans le SVC."*
