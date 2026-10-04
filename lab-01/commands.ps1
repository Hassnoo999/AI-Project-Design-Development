# Commands used for Lab 01. Run from the repository root.
# Environment installation commands are in setup_environment.ps1.
python lab-01/setup_structure.py
python -m venv aipdd_env
. .\aipdd_env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -m pip install numpy opencv-python matplotlib ultralytics jupyter ipykernel nbconvert
python -m pip check
python -m pip freeze --all | Set-Content -Encoding utf8 requirements.txt
python -m ipykernel install --user --name aipdd_env --display-name 'Python (aipdd_env)'
python -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=aipdd_env --ExecutePreprocessor.timeout=180 notebooks/lab01_setup.ipynb
python -m jupyter nbconvert --to html --output-dir lab-01 --output lab01_setup notebooks/lab01_setup.ipynb

# Git workflow performed (the repository already had its first commit).
# git init
# git config user.name 'Hassan Khan'
# git config user.email 'hassanbinsaqib01@gmail.com'
# git add .gitignore data models notebooks src configs logs lab-01/setup_structure.py
# git commit -m 'Add standard AI project structure and environment setup scripts'
# git switch -c feature/lab01-setup
# git add requirements.txt
# git commit -m 'Pin aipdd_env dependencies for Lab 01'
# git switch main
# git merge --no-ff feature/lab01-setup -m 'Merge Lab 01 environment setup'
# git status
# git log --oneline --graph --decorate --all
# git branch -av

# To open Jupyter interactively:
# python -m jupyter notebook notebooks/lab01_setup.ipynb
