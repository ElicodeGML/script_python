# README

Ce dépôt contient plusieurs scripts et notebooks Python personnels.

But: Réorganisation proposée (branche: reorganize/tree-v1)

Nouvelle arborescence créée dans cette branche :

- notebooks/                 # Tous les Jupyter Notebooks (.ipynb), renommés pour être lisibles
- projects/deep_learning/     # Projet "1 mois pour le deep learning" (scripts et données spécifiques)
- scripts/                    # Scripts indépendants, jeux, exemples
- src/                        # Modules Python réutilisables (package)
- legacy/                     # Copie des fichiers originaux (aucune suppression)

Que j'ai ajouté sur la branche :
- README.md (ce fichier)
- notebooks/README.md
- projects/deep_learning/README.md
- src/__init__.py
- scripts/reorganize_repo.py  (script pour effectuer la réorganisation automatiquement)
- .gitignore (mise à jour recommandée)

Comment utiliser
1) Clone le dépôt et positionne-toi sur la branche reorganize/tree-v1 :
   git fetch origin
   git checkout reorganize/tree-v1

2) Installe les dépendances pour le script de réorganisation :
   pip install nbformat

3) Lance le script à la racine du dépôt :
   python3 scripts/reorganize_repo.py

Le script va :
- créer les nouveaux dossiers
- copier tous les fichiers originaux dans legacy/
- déplacer et renommer les notebooks et scripts vers la nouvelle arborescence
- supprimer les sorties des notebooks (strip outputs)
- ajouter et committer les changements locaux (le script tente de faire un commit sur la branche locale)

Remarques
- Le script n'efface rien définitivement : tous les originaux sont sauvegardés dans legacy/.
- Après vérification locale, pousse la branche et ouvre une PR depuis reorganize/tree-v1 vers ta branche principale.
