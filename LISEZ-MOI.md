# Landing page WAYRE

Fichiers : `index.html`, dossier `images/`, `robots.txt`.

## Avant la mise en ligne
1. Remplacer le texte de « Mentions légales » et « Politique de confidentialité » en bas de page (éditeur, adresse, immatriculation, hébergeur ; responsable du traitement, durée de conservation, droits).
2. Une fois le nom de domaine connu, ajouter dans `<head>` :
   `<link rel="canonical" href="https://TON-DOMAINE/">` et `<meta property="og:image" content="https://TON-DOMAINE/images/logo-wayre.png">`
3. Créer un `sitemap.xml` (adresse de la page) et le déclarer dans Google Search Console.
4. Ajouter un bandeau de consentement aux cookies avant d'installer un outil de mesure ou des publicités.
5. Formulaire : par défaut il ouvre un email pré-rempli. Pour l'envoyer vers n8n, renseigner l'attribut `data-endpoint` de la balise `<form id="form">` avec l'adresse du webhook.
