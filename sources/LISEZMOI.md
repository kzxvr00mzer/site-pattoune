# Site Pattoune chez soi

Site statique (HTML/CSS/JS, sans WordPress ni dépendance). Il suffit de déposer **tout le contenu de ce dossier** à la racine de l'hébergement de pattoune-chez-soi.fr.

## Pages
- `index.html` : tout le site sur une page (accueil, pourquoi moi, Alicia, formules chien et chat, famille nombreuse, réservation, zone, FAQ, contact) · `mentions-legales.html` · `404.html`
- SEO : `sitemap.xml`, `robots.txt`, données structurées LocalBusiness / Service / FAQPage / BreadcrumbList dans chaque page.

## À compléter avant la mise en ligne
1. `mentions-legales.html` : nom de famille d'Alicia et adresse (l'hébergeur OVH est déjà renseigné).
2. Photos : la photo d'Alicia (`assets/img/alicia-pet-sitter-pau.jpg`) vient d'une capture d'écran en 320 px ; la remplacer par l'original en meilleure qualité si possible.
3. Redirections : l'ancien site WordPress n'avait qu'une page, donc pas de redirection d'URL nécessaire. Configurer `404.html` comme page d'erreur chez l'hébergeur.
4. Après la mise en ligne : soumettre `https://pattoune-chez-soi.fr/sitemap.xml` dans Google Search Console.

## Modifier le site
Les pages sont générées par `gen.py` (textes, tarifs, communes au même endroit) : `python3 gen.py .` régénère les pages HTML. On peut aussi modifier les fichiers HTML directement.

## Mise en ligne sur OVH (hébergement web)
1. **Sauvegarder l'ancien site** : dans l'espace client OVH > Hébergements > votre hébergement, faire une sauvegarde (onglet FTP-SSH > « Restaurer une sauvegarde » ou télécharger le dossier `www` en FTP) et exporter la base de données WordPress (onglet Bases de données > Créer une sauvegarde).
2. **Se connecter en FTP** avec FileZilla (identifiants dans l'onglet FTP-SSH, serveur `ftp.clusterXXX.hosting.ovh.net`, port 21).
3. Dans le dossier `www`, **déplacer l'ancien WordPress** dans un sous-dossier `ancien-site` (ou le supprimer une fois la sauvegarde vérifiée).
4. **Envoyer tout le contenu** de ce dossier dans `www` (y compris le fichier caché `.htaccess` ; dans FileZilla : Serveur > Forcer l'affichage des fichiers cachés). `gen.py`, `LISEZMOI.md` et `apercu.html` peuvent rester en local.
5. Vérifier que le **certificat SSL** (Let's Encrypt, gratuit) est actif dans l'onglet Multisite, puis ouvrir https://pattoune-chez-soi.fr.

## Galerie « Les Pattounes gardées »
Les 157 photos de `assets/img/pattounes/` ont été découpées depuis des captures du compte Instagram (environ 280 × 370 px).
Pour des images plus nettes, remplacez-les par les originaux en gardant les mêmes noms de fichiers.
La liste et l’ordre des photos sont dans `gen.py` (variable `GALLERY`, les 18 premières sont visibles d’emblée).
