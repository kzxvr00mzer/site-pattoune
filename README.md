# Site Pattoune chez soi

Site statique de [pattoune-chez-soi.fr](https://pattoune-chez-soi.fr/), pet sitter à domicile à Pau.

- La racine du dépôt est le site en ligne : OVHcloud le déploie automatiquement à chaque push sur `main` (intégration Git de l'hébergement web).
- `sources/gen.py` régénère les pages HTML (`python3 sources/gen.py .`), `sources/LISEZMOI.md` explique l'organisation des fichiers.
- `sources/` et `.git` ne sont pas accessibles en ligne (règles dans `.htaccess`).
