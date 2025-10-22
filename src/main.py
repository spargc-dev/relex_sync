# src/main.py
import sys
from dotenv import load_dotenv
from src.services.orchestrator import Orchestrator
from src.config.interfaces import REGISTRY
# import subprocess, os # para subir a ABS

def main():
    load_dotenv()
    orch = Orchestrator()

    # Si pasas nombres por CLI, corre solo esas interfaces; si no, corre todas
    # Ejemplos:
    #   python -m src.main product_groups
    #   python -m src.main campaigns
    #   python -m src.main product_groups campaigns
    #   python -m src.main
    targets = sys.argv[1:] or list(REGISTRY.keys())

    for name in targets:
        if name not in REGISTRY:
            print(f"❌ Interfaz desconocida: {name}")
            continue
        try:
            path = orch.run_interface(name)
            print(f"✅ {name}: {path}")
        except Exception as e:
            print(f"❌ {name} falló: {e}")

    #repo_root = os.path.dirname(os.path.abspath(__file__))  # src/ # para subir a ABS
    #repo_root = os.path.abspath(os.path.join(repo_root, ".."))  # raíz # para subir a ABS

    #ps_script = os.path.join(repo_root, "scripts", "upload.ps1") # para subir a ABS
    #subprocess.run( # para subir a ABS
    #    ["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_script], # para subir a ABS
    #    check=True # para subir a ABS
    #) # para subir a ABS

if __name__ == "__main__":
    main()
