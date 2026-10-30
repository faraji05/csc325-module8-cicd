# CSC325 Module 8: First CI/CD Pipeline

A small Django REST Framework backend and GitHub Actions workflow for the
Module 8 assignment.

## Requirements and local setup

- Python 3.12

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

The public health endpoint is `GET /api/health/`.

## CI/CD workflow

`.github/workflows/csc325_ci_cd.yml` runs for pushes to `main` and pull
requests targeting `main`. Its ordered jobs are Setup, Dependencies, Test, and
Deploy. Deploy depends on Test, so it only starts when the full test suite
passes. Deploy currently prints a placeholder; it does not host a live app.

To keep `main` protected while recording the feature push, create a pull
request from the feature branch to `main`. The pull request triggers the
workflow; merging it later also triggers the `main` push workflow. Configure
a GitHub ruleset targeting `main` with **Require a pull request before
merging** enabled.
