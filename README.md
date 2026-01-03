# TP – Gestion des Notes Internes (Dark Theme)
Ce module Odoo offre une solution complète pour la création, l'organisation et le suivi de notes internes, avec une interface utilisateur améliorée incluant un mode sombre.
## 📋 Fonctionnalités Principales
### 📝 Gestion Avancée des Notes
- **Cycle de vie** : Gestion des états (Brouillon, Publié, Archivé).
- **Priorisation** : Système de priorité à 4 niveaux avec indicateurs visuels :
  - Basse
  - Normale
  - Haute (⚡)
  - Urgente (🔥)
- **Organisation** : Tri par date de création, date de note, ou priorité.
- **Favoris** : Marquage rapide des notes importantes.
### 📅 Suivi Temporel
- **Échéances** : Définition de dates limites pour chaque note.
- **Alertes de retard** : Détection automatique des notes dont la date d'échéance est dépassée.
- **Validation** : Contrôles de cohérence sur les dates (anti-datage interdit).
### 🎨 Expérience Utilisateur
- **Thème Sombre** : Support natif d'un mode sombre (Dark Mode) pour réduire la fatigue visuelle.
- **Personnalisation** : Choix de couleurs de thème pour les notes (Bleu, Vert, Rouge, Violet).
- **Tableau de Bord** : Statistiques en temps réel (Total, Brouillons, Publiés, Archivés, Urgences, Retards).
### 💬 Collaboration
- Intégration complète du **Chatter Odoo** (historique des modifications, envoi de messages, activités planifiées).
- Notifications améliorées pour les actions principales (Publication, Archivage, Suppression).
## 🛠 Installation
1. Placez le dossier `tp_gestion_notes` dans votre répertoire `addons` Odoo.
2. Redémarrez votre service Odoo.
3. Activez le mode développeur.
4. Mettez à jour la liste des applications.
5. Recherchez "TP – Gestion des Notes Internes" et cliquez sur **Installer**.
## ⚙️ Dépendances technique
Ce module dépend des modules standard :
- `base`
- `web`
- `mail`
---
*Développé dans le cadre du module ERP/Odoo - 5IIR*
