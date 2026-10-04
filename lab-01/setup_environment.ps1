# Run from the repository root. Installation is CPU only.
$ErrorActionPreference = 'Stop'
python -m venv aipdd_env
. .\aipdd_env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -m pip install numpy opencv-python matplotlib ultralytics jupyter ipykernel nbconvert
python -m pip check
python -m pip freeze --all | Set-Content -Encoding utf8 requirements.txt
python -m ipykernel install --user --name aipdd_env --display-name 'Python (aipdd_env)'
Write-Host 'For an exact reinstall, use the pinned requirements.txt and the CPU wheel index.'
