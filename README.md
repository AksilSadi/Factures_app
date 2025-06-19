# 🎬 Plateforme Web de Films & Séries – Projet PC3R

Ce projet est une application web complète permettant de consulter, noter, commenter et filtrer des films et séries grâce à une interface intuitive. Elle repose sur trois parties distinctes :

- Un **Backend** en Go
- Un **CMS Strapi** connecté à une base PostgreSQL
- Un **Frontend** développé en React avec Vite

---

## 📂 Repositories

- 🔙 **Backend (Go)**  
  [https://github.com/MassinS/backend-tmdb/tree/main](https://github.com/MassinS/backend-tmdb/tree/main)

- 📦 **CMS (Strapi)**  
  [https://github.com/MassinS/TMDB-DATABASE-STRAPI](https://github.com/MassinS/TMDB-DATABASE-STRAPI)

- 🎨 **Frontend (React + Vite)**  
  [https://github.com/MassinS/frontend_pc3r](https://github.com/MassinS/frontend_pc3r)

---

## ⚙️ Architecture générale

- **Frontend (React + Vite)** :  
  Affichage dynamique, filtres, notation, commentaire, recherche de films et séries.

- **Backend (Go)** :  
communication avec Strapi.

- **Strapi (CMS)** :  
  Sert de base de données pour stocker les utilisateurs, notes, commentaires, films likés, etc.

---

## 🚀 Déploiement

Les trois services sont déployés sur [Render](https://render.com) :

- **Backend** : Build à partir du `Dockerfile`, relié à GitHub
- **Strapi** : Connecté à une base PostgreSQL provisionnée via Render, lancé automatiquement
- **Frontend** : Service de site statique généré par Vite (`npm run build`, dossier `dist`)

---