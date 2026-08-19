# Script pour réorganiser l'arborescence du dépôt
# Usage:
#   pip install nbformat
#   python3 scripts/reorganize_repo.py

import os
import re
import shutil
import unicodedata
import nbformat
from nbformat import NotebookNode
import subprocess

ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Mappage des dossiers sources -> destinations
MAPPINGS = [
    ("notebook", "notebooks"),
    ("projet 1 mois pour le 'deep leaning'", os.path.join("projects", "deep_learning")),
    ("scripts_", "scripts"),
]

# Fichiers à traiter en priorité pour src
SRC_CANDIDATES = [
    os.path.join("notebook", "student.py"),
    os.path.join("scripts_", "class_python.py"),
]

VALID_EXT = {'.ipynb', '.py', '.md', '.txt'}


def normalize_name(name: str) -> str:
    # lowercase, replace spaces by underscores, remove accents and special chars
    name = name.strip()
    name = name.replace(' ', '_')
    name = name.lower()
    name = unicodedata.normalize('NFKD', name)
    name = name.encode('ascii', 'ignore').decode('ascii')
    # replace characters not alnum, underscore, dot or dash by underscore
    name = re.sub(r'[^a-z0-9_\.-]', '_', name)
    # collapse multiple underscores
    name = re.sub(r'_+', '_', name)
    return name


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def strip_notebook_outputs(src_path, dst_path):
    try:
        nb = nbformat.read(src_path, as_version=4)
        for cell in nb.get('cells', []):
            if cell.get('outputs') is not None:
                cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None
        nbformat.write(nb, dst_path)
    except Exception as e:
        print(f"Warning: impossible de traiter le notebook {src_path}: {e}")
        shutil.copy2(src_path, dst_path)


def copy_to_legacy(original_path, repo_root):
    rel = os.path.relpath(original_path, repo_root)
    dest = os.path.join(repo_root, 'legacy', rel)
    ensure_dir(os.path.dirname(dest))
    shutil.copy2(original_path, dest)
    return dest


def git_commit(message):
    try:
        subprocess.run(['git', 'add', '.'], cwd=ROOT, check=True)
        subprocess.run(['git', 'commit', '-m', message], cwd=ROOT, check=True)
        print('Commit created locally.')
    except subprocess.CalledProcessError as e:
        print('Git commit failed (peut-être aucun changement à committer):', e)


def main():
    print('Réorganisation démarrée...')
    ensure_dir(os.path.join(ROOT, 'legacy'))

    # 1) Traiter mappings
    for src_dir, dst_dir in MAPPINGS:
        abs_src = os.path.join(ROOT, src_dir)
        abs_dst = os.path.join(ROOT, dst_dir)
        if not os.path.exists(abs_src):
            continue
        print(f'Traitement de {abs_src} -> {abs_dst}')
        for root, dirs, files in os.walk(abs_src):
            rel_root = os.path.relpath(root, abs_src)
            for f in files:
                ext = os.path.splitext(f)[1]
                if ext.lower() not in VALID_EXT:
                    # copy non-valid files to legacy only
                    src_path = os.path.join(root, f)
                    copy_to_legacy(src_path, ROOT)
                    continue
                new_name = normalize_name(f)
                subpath = rel_root if rel_root != '.' else ''
                dst_subdir = os.path.join(abs_dst, subpath)
                ensure_dir(dst_subdir)
                src_path = os.path.join(root, f)
                dst_path = os.path.join(dst_subdir, new_name)
                # copy original to legacy
                copy_to_legacy(src_path, ROOT)
                # if notebook -> strip outputs
                if ext.lower() == '.ipynb':
                    strip_notebook_outputs(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                print(f'  -> {dst_path}')

    # 2) Déplacer fichiers candidats vers src/
    ensure_dir(os.path.join(ROOT, 'src'))
    for candidate in SRC_CANDIDATES:
        abs_candidate = os.path.join(ROOT, candidate)
        if os.path.exists(abs_candidate):
            new_name = normalize_name(os.path.basename(candidate))
            dst_path = os.path.join(ROOT, 'src', new_name)
            copy_to_legacy(abs_candidate, ROOT)
            shutil.copy2(abs_candidate, dst_path)
            print(f'Copié vers src/: {dst_path}')

    # 3) Nettoyage des noms dans la racine (ex: README_Version3.md -> README.md)
    readme_old = os.path.join(ROOT, 'README_Version3.md')
    if os.path.exists(readme_old):
        copy_to_legacy(readme_old, ROOT)
        dst_readme = os.path.join(ROOT, 'README.md')
        shutil.copy2(readme_old, dst_readme)
        print('README_Version3.md copié vers README.md')

    # 4) Créer fichier __init__ déjà ajouté par le commit (si non)
    ensure_dir(os.path.join(ROOT, 'src'))

    # 5) Commit local
    git_commit('Reorganize tree: create notebooks/, projects/, scripts/, src/ and copy originals to legacy/')
    print('Réorganisation terminée. Vérifie les changements localement, puis pousse la branche si tout est OK.')

if __name__ == '__main__':
    main()
