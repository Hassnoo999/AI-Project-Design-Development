# AI Project Design and Development

**Student:** Hassan Bin Saqib (231170)  
**Course:** AI Project Design and Development, Semester 7, Air University

## Lab folders

| Folder | Contents |
| --- | --- |
| `lab-01/` | Environment setup, introductory code and Lab 1 submission evidence |
| `lab-02/` | Project requirements, design, code and Lab 2 submission evidence |
| `lab-03/` | Placeholder for the later Google Colab notebook and submission link |

The project idea is a classroom cheating detection assistant. Suspicious activity would be flagged for a teacher to review; a flag alone would not establish cheating.

## Lab 01 deliverables

- [Setup script and folder tree](lab-01/setup_structure.py)
- [Pinned environment](requirements.txt)
- [Executed notebook](notebooks/lab01_setup.ipynb) and [rendered HTML](lab-01/lab01_setup.html)
- [Git and environment evidence](lab-01/evidence/)
- [Task-wise Word submission](lab-01/Lab01_Deliverables.docx)

## Lab 02 deliverables

- [Task 1 smart attendance requirements](lab-02/requirements.md)
- [Task 2 surveillance boundary sheet](lab-02/boundary_specification.md)
- [Task 3 DFD images and Mermaid sources](lab-02/diagrams/)
- [Task 4 Python module interfaces](lab-02/interfaces.py)
- [Task 5 unified ARCHITECTURE.md](ARCHITECTURE.md)
- [Task-wise Word submission](lab-02/Lab02_Deliverables.docx)

Performance and accuracy values in Lab 2 are design targets. Lab 1 checks imports and small CPU operations; it does not train a cheating detector.

## Open the Lab 1 notebook

The local environment is named `aipdd_env` and is excluded from Git. To reproduce it on Python 3.12:

```powershell
python -m venv aipdd_env
. .\aipdd_env\Scripts\Activate.ps1
python -m pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt
python -m ipykernel install --user --name aipdd_env --display-name "Python (aipdd_env)"
python -m jupyter notebook notebooks/lab01_setup.ipynb
```

Select **Python (aipdd_env)** in Jupyter. The pinned file records the Windows Python 3.12 environment, including transitive dependencies. CPU wheels are obtained through the PyTorch CPU index.

## Submission

Repository: https://github.com/Hassnoo999/AI-Project-Design-Development

Lab 3 will be completed separately in Google Colab.
