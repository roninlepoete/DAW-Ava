# Voice-Swap — Singing Voice Conversion (musiciens + producteurs)

> Plateforme SVC pour musiciens avec plugin VST/AU et roster d'artistes.
> Date de veille : 2026-04-12
> Source : https://www.voice-swap.ai

---

## CE QUE C'EST

Plateforme SVC orientee musiciens et producteurs.
Convertir une voix chantee en une autre, entrainer un modele vocal custom.
Plugin VST/AU integre pour utilisation directe dans le DAW.
Roster d'artistes pro (Robert Owens, Ayah Marar) avec royalties reversees.
Protection copyright BMAT integree.

---

## API — ENTERPRISE GATE, PAS EN LIBRE-SERVICE

**L'API n'est PAS publique.** Acces via la page /business uniquement.

| Etape | Detail |
|-------|--------|
| 1. Formulaire | Remplir nom, email, entreprise, message sur /business |
| 2. Token essai | Token API 30 jours pour evaluation |
| 3. Production | Contacter les ventes pour tarif et acces permanent |
| Docs API | /openapi (visible apres connexion uniquement) |

**Consequence pour DAW-Ava** : impossible d'integrer sans passer par leur equipe commerciale.
Pas de signup self-service, pas de cle API generee en autonomie.

---

## PRICING — CREDITS (abonnement OU achat ponctuel, en livres sterling)

### Achat ponctuel — PAY-AS-YOU-GO (sans abonnement)

**OUI, on peut acheter des credits SANS abonnement.**

| Offre | Prix | Credits | Abonnement requis |
|-------|------|---------|-------------------|
| One-shot | £11.99 | 75 | **NON** |

75 credits = 1 cycle complet (train 40 + convert 1 + download 10 = 51) + 24 credits restants (~2 conversions+downloads).
Un seul pack visible sur la page pricing. Pas d'info sur l'achat de packs multiples.

### Plans mensuels (optionnels)

| Plan | Prix/mois | Credits/mois | GPU rapide |
|------|-----------|--------------|------------|
| Beginner | £6.99 | 50 | Non |
| Pro | £9.99 | 150 | Non |
| Ultimate | £39.99 | 1 000 | OUI (2x faster) |

### Cout des operations (en credits)

| Action | Credits |
|--------|---------|
| Voice conversion | 1 |
| Stem separation | 3 |
| VST usage | 3 |
| Download | 10 |
| Upload Soundcloud | 10 |
| **Training modele** | **40** |

### Analyse d'un cycle complet

Un cycle typique (entrainer + convertir + telecharger) :
- Training : 40 credits
- Conversion : 1 credit
- Download : 10 credits
- **Total minimum : 51 credits**

Le plan Beginner (50 credits) ne couvre PAS un cycle complet.
Le plan Pro (150 credits) couvre ~3 cycles par mois.
Le plan Ultimate (1 000 credits) couvre ~19 cycles par mois.

---

## ENTRAINEMENT DU MODELE VOCAL

| Parametre | Detail |
|-----------|--------|
| **Duree audio** | Minimum 20 min, recommande 40 min |
| **Contenu** | Voix chantee seule |
| **Cout** | 40 credits par entrainement |
| **Resultat** | Modele custom disponible dans le VST et sur la plateforme web |

---

## PLUGIN VST/AU

| Critere | Detail |
|---------|--------|
| **Type** | VST/AU gratuit (inclus dans tous les plans) |
| **Fonction** | Conversion vocale directe dans le DAW |
| **Cout par usage** | 3 credits par utilisation VST |
| **Avantage** | Pas besoin de CLI/API — le Cap'taine convertit depuis son DAW |

---

## VERDICT POUR DAW-AVA

**Forces** :
- Plugin VST/AU = integration DAW native (zero CLI)
- Roster d'artistes pro = qualite validee par l'industrie
- Protection copyright BMAT
- Achat ponctuel possible (£11.99 pour 75 credits, sans abonnement)

**Faiblesses** :
- API enterprise-gate = friction d'acces maximale pour l'integration programmatique
- Pricing en credits = pas transparent (un cycle = 51 credits minimum)
- Plan Beginner insuffisant pour un seul cycle complet
- Tarifs en livres sterling (pas en dollars)
- Pas de Voice Blending comme Kits.ai

**Comparaison avec Kits.ai** :

| Critere | Kits.ai | Voice-Swap |
|---------|---------|------------|
| API publique | OUI (token self-service) | NON (enterprise gate) |
| Plugin DAW | Non | OUI (VST/AU gratuit) |
| Pricing | Abonnement $10-60/mois | Credits £6.99-39.99/mois |
| Voice Blending | OUI | NON |
| Achat ponctuel | NON | OUI (£11.99 / 75 credits) |
| Transparence prix | Claire | Opaque (credits) |

**Recommandation** :
- Si le Cap'taine veut travailler DANS son DAW : Voice-Swap (VST)
- Si le Cap'taine veut un pipeline automatise via API : Kits.ai
- Les deux approches sont complementaires, pas exclusives

---

## SOURCES

- [Voice-Swap](https://www.voice-swap.ai)
- [Voice-Swap Pricing](https://www.voice-swap.ai/pricing)
- [Voice-Swap Business/API](https://www.voice-swap.ai/business)

---

*Veille DAW-Ava — "La voix du Cap'taine est sacree"*
