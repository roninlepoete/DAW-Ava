"""
DAW-Ava — Client RunPod Serverless GPU
Appelle l'endpoint daw-ava-gpu pour les operations lourdes.

Operations :
  - dereverb : suppression echo + reverb
  - stems    : separation vocal + instrumental

Usage :
  python runpod_client.py dereverb <audio_url>
  python runpod_client.py stems <audio_url>
"""

import os
import sys
import time
import json
import winreg
import requests
from pathlib import Path


def _get_api_key():
    """Charge RUNPOD_API_KEY depuis le registre Windows."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        val, _ = winreg.QueryValueEx(key, "RUNPOD_API_KEY")
        winreg.CloseKey(key)
        return val
    except (FileNotFoundError, OSError):
        raise RuntimeError("RUNPOD_API_KEY introuvable dans le registre Windows.")


ENDPOINT_ID = "j8w78y9nsr72ec"
BASE_URL = f"https://api.runpod.ai/v2/{ENDPOINT_ID}"


def run_job(operation, params):
    """Envoie un job et attend le resultat."""
    api_key = _get_api_key()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {"input": {"operation": operation, **params}}

    # Submit job
    print(f"[RunPod] Envoi job '{operation}'...")
    r = requests.post(f"{BASE_URL}/run", json=payload, headers=headers)
    r.raise_for_status()
    job = r.json()
    job_id = job.get("id")
    print(f"[RunPod] Job ID : {job_id}")
    print(f"[RunPod] Status : {job.get('status')}")

    # Poll pour le resultat
    while True:
        time.sleep(5)
        r = requests.get(f"{BASE_URL}/status/{job_id}", headers=headers)
        r.raise_for_status()
        status = r.json()
        state = status.get("status")
        print(f"[RunPod] Status : {state}")

        if state == "COMPLETED":
            return status.get("output")
        elif state == "FAILED":
            print(f"[RunPod] ERREUR : {status.get('error')}")
            return None
        elif state in ("IN_QUEUE", "IN_PROGRESS"):
            continue
        else:
            print(f"[RunPod] Status inconnu : {state}")
            return None


def save_b64_file(b64_data, filename, output_dir):
    """Decode base64 et sauvegarde un fichier."""
    import base64
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / filename
    with open(out_file, "wb") as f:
        f.write(base64.b64decode(b64_data))
    size_mb = out_file.stat().st_size / (1024 * 1024)
    print(f"  Sauve : {out_file.name} ({size_mb:.1f} Mo)")
    return out_file


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage :")
        print("  python runpod_client.py dereverb <audio_url> [model]")
        print("  python runpod_client.py stems <audio_url>")
        sys.exit(1)

    op = sys.argv[1]
    audio_url = sys.argv[2]

    if op == "dereverb":
        model = sys.argv[3] if len(sys.argv) > 3 else "UVR-DeEcho-DeReverb.pth"
        result = run_job("dereverb", {"audio_url": audio_url, "model": model})
        if result:
            for name, data in result.items():
                if isinstance(data, dict) and "data_b64" in data:
                    save_b64_file(data["data_b64"], data["filename"], "output/runpod")

    elif op == "stems":
        result = run_job("stems", {"audio_url": audio_url})
        if result:
            for name, data in result.items():
                if isinstance(data, dict) and "data_b64" in data:
                    save_b64_file(data["data_b64"], data["filename"], "output/runpod")

    else:
        print(f"Operation inconnue : {op}")
