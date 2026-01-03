# Guide de Compilation du Rapport LaTeX

## Prérequis

Pour compiler le rapport LaTeX, vous devez avoir installé :

1. **LaTeX Distribution** :
   - Sur Linux : `texlive-full` ou `texlive-latex-extra`
   - Sur Windows : MiKTeX ou TeX Live
   - Sur macOS : MacTeX

2. **Packages nécessaires** :
   - `babel` (support français)
   - `geometry` (mise en page)
   - `graphicx` (images)
   - `hyperref` (liens hypertexte)
   - `listings` (code source)
   - `xcolor` (couleurs)
   - `amsmath` (mathématiques)
   - `fancyhdr` (en-têtes/pieds de page)
   - `titlesec` (formatage des titres)
   - `enumitem` (listes)
   - `booktabs` (tableaux)
   - `array` (tableaux avancés)
   - `longtable` (tableaux longs)

## Compilation

### Méthode 1 : Compilation directe avec pdflatex

```bash
pdflatex RAPPORT_PROJET.tex
pdflatex RAPPORT_PROJET.tex  # Deuxième passe pour les références
```

### Méthode 2 : Utilisation de make

Créez un fichier `Makefile` :

```makefile
all: RAPPORT_PROJET.pdf

RAPPORT_PROJET.pdf: RAPPORT_PROJET.tex
	pdflatex RAPPORT_PROJET.tex
	pdflatex RAPPORT_PROJET.tex
	rm -f *.aux *.log *.out *.toc

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
```

Puis exécutez :
```bash
make
```

### Méthode 3 : Avec un IDE LaTeX

Utilisez un éditeur LaTeX comme :
- **TeXstudio** (recommandé)
- **TeXmaker**
- **Overleaf** (en ligne)
- **VS Code** avec l'extension LaTeX Workshop

## Structure du Document

Le rapport contient :

1. **Page de titre** avec informations du projet
2. **Table des matières** automatique
3. **Introduction** : Contexte, objectifs, technologies
4. **Architecture** : Structure, modèles de données
5. **Fonctionnalités** : Toutes les fonctionnalités détaillées
6. **Interface Utilisateur** : Vues, thèmes, design
7. **Améliorations Techniques** : Performance, sécurité
8. **Notifications** : Système de retours utilisateur
9. **Code Source** : Exemples de code
10. **Conclusion** : Résultats et perspectives
11. **Annexes** : Structure, statistiques, références

## Personnalisation

Pour personnaliser le rapport :

1. **Modifier les informations** dans la section `\author{}`
2. **Ajouter des images** avec `\includegraphics{chemin/image.png}`
3. **Modifier les couleurs** dans les définitions `\definecolor`
4. **Ajuster la mise en page** dans `\geometry{}`

## Résolution de Problèmes

### Erreur "Package not found"
Installez le package manquant :
```bash
# Sur Linux avec texlive
sudo apt-get install texlive-lang-french texlive-latex-extra

# Sur Windows/MacTeX
tlmgr install <nom-du-package>
```

### Erreur de compilation
- Vérifiez que tous les packages sont installés
- Assurez-vous d'avoir compilé deux fois (pour les références)
- Vérifiez les chemins des fichiers inclus

### Caractères spéciaux
Le document utilise `utf8` encoding, assurez-vous que votre éditeur l'utilise aussi.

## Résultat

Le fichier `RAPPORT_PROJET.pdf` sera généré dans le même répertoire que le fichier `.tex`.

