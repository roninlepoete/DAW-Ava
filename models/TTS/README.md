# TTS — Text-to-Speech (synthese vocale)

> Transformer du texte en voix parlee. Clonage vocal possible.

---

## Outils disponibles

| Outil | Endpoint Fal.ai | Prix | Forces |
|-------|-----------------|------|--------|
| Kokoro | `fal-ai/kokoro/american-english` | $0.02/1000 chars | Volume, economique, multi-langues |
| F5-TTS | `fal-ai/f5-tts` | $0.05/1000 chars | Clonage vocal (audio reference requis) |
| Dia TTS | `fal-ai/dia-tts` | $0.04/1000 chars | Multi-locuteurs, controle emotion, dialogue |
| Orpheus | `fal-ai/orpheus-tts` | $0.05/1000 chars | Qualite humaine maximale, expressivite |
| ElevenLabs Multilingual | `fal-ai/elevenlabs/tts/multilingual-v2` | Variable | 29 langues, francais excellent |
| Qwen 3 TTS | `fal-ai/qwen-3-tts/clone-voice/1.7b` | Pay-per-use | Clone zero-shot |
| MiniMax Speech-02 HD | `fal-ai/minimax/voice-clone` | Pay-per-use | Clone haute qualite |

## Choix DAW-Ava

**Kokoro** pour le volume. **ElevenLabs Multilingual** pour le francais pro. **Dia TTS** pour le clonage Mikhaelize. Voir `specs/TTS/fal-ai/`.
