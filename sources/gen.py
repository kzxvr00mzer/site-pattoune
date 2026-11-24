#!/usr/bin/env python3
"""Génère les pages statiques du site Pattoune chez soi."""
import json, os, sys
OUT = sys.argv[1]
SITE = "https://pattoune-chez-soi.fr"
TEL = "06 26 32 31 67"; TEL_LINK = "+33626323167"
MAIL = "pattounechezsoi@gmail.com"
FB = "https://www.facebook.com/profile.php?id=100086993795203"
IG = "https://www.instagram.com/pattoune_chez_soi/"
GOOGLE_AVIS = "https://www.google.com/search?q=Pattoune+chez+soi+Pau+avis"

# Communes à 12 km maximum de Pau (distances indicatives, à vol d'oiseau)
TOWNS = ["Pau", "Billère", "Lons", "Lescar", "Jurançon", "Gelos", "Mazères-Lezons", "Bizanos",
         "Idron", "Aressy", "Uzos", "Rontignon", "Narcastet", "Meillon", "Assat", "Ousse", "Lée",
         "Sendets", "Buros", "Montardon", "Serres-Castet", "Morlaàs", "Gan", "Laroin",
         "Artiguelouve", "Poey-de-Lescar", "Saint-Faust", "Bosdarros"]
TOWNS_TXT = ", ".join(TOWNS[1:-1]) + " et " + TOWNS[-1]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="paw" viewBox="0 0 24 24"><ellipse cx="6" cy="9" rx="2.3" ry="3"/><ellipse cx="10.3" cy="5.2" rx="2.3" ry="3"/><ellipse cx="15.2" cy="5.4" rx="2.3" ry="3"/><ellipse cx="19" cy="9.6" rx="2.2" ry="2.8"/><path d="M12.5 11c-3 0-6.5 4.2-6.5 7 0 2 1.6 3 3.4 3 1.4 0 2.1-.7 3.1-.7s1.8.7 3.2.7c1.8 0 3.3-1 3.3-3 0-2.8-3.5-7-6.5-7z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/></symbol>
<symbol id="i-sms" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></symbol>
<symbol id="i-camera" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></symbol>
<symbol id="i-sliders" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24" fill="currentColor"><path d="M14 8V6.5c0-.8.2-1.3 1.4-1.3H17V2.2C16.7 2.1 15.7 2 14.6 2 12.2 2 10.6 3.4 10.6 6.1V8H8v3.4h2.6V22H14V11.4h2.7L17 8z"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor"/></symbol>
<symbol id="i-dog" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 22c-6-2-10 4-8 12 1 4 4 4 6 2"/><path d="M44 22c6-2 10 4 8 12-1 4-4 4-6 2"/><path d="M18 26c0-9 6-14 14-14s14 5 14 14v10c0 9-6 16-14 16s-14-7-14-16z"/><circle cx="26" cy="31" r="1.6" fill="currentColor"/><circle cx="38" cy="31" r="1.6" fill="currentColor"/><path d="M29 40h6l-3 3z" fill="currentColor"/><path d="M32 43v3"/></symbol>
<symbol id="i-cat" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 10l8 12h20l8-12 2 22c0 12-9 20-20 20S12 44 12 32z"/><circle cx="25" cy="33" r="1.6" fill="currentColor"/><circle cx="39" cy="33" r="1.6" fill="currentColor"/><path d="M30 40h4l-2 2z" fill="currentColor"/><path d="M8 38l10 1M8 44l10-2M56 38l-10 1M56 44l-10-2"/></symbol>
<symbol id="i-bunny" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M24 26C20 14 20 4 25 4s6 12 5 22"/><path d="M40 26c4-12 4-22-1-22s-6 12-5 22"/><circle cx="32" cy="40" r="16"/><circle cx="26" cy="38" r="1.6" fill="currentColor"/><circle cx="38" cy="38" r="1.6" fill="currentColor"/><path d="M30 45h4l-2 2z" fill="currentColor"/></symbol>
</svg>"""

def icon(name, cls=""):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#{name}"/></svg>'

LOGO_MARK = '''<img class="logo-mark" src="assets/img/logo-maison.png" width="125" height="138" alt="">'''


ICONS = ICONS[:ICONS.rindex("</svg>")] + """<symbol id="i-cap" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 9 12 4 2 9l10 5 10-5z"/><path d="M6 11v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/><path d="M22 9v6"/></symbol>
<symbol id="i-mobile" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></symbol>
<symbol id="i-smile" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></symbol>
</svg>"""

# Menu : ancres de la page unique
NAV = [("#pourquoi", "Pourquoi moi"), ("#chien", "Garde de chien"), ("#chat", "Garde de chat"),
       ("#zone", "Zone"), ("#faq", "FAQ")]

ARROW = icon("i-arrow")

def header(current):
    base = "" if current == "index.html" else "index.html"
    items = "".join(f'<li><a href="{base}{h}">{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<div class="progress" aria-hidden="true"></div>
<header class="header">
 <div class="wrap">
  <a class="logo" href="{base or '#accueil'}" aria-label="Pattoune chez soi, retour en haut">{LOGO_MARK}<span>Pattoune chez soi<small>Pet sitter · Pau</small></span></a>
  <button class="burger" aria-expanded="false" aria-controls="nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
  <nav class="nav" id="nav" aria-label="Navigation principale">
   <ul>{items}<li><a class="btn btn--sm" href="{base}#contact">Réserver {ARROW}</a></li></ul>
  </nav>
 </div>
</header>'''

FOOTER = f'''<footer class="footer">
 <div class="wrap">
  <div class="footer-grid">
   <div>
    <a class="footer-logo" href="index.html"><img src="assets/img/logo-pattoune.png" width="125" height="163" alt="Logo Pattoune chez soi" loading="lazy"></a>
    <p class="small">Garde de chiens et de chats à votre domicile, visites et promenades à Pau et dans un rayon de 12 km. Pour des Pattounes heureuses !</p>
    <div class="socials"><a href="{FB}" rel="noopener" target="_blank" aria-label="Facebook de Pattoune chez soi">{icon("i-fb")}</a><a href="{IG}" rel="noopener" target="_blank" aria-label="Instagram de Pattoune chez soi">{icon("i-ig")}</a></div>
   </div>
   <div><h2>Services</h2><ul><li><a href="index.html#chien">Garde de chien à Pau</a></li><li><a href="index.html#chat">Garde de chat à Pau</a></li><li><a href="index.html#chien-carte">Promenade de chien</a></li><li><a href="index.html#nac">Rongeurs, oiseaux, poissons</a></li></ul></div>
   <div><h2>Infos</h2><ul><li><a href="index.html#zone">Communes desservies</a></li><li><a href="index.html#faq">Questions fréquentes</a></li><li><a href="index.html#reservation">Réservation</a></li><li><a href="mentions-legales.html">Mentions légales</a></li></ul></div>
   <div><h2>Contact</h2><ul><li><a href="sms:{TEL_LINK}">SMS : {TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>Pau (64000) et alentours</li><li>Réponse de 9h à 20h</li></ul></div>
  </div>
  <div class="footer-bottom"><span>© Pattoune chez soi · SIRET 920 022 464 00019 · Réalisé par Kevin Ly</span><span>Pet sitting à domicile à Pau, Billère, Lons, Lescar, Jurançon et alentours</span></div>
 </div>
</footer>
<a class="call-fab" href="sms:{TEL_LINK}" aria-label="Envoyer un SMS à Alicia au {TEL}">{icon("i-sms")}</a>'''

BUSINESS = {
    "@type": "LocalBusiness",
    "@id": SITE + "/#business",
    "name": "Pattoune chez soi",
    "alternateName": "Pattoune chez soi - Pet sitter Pau",
    "description": "Pet sitter à Pau : garde de chiens et de chats au domicile du propriétaire, visites et promenades à Pau et dans un rayon de 12 km.",
    "url": SITE + "/",
    "logo": SITE + "/assets/img/logo-pattoune.png",
    "image": SITE + "/assets/img/og-pattoune.jpg",
    "telephone": TEL_LINK,
    "email": MAIL,
    "priceRange": "10 € - 72 € / jour",
    "currenciesAccepted": "EUR",
    "paymentAccepted": "Chèque, Virement, Espèces, PayPal",
    "founder": {"@type": "Person", "name": "Alicia", "jobTitle": "Pet sitter"},
    "address": {"@type": "PostalAddress", "addressLocality": "Pau", "postalCode": "64000",
                "addressRegion": "Nouvelle-Aquitaine", "addressCountry": "FR"},
    "geo": {"@type": "GeoCoordinates", "latitude": 43.2951, "longitude": -0.3708},
    "areaServed": [{"@type": "GeoCircle",
                    "geoMidpoint": {"@type": "GeoCoordinates", "latitude": 43.2951, "longitude": -0.3708},
                    "geoRadius": "12000"}] + [{"@type": "City", "name": t} for t in TOWNS],
    "knowsAbout": ["Garde de chien à domicile", "Garde de chat à domicile", "Promenade de chien", "Pet sitting"],
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "ACACED (Attestation de connaissances pour les animaux de compagnie d'espèces domestiques)"},
        {"@type": "EducationalOccupationalCredential", "name": "Certificat professionnel des métiers animaliers, spécialité éducation et élevage"},
        {"@type": "EducationalOccupationalCredential", "name": "Formation aux premiers secours animaliers"}],
    "sameAs": [FB, IG],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Formules de garde", "itemListElement": [
        {"@type": "Offer", "name": n, "price": str(p), "priceCurrency": "EUR",
         "itemOffered": {"@type": "Service", "name": n, "serviceType": s, "areaServed": "Pau"}}
        for n, p, s in [("Chien tranquille", 26, "Garde de chien à domicile"),
                        ("Chien baladeur", 34, "Garde de chien à domicile"),
                        ("Chien sportif", 38, "Garde de chien à domicile"),
                        ("Chat d'intérieur sociable", 22, "Garde de chat à domicile"),
                        ("Chat d'intérieur solitaire", 12, "Garde de chat à domicile"),
                        ("Chat d'extérieur", 10, "Garde de chat à domicile")]]},
}

def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + (u if u != "index.html" else "")}
        for i, (n, u) in enumerate(items)]}

def crumbs_html(items):
    lis = "".join(f'<li><a href="{u}">{n}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{n}</li>'
                  for i, (n, u) in enumerate(items))
    return f'<nav class="crumbs" aria-label="Fil d’Ariane"><ol>{lis}</ol></nav>'

def page(fname, title, desc, body, graph=None, robots="index, follow"):
    canonical = SITE + "/" + ("" if fname == "index.html" else fname)
    ld = ""
    if graph:
        ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + "</script>"
    html = f'''<!doctype html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="geo.region" content="FR-64">
<meta name="geo.placename" content="Pau">
<meta name="geo.position" content="43.2951;-0.3708">
<meta name="ICBM" content="43.2951, -0.3708">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Pattoune chez soi">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-pattoune.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#414343">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/fraunces-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/nunito-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
{ld}
</head>
<body>
{ICONS}
{header(fname)}
<main id="contenu">
{body}
</main>
{FOOTER}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)

WAVE_DOWN = lambda c: f'<svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path fill="{c}" d="M0 40c240 40 480 40 720 10S1200-10 1440 30V80H0z"/></svg>'

CTA = f'''<section class="section"><div class="wrap">
 <div class="cta reveal reveal--zoom">
  <svg class="deco" style="width:260px;right:-40px;top:-50px;transform:rotate(20deg)" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="#paw"/></svg>
  <div><h2>Vous partez bientôt ?</h2><p>Racontez-moi votre animal et vos dates : je vous réponds rapidement avec la formule adaptée. Première rencontre gratuite dans un rayon de 4 km autour de Pau.</p></div>
  <div class="cta-actions"><a class="phone-big" href="sms:{TEL_LINK}">{TEL}</a><a class="btn btn--light" href="contact.html">Demander une garde {ARROW}</a></div>
 </div>
</div></section>'''

HERO_ILLUS = '''<svg class="hero-illus" viewBox="0 0 400 400" role="img" aria-label="Illustration d’un sacré de Birmanie et d’un shiba inu noir et feu assis côte à côte, heureux à la maison">
 <defs>
  <radialGradient id="bir-body" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#FFFBF3"/><stop offset="1" stop-color="#EADBC3"/></radialGradient>
  <radialGradient id="bir-mask" cx="50%" cy="56%" r="54%"><stop offset="0" stop-color="#2A1D17"/><stop offset=".42" stop-color="#3F2C23" stop-opacity=".96"/><stop offset=".74" stop-color="#7E6050" stop-opacity=".5"/><stop offset="1" stop-color="#C9AE92" stop-opacity="0"/></radialGradient>
  <linearGradient id="bir-leg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3E8D6"/><stop offset=".45" stop-color="#C9A486"/><stop offset="1" stop-color="#A27E63"/></linearGradient>
  <linearGradient id="bir-tail" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7A5A46"/><stop offset="1" stop-color="#3E2A20"/></linearGradient>
 </defs>
 <!-- sacré de Birmanie : crème, masque seal, yeux bleus, gants blancs -->
 <g transform="translate(36 110)">
  <g class="cat-tail"><path d="M96 244c34 10 66 8 76-14 5-11-1-21-9-21" fill="none" stroke="url(#bir-tail)" stroke-width="28" stroke-linecap="round"/>
  <path d="M120 252c20 2 38-2 44-14" fill="none" stroke="#8C6A55" stroke-width="5" stroke-linecap="round" opacity=".5"/></g>
  <ellipse cx="80" cy="188" rx="64" ry="64" fill="url(#bir-body)"/>
  <path d="M34 134q-4 26 12 38q0 12 12 15q6 11 22 9q16 2 22-9q12-3 12-15q16-12 12-38q-46 26-92 0z" fill="#FFF9F0"/>
  <rect x="44" y="194" width="26" height="54" rx="13" fill="url(#bir-leg)"/>
  <rect x="90" y="194" width="26" height="54" rx="13" fill="url(#bir-leg)"/>
  <rect x="44" y="232" width="26" height="16" rx="8" fill="#FFFFFF"/><rect x="90" y="232" width="26" height="16" rx="8" fill="#FFFFFF"/>
  <ellipse cx="57" cy="247" rx="17" ry="10" fill="#FFFFFF"/><ellipse cx="103" cy="247" rx="17" ry="10" fill="#FFFFFF"/>
  <path d="M51 247v6M57 247v7M63 247v6M97 247v6M103 247v7M109 247v6" stroke="#E2D9CC" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M30 82 22 20l46 30zM130 82l8-62-46 30z" fill="#3E2B22"/>
  <path d="M36 70l-5-36 22 18zM124 70l5-36-22 18z" fill="#B98C7E"/>
  <path d="M38 64l2-18M42 66l6-14M122 64l-2-18M118 66l-6-14" stroke="#F3E8D6" stroke-width="1.6" stroke-linecap="round"/>
  <circle cx="80" cy="96" r="53" fill="url(#bir-body)"/>
  <path d="M30 98l-12 6 10 3-9 8 13-1-4 10 16-9zM130 98l12 6-10 3 9 8-13-1 4 10-16-9z" fill="#F4EADA"/>
  <ellipse cx="80" cy="104" rx="45" ry="41" fill="url(#bir-mask)"/>
  <ellipse cx="80" cy="104" rx="13" ry="19" fill="#22170F" opacity=".45"/>
  <g class="blink">
   <circle cx="59" cy="93" r="12.5" fill="#8EC1EC" stroke="#1E140F" stroke-width="1.6"/><circle cx="101" cy="93" r="12.5" fill="#8EC1EC" stroke="#1E140F" stroke-width="1.6"/>
   <ellipse cx="60" cy="94.5" rx="6" ry="8.5" fill="#13202B"/><ellipse cx="102" cy="94.5" rx="6" ry="8.5" fill="#13202B"/>
   <circle cx="63.5" cy="89.5" r="3.4" fill="#fff"/><circle cx="105.5" cy="89.5" r="3.4" fill="#fff"/>
   <circle cx="57" cy="99" r="1.5" fill="#fff"/><circle cx="99" cy="99" r="1.5" fill="#fff"/>
  </g>
  <ellipse cx="45" cy="114" rx="8" ry="5" fill="#F4A3A8" opacity=".75"/><ellipse cx="115" cy="114" rx="8" ry="5" fill="#F4A3A8" opacity=".75"/>
  <path d="M74 111h12l-6 7z" fill="#1E140F"/>
  <path d="M74 122q6 9 12 0z" fill="#F08C96"/>
  <path d="M80 118q-3 7-10 4M80 118q3 7 10 4" fill="none" stroke="#1E140F" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M42 112l-28-6M42 119l-28 4M118 112l28-6M118 119l28 4" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" opacity=".85"/>
 </g>
 <!-- shiba inu noir et feu : masque crème, sourcils feu, harnais noir -->
 <g transform="translate(196 96)">
  <g class="tail"><path d="M116 212c30 0 50-22 44-48-5-20-30-24-36-8-4 10 4 18 12 15" fill="none" stroke="#1F1F23" stroke-width="20" stroke-linecap="round"/>
  <path d="M132 168c4-8 16-8 20 2" fill="none" stroke="#EFE6D8" stroke-width="5" stroke-linecap="round"/></g>
  <ellipse cx="80" cy="204" rx="66" ry="62" fill="#1F1F23"/>
  <path d="M44 150q36 22 72 0c14 40 10 80 2 108H42c-8-28-12-68 2-108z" fill="#F3ECE0"/>
  <rect x="42" y="202" width="28" height="60" rx="14" fill="#F3ECE0" stroke="#DCC7AA" stroke-width="1.5"/><rect x="90" y="202" width="28" height="60" rx="14" fill="#F3ECE0" stroke="#DCC7AA" stroke-width="1.5"/>
  <ellipse cx="55" cy="261" rx="18" ry="10" fill="#F3ECE0"/><ellipse cx="105" cy="261" rx="18" ry="10" fill="#F3ECE0"/>
  <path d="M38 174q42 28 84 0" fill="none" stroke="#121214" stroke-width="9" stroke-linecap="round"/>
  <path d="M80 188v30" stroke="#121214" stroke-width="7" stroke-linecap="round"/>
  <circle cx="52" cy="183" r="4.2" fill="none" stroke="#C9CED3" stroke-width="2.4"/><circle cx="108" cy="183" r="4.2" fill="none" stroke="#C9CED3" stroke-width="2.4"/><circle cx="80" cy="192" r="4.2" fill="none" stroke="#C9CED3" stroke-width="2.4"/>
  <path d="M28 80 36 14l42 36zM132 80l-8-66-42 36z" fill="#1F1F23"/>
  <path d="M38 66l3-38 24 22zM122 66l-3-38-24 22z" fill="#C88A52"/>
  <path d="M42 62l2-26 18 16zM118 62l-2-26-18 16z" fill="#EAD6BA"/>
  <ellipse cx="80" cy="102" rx="60" ry="54" fill="#1F1F23"/>
  <path d="M30 107c3 37 27 58 50 58s47-21 50-58c-11 6-27 1-33-9-5-6-27-6-32 0-6 10-22 15-35 9z" fill="#C0803F"/>
  <ellipse cx="60" cy="97" rx="11" ry="7" fill="#C0803F"/><ellipse cx="100" cy="97" rx="11" ry="7" fill="#C0803F"/>
  <path d="M34 112c4 32 24 50 46 50s42-18 46-50c-10 6-26 2-32-8-5-6-23-6-28 0-6 10-22 14-32 8z" fill="#F3ECE0"/>
  <ellipse cx="60" cy="76" rx="7.5" ry="4.5" fill="#D9A065"/><ellipse cx="100" cy="76" rx="7.5" ry="4.5" fill="#D9A065"/>
  <g class="blink">
   <ellipse cx="60" cy="95" rx="9.5" ry="10" fill="#120D0B"/><ellipse cx="100" cy="95" rx="9.5" ry="10" fill="#120D0B"/>
   <circle cx="63.5" cy="91" r="3.2" fill="#fff"/><circle cx="103.5" cy="91" r="3.2" fill="#fff"/>
   <circle cx="57.5" cy="99.5" r="1.4" fill="#fff"/><circle cx="97.5" cy="99.5" r="1.4" fill="#fff"/>
  </g>
  <ellipse cx="80" cy="120" rx="10.5" ry="7.5" fill="#120D0B"/>
  <ellipse cx="45" cy="128" rx="9" ry="5.5" fill="#F4A3A8" opacity=".7"/><ellipse cx="115" cy="128" rx="9" ry="5.5" fill="#F4A3A8" opacity=".7"/>
  <path d="M66 130q14 20 28 0q-14 5-28 0z" fill="#3B1E1E"/>
  <path d="M74 136q6 14 12 0q-6 2-12 0z" fill="#F08C8C"/>
  <path d="M80 127v4M64 129q16 6 32 0" fill="none" stroke="#120D0B" stroke-width="2.6" stroke-linecap="round"/>
 </g>
</svg>'''

def price_table(caption, rows, cols):
    head = "".join(f'<th scope="col">{c}</th>' for c in cols)
    body = "".join("<tr><th scope=\"row\">" + r[0] + "</th>" + "".join(f'<td class="num">{v}</td>' for v in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><caption>{caption}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

def zone_tabs(prefix, zones):
    tabs = "".join(f'<button class="tab" role="tab" id="{prefix}-t{i}" aria-controls="{prefix}-p{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{z[0]}</button>' for i, z in enumerate(zones))
    panels = "".join(f'<div role="tabpanel" id="{prefix}-p{i}" aria-labelledby="{prefix}-t{i}"{"" if i == 0 else " hidden"}>{z[1]}</div>' for i, z in enumerate(zones))
    return f'<div class="tabs-wrap"><div class="tabs" role="tablist" aria-label="Distance depuis Pau">{tabs}</div></div>{panels}'

cols3 = ["Durée de la visite", "1 visite/jour", "2 visites/jour", "3 visites/jour"]
dog_zones = [
    ("Jusqu’à 4 km", price_table("Garde de chien à la carte, jusqu’à 4 km de Pau. Pré-visite et remise des clés : offertes", [["30 min", "14 €", "26 €", "40 €"], ["1 h", "20 €", "38 €", "58 €"]], cols3)),
    ("4 à 8 km", price_table("Garde de chien à la carte, de 4 à 8 km de Pau. Pré-visite et remise des clés : 6 €", [["30 min", "20 €", "32 €", "46 €"], ["1 h", "26 €", "44 €", "64 €"]], cols3)),
    ("8 à 12 km", price_table("Garde de chien à la carte, de 8 à 12 km de Pau. Pré-visite et remise des clés : 9 €", [["30 min", "28 €", "40 €", "54 €"], ["1 h", "34 €", "52 €", "72 €"]], cols3)),
]
cat_cols = ["Durée de la visite", "1 visite/jour", "2 visites/jour", "3 visites/jour"]
cat_zones = [
    ("Jusqu’à 4 km", price_table("Garde de chat à la carte, jusqu’à 4 km de Pau. Pré-visite et remise des clés : offertes", [["20 min", "10 €", "18 €", "28 €"], ["30 min", "12 €", "22 €", "34 €"], ["1 h", "18 €", "34 €", "—"]], cat_cols)),
    ("4 à 8 km", price_table("Garde de chat à la carte, de 4 à 8 km de Pau. Pré-visite et remise des clés : 6 €", [["20 min", "16 €", "24 €", "34 €"], ["30 min", "18 €", "28 €", "40 €"], ["1 h", "24 €", "40 €", "—"]], cat_cols)),
    ("8 à 12 km", price_table("Garde de chat à la carte, de 8 à 12 km de Pau. Pré-visite et remise des clés : 9 €", [["20 min", "24 €", "32 €", "42 €"], ["30 min", "26 €", "36 €", "48 €"], ["1 h", "32 €", "48 €", "—"]], cat_cols)),
]
MAP = [("Billère", -3, .3), ("Lons", -4.2, 2.4), ("Lescar", -7.5, 1.5), ("Jurançon", -2.2, -2.6), ("Gelos", .4, -3.4),
       ("Bizanos", 3, -1.2), ("Idron", 5.2, -.4), ("Ousse", 8, -1.8), ("Buros", 5.5, 5), ("Montardon", -.5, 8),
       ("Morlaàs", 9.6, 6.8), ("Gan", -1.8, -8.6), ("Artiguelouve", -9.6, -2.2), ("Assat", 8.6, -6.6),
       ("Saint-Faust", -6.4, -8), ("Bosdarros", 1.4, -10.8), ("Poey-de-Lescar", -9.6, 4.6)]
map_html = "".join(f'<span class="town" style="left:{50 + e * 50 / 12:.1f}%;top:{50 - n * 50 / 12:.1f}%">{t}</span>' for t, e, n in MAP)

# =============================================================== PAGE UNIQUE
FAQ = [
    ("certifs", "Quelles sont vos certifications ?", "<ul><li>Certificat professionnel des métiers animaliers, spécialité éducation et élevage</li><li>Titulaire de l’ACACED</li><li>Formation aux premiers secours animaliers</li><li>Assurance responsabilité civile</li></ul>"),
    ("pourquoi-choisir", "Pourquoi choisir Pattoune chez soi plutôt qu’une pension ou une plateforme ?", "<p>Votre animal est gardé chez lui, par une professionnelle qualifiée et de confiance, avec un service adapté à ses besoins. Dans une pension il change de repères, et sur les plateformes de pet sitting les gardiens ne sont pas toujours qualifiés.</p>"),
    ("deplacement", "Jusqu’où vous déplacez-vous ?", "<p>À Pau et dans un rayon de 12 km. Le déplacement est offert pour la première visite seulement (rencontre et signature du contrat), jusqu’à 4 km de Pau ; au-delà, les tarifs à la carte « 4-8 km » et « 8-12 km » s’appliquent. <a href=\"#zone\">Voir les communes desservies</a>.</p>"),
    ("plusieurs", "Comment calculer le prix pour plusieurs animaux ?", "<p>Ajoutez simplement 4 € par chat supplémentaire et 8 € par chien supplémentaire.</p>"),
    ("prise-en-charge", "Les frais de garde peuvent-ils être pris en charge ?", "<p>Une prise en charge est possible dans certains cas, par exemple lors d’une hospitalisation. Renseignez-vous auprès de votre complémentaire santé.</p>"),
    ("paiement", "Quels moyens de paiement acceptez-vous ?", "<p>Chèque, virement, espèces et PayPal.</p>"),
    ("contact-faq", "Comment vous joindre ?", f"<p>Par e-mail à <a href=\"mailto:{MAIL}\">{MAIL}</a> ou par SMS écrit au <a href=\"sms:{TEL_LINK}\">{TEL}</a>, en formulant clairement votre demande. WhatsApp est possible si vous êtes à l’étranger.</p>"),
    ("nac", "Gardez-vous d’autres animaux que les chiens et les chats ?", "<p>Oui : rongeurs, oiseaux et poissons, sur devis. Je ne garde pas les reptiles, qui ne sont pas dans mes compétences.</p>"),
]
import re
faq_graph = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", a)).strip()}} for _, q, a in FAQ]}
faq_items = "".join(f'<details id="{i}"><summary>{q}</summary><div class="answer">{a}</div></details>' for i, q, a in FAQ)

BUSINESS["image"] = [SITE + "/assets/img/og-pattoune.jpg", SITE + "/assets/img/alicia-pet-sitter-pau.jpg"]
BUSINESS["founder"]["image"] = SITE + "/assets/img/alicia-pet-sitter-pau.jpg"
services = [
    {"@type": "Service", "name": "Garde de chien à domicile à Pau", "serviceType": "Garde de chien à domicile",
     "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "City", "name": "Pau"},
     "offers": [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "EUR"} for n, p in [("Chien tranquille", "26"), ("Chien baladeur", "34"), ("Chien sportif", "38")]]},
    {"@type": "Service", "name": "Garde de chat à domicile à Pau", "serviceType": "Garde de chat à domicile",
     "provider": {"@id": SITE + "/#business"}, "areaServed": {"@type": "City", "name": "Pau"},
     "offers": [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "EUR"} for n, p in [("Chat d'intérieur sociable", "22"), ("Chat d'intérieur solitaire", "12"), ("Chat d'extérieur", "10")]]},
]
graph = [BUSINESS, {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Pattoune chez soi",
                    "inLanguage": "fr-FR", "publisher": {"@id": SITE + "/#business"}}] + services + [faq_graph]

names = ["Oria", "Poopy", "Maya", "Bosti", "Snow", "Jessy", "Carlita", "Twist", "Piana", "Pompom & Gaspard",
         "Rockett", "Judy", "Malou", "Leeloo", "Taiga", "Romance", "Ralph", "Fenwick", "Scrap", "Zouzou",
         "Roxie", "Django", "Bidouille", "Pepper", "Mimine Rousse", "Gustave", "Rebelle", "Yuzu", "Tapioca"]
mq = "".join(f"<span>{n}</span>" for n in names)
mq2 = mq.replace("<span>", '<span aria-hidden="true">')


# Photos des Pattounes gardées (découpées depuis le compte Instagram, ordre = 18 premières visibles)
GALLERY = [["chien-garde-pau-01.webp", 278, 359, "chien"], ["chat-garde-pau-01.webp", 276, 366, "chat"], ["chien-garde-pau-02.webp", 278, 364, "chien"], ["chat-garde-pau-02.webp", 279, 369, "chat"], ["chien-garde-pau-03.webp", 279, 371, "chien"], ["chat-garde-pau-03.webp", 278, 366, "chat"], ["chien-garde-pau-04.webp", 277, 365, "chien"], ["chat-garde-pau-04.webp", 272, 372, "chat"], ["chiens-garde-pau-01.webp", 272, 371, "chiens"], ["chat-garde-pau-05.webp", 278, 362, "chat"], ["chien-garde-pau-05.webp", 279, 359, "chien"], ["chat-garde-pau-06.webp", 279, 366, "chat"], ["chiens-garde-pau-02.webp", 272, 366, "chiens"], ["chat-garde-pau-07.webp", 277, 355, "chat"], ["chien-garde-pau-06.webp", 274, 362, "chien"], ["chat-garde-pau-08.webp", 278, 363, "chat"], ["chien-garde-pau-07.webp", 275, 359, "chien"], ["lapin-garde-pau-01.webp", 269, 362, "lapin"], ["chien-garde-pau-08.webp", 273, 371, "chien"], ["chat-garde-pau-09.webp", 278, 368, "chat"], ["chat-garde-pau-10.webp", 272, 371, "chat"], ["chat-garde-pau-11.webp", 273, 365, "chat"], ["chat-garde-pau-12.webp", 278, 365, "chat"], ["chien-garde-pau-09.webp", 272, 365, "chien"], ["chat-garde-pau-13.webp", 271, 365, "chat"], ["chat-garde-pau-14.webp", 271, 364, "chat"], ["chat-garde-pau-15.webp", 277, 365, "chat"], ["chat-garde-pau-16.webp", 268, 362, "chat"], ["chat-garde-pau-17.webp", 271, 366, "chat"], ["chat-garde-pau-18.webp", 278, 366, "chat"], ["chat-garde-pau-19.webp", 279, 366, "chat"], ["chat-garde-pau-20.webp", 271, 371, "chat"], ["chat-garde-pau-21.webp", 278, 371, "chat"], ["chat-garde-pau-22.webp", 279, 371, "chat"], ["chat-garde-pau-23.webp", 278, 371, "chat"], ["chat-garde-pau-24.webp", 279, 371, "chat"], ["chat-garde-pau-25.webp", 271, 360, "chat"], ["chat-garde-pau-26.webp", 278, 360, "chat"], ["chat-garde-pau-27.webp", 279, 360, "chat"], ["chat-garde-pau-28.webp", 278, 360, "chat"], ["chat-garde-pau-29.webp", 279, 360, "chat"], ["chien-garde-pau-10.webp", 275, 369, "chien"], ["chat-garde-pau-30.webp", 278, 369, "chat"], ["chat-garde-pau-31.webp", 278, 369, "chat"], ["chat-garde-pau-32.webp", 271, 369, "chat"], ["chat-garde-pau-33.webp", 275, 371, "chat"], ["chat-garde-pau-34.webp", 278, 371, "chat"], ["chat-garde-pau-35.webp", 279, 371, "chat"], ["chat-garde-pau-36.webp", 278, 371, "chat"], ["chien-garde-pau-11.webp", 271, 371, "chien"], ["chien-garde-pau-12.webp", 278, 353, "chien"], ["chats-garde-pau-01.webp", 271, 359, "chats"], ["chat-garde-pau-37.webp", 268, 370, "chat"], ["chat-garde-pau-38.webp", 278, 370, "chat"], ["chat-garde-pau-39.webp", 279, 370, "chat"], ["chat-garde-pau-40.webp", 278, 370, "chat"], ["chien-garde-pau-13.webp", 249, 370, "chien"], ["chat-garde-pau-41.webp", 268, 371, "chat"], ["chat-garde-pau-42.webp", 278, 371, "chat"], ["chat-garde-pau-43.webp", 279, 371, "chat"], ["chat-garde-pau-44.webp", 278, 371, "chat"], ["chat-garde-pau-45.webp", 249, 371, "chat"], ["chat-garde-pau-46.webp", 268, 369, "chat"], ["chat-garde-pau-47.webp", 278, 369, "chat"], ["chat-garde-pau-48.webp", 279, 369, "chat"], ["chat-garde-pau-49.webp", 278, 369, "chat"], ["chien-garde-pau-14.webp", 249, 369, "chien"], ["chat-garde-pau-50.webp", 278, 366, "chat"], ["chat-garde-pau-51.webp", 279, 366, "chat"], ["chat-garde-pau-52.webp", 278, 366, "chat"], ["chat-garde-pau-53.webp", 277, 366, "chat"], ["chat-garde-pau-54.webp", 276, 371, "chat"], ["chat-garde-pau-55.webp", 278, 371, "chat"], ["chien-garde-pau-15.webp", 279, 371, "chien"], ["chat-garde-pau-56.webp", 278, 371, "chat"], ["chat-garde-pau-57.webp", 277, 371, "chat"], ["chat-garde-pau-58.webp", 276, 351, "chat"], ["chat-garde-pau-59.webp", 278, 347, "chat"], ["chat-garde-pau-60.webp", 279, 351, "chat"], ["chat-garde-pau-61.webp", 278, 351, "chat"], ["chat-garde-pau-62.webp", 277, 351, "chat"], ["chat-garde-pau-63.webp", 267, 369, "chat"], ["chat-garde-pau-64.webp", 278, 369, "chat"], ["chat-garde-pau-65.webp", 279, 369, "chat"], ["chat-garde-pau-66.webp", 278, 369, "chat"], ["chat-garde-pau-67.webp", 273, 369, "chat"], ["chat-garde-pau-68.webp", 267, 371, "chat"], ["chat-garde-pau-69.webp", 278, 371, "chat"], ["chat-garde-pau-70.webp", 279, 371, "chat"], ["chat-garde-pau-71.webp", 278, 371, "chat"], ["chien-garde-pau-16.webp", 273, 371, "chien"], ["chat-garde-pau-72.webp", 267, 366, "chat"], ["chat-garde-pau-73.webp", 278, 366, "chat"], ["chat-garde-pau-74.webp", 279, 366, "chat"], ["chat-garde-pau-75.webp", 278, 366, "chat"], ["chien-garde-pau-17.webp", 273, 366, "chien"], ["chat-garde-pau-76.webp", 274, 363, "chat"], ["chat-garde-pau-77.webp", 279, 363, "chat"], ["chat-garde-pau-78.webp", 278, 363, "chat"], ["chat-garde-pau-79.webp", 272, 363, "chat"], ["chat-garde-pau-80.webp", 274, 371, "chat"], ["chat-garde-pau-81.webp", 278, 371, "chat"], ["chat-garde-pau-82.webp", 279, 371, "chat"], ["chat-garde-pau-83.webp", 278, 371, "chat"], ["chien-garde-pau-18.webp", 274, 364, "chien"], ["chat-garde-pau-84.webp", 278, 364, "chat"], ["chat-garde-pau-85.webp", 279, 364, "chat"], ["chien-garde-pau-19.webp", 272, 364, "chien"], ["chat-garde-pau-86.webp", 273, 365, "chat"], ["chat-garde-pau-87.webp", 278, 365, "chat"], ["chats-garde-pau-02.webp", 279, 365, "chats"], ["chat-garde-pau-88.webp", 278, 365, "chat"], ["chiens-garde-pau-03.webp", 274, 365, "chiens"], ["chat-garde-pau-89.webp", 273, 371, "chat"], ["chat-garde-pau-90.webp", 278, 371, "chat"], ["chat-garde-pau-91.webp", 278, 371, "chat"], ["chat-garde-pau-92.webp", 274, 371, "chat"], ["chat-garde-pau-93.webp", 273, 362, "chat"], ["chats-garde-pau-03.webp", 278, 362, "chats"], ["chat-garde-pau-94.webp", 279, 362, "chat"], ["chat-garde-pau-95.webp", 278, 362, "chat"], ["chat-garde-pau-96.webp", 274, 362, "chat"], ["chat-garde-pau-97.webp", 274, 366, "chat"], ["chat-garde-pau-98.webp", 278, 366, "chat"], ["chat-garde-pau-99.webp", 279, 366, "chat"], ["chat-garde-pau-100.webp", 278, 365, "chat"], ["chat-garde-pau-101.webp", 274, 372, "chat"], ["chat-garde-pau-102.webp", 278, 372, "chat"], ["chat-garde-pau-103.webp", 279, 372, "chat"], ["chat-garde-pau-104.webp", 278, 372, "chat"], ["chat-garde-pau-105.webp", 274, 365, "chat"], ["chat-garde-pau-106.webp", 278, 365, "chat"], ["chien-garde-pau-20.webp", 279, 365, "chien"], ["chat-garde-pau-107.webp", 278, 365, "chat"], ["chat-garde-pau-108.webp", 272, 365, "chat"], ["chat-garde-pau-109.webp", 274, 367, "chat"], ["chat-garde-pau-110.webp", 278, 367, "chat"], ["chat-garde-pau-111.webp", 279, 367, "chat"], ["chat-garde-pau-112.webp", 278, 367, "chat"], ["chats-garde-pau-04.webp", 269, 367, "chats"], ["chat-garde-pau-113.webp", 274, 371, "chat"], ["chat-garde-pau-114.webp", 278, 371, "chat"], ["chat-garde-pau-115.webp", 279, 371, "chat"], ["chat-garde-pau-116.webp", 278, 371, "chat"], ["chien-garde-pau-21.webp", 269, 371, "chien"], ["chat-garde-pau-117.webp", 278, 362, "chat"], ["chat-garde-pau-118.webp", 279, 362, "chat"], ["chat-garde-pau-119.webp", 278, 355, "chat"], ["chien-garde-pau-22.webp", 279, 355, "chien"], ["chat-garde-pau-120.webp", 278, 355, "chat"], ["chat-garde-pau-121.webp", 271, 368, "chat"], ["chat-garde-pau-122.webp", 278, 368, "chat"], ["chat-garde-pau-123.webp", 279, 368, "chat"], ["chat-garde-pau-124.webp", 261, 368, "chat"], ["chien-garde-pau-23.webp", 272, 358, "chien"], ["chat-garde-pau-125.webp", 278, 358, "chat"], ["chiens-garde-pau-04.webp", 272, 358, "chiens"]]
GAL_ALT = {"chien": "Chien gardé à domicile à Pau par Pattoune chez soi", "chiens": "Chiens gardés à domicile à Pau par Pattoune chez soi",
           "chat": "Chat gardé à domicile à Pau par Pattoune chez soi", "chats": "Chats gardés à domicile à Pau par Pattoune chez soi",
           "lapin": "Lapin gardé à domicile à Pau par Pattoune chez soi"}
GAL_FIRST = 18
gallery_html = "".join(
    f'<li class="g-item" style="--i:{i % 6}"{" hidden" if i >= GAL_FIRST else ""}><button type="button" class="g-btn" data-i="{i}" aria-label="Agrandir la photo : {GAL_ALT[sp]}">'
    f'<img src="assets/img/pattounes/{f}" width="{w}" height="{h}" alt="{GAL_ALT[sp]}" loading="lazy" decoding="async">'
    f'<span class="g-zoom" aria-hidden="true"><svg><use href="#paw"/></svg></span></button></li>'
    for i, (f, w, h, sp) in enumerate(GALLERY))

def kicker(t): return f'<span class="kicker">{t}</span>'
def li_check(t): return f"<li>{icon('i-check')}<span>{t}</span></li>"


# Vrais avis Google (repris de l ancien site ; dates volontairement non affichées)
REVIEWS = [
    ("Celine Desurmont", "septembre 2023", "Chat", "Nous cherchions quelqu'un pour s'occuper de notre chatte Ori pendant nos déplacements professionnels et nos vacances et nous sommes tombés sur Alicia, dont les avis étaient très rassurants... et ils sont tout à fait fondés ! Elle est très sérieuse et douce, et on sent qu'elle aime profondément nos compagnons poilus. Elle a su apprivoiser notre Ori, qui peut parfois être un peu sélective dans ses contacts avec les humains. On part l'esprit tranquille à présent. N'hésitez pas à faire appel à Alicia !"),
    ("Aurélie Clarens", "mai 2023", "Chien", "Je suis très satisfaite de mon expérience. Alicia est adorable, elle a pris soin de mon chien comme si c’était le sien. Elle m’envoyait des nouvelles à chaque passage. Je referais appel à elle dès que besoin."),
    ("Marion CURT", "août 2023", "Souris", "Première fois que j'ose faire garder mes souris et laisser les clés à quelqu'un. J'en ai été ravie. Très sérieuse. Avec contrat et prise de notes pour les tâches à effectuer. Du coup j'ai pu partir deux fois cette année en vacances avec l'esprit tranquille. Je recommande à 100%."),
    ("Mehdi Lafenêtre", "mai 2023", "2 Sacrés de Birmanie", "Alicia est la nounou officielle de mes deux sacrés de Birmanie depuis plusieurs mois. Ils l’adorent et je sais que je peux partir serein si je dois m’absenter plusieurs jours. Je recommande à 200%, si vous souhaitez faire garder vos animaux, foncez les yeux fermés !"),
    ("marina", "septembre 2023", "Léon", "Je recommande fortement les services d’Alicia qui est une personne formidable, sympathique, ponctuelle et très professionnelle. Alicia s’est occupée parfaitement de notre adorable Léon pendant notre absence et nous a envoyé des vidéos et photos quotidiennes. Nous referons appel à elle sans hésiter pour nos prochaines absences."),
    ("St Tel", "août 2023", "4 chats", "Alicia s'est occupée pendant 10 jours de mes 4 chats, je recommande vraiment pour sa gentillesse, sa disponibilité, mes chats étaient bien heureux de la voir tous les jours et moi d'avoir de leurs nouvelles quotidiennement. Vraiment parfait !"),
]
from html import escape as _e
reviews_html = "".join(
    f'<figure class="review reveal" style="--d:{i * 0.08:.2f}s"><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div>'
    f'<blockquote>«&nbsp;{_e(t)}&nbsp;»</blockquote><figcaption><span class="avatar" aria-hidden="true">{_e(n[0].upper())}</span>'
    f'<span><strong>{_e(n)}</strong><small>{_e(a)} · avis Google</small></span></figcaption></figure>'
    for i, (n, d, a, t) in enumerate(REVIEWS))

body = f'''<section class="hero" id="accueil">
 <svg class="deco" data-parallax="0.15" style="width:180px;left:-40px;top:60px;transform:rotate(-20deg)" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="#paw"/></svg>
 <div class="wrap">
  <div>
   <span class="eyebrow reveal">{icon("i-pin")} Pet sitter à Pau &amp; 12 km autour</span>
   <h1 class="reveal" style="--d:.1s">Garde de chien et chat à domicile à Pau, pour des <em>Pattounes<svg viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14C50 4 150 4 197 12"/></svg></em> heureuses&nbsp;!</h1>
   <p class="lead reveal" style="--d:.2s">Partez 100 % serein. Votre compagnon reste chez lui, dans ses habitudes, et je viens m’occuper de lui : repas, câlins, promenades. Vous recevez des photos et des nouvelles chaque jour.</p>
   <div class="hero-cta reveal" style="--d:.3s">
    <a class="btn" href="#contact">Réserver une garde {ARROW}</a>
    <a class="btn btn--ghost" href="#chien">Voir les formules</a>
   </div>
   <ul class="trust reveal" style="--d:.4s">
    <li><span class="stars" aria-hidden="true">★★★★★</span> 5/5 sur Google</li>
    <li>{icon("i-shield")} Diplômée ACACED · assurée</li>
   </ul>
  </div>
  <div class="hero-art reveal reveal--zoom" style="--d:.2s">
   <div class="hero-blob"></div>
   {HERO_ILLUS}
   <div class="hero-mini hero-mini--dog" data-parallax="0.06"><img src="assets/img/chien-heureux.jpg" alt="Chien heureux, la gueule ouverte, gardé à domicile à Pau" width="556" height="520" decoding="async"></div>
   <div class="hero-mini hero-mini--cat" data-parallax="-0.08"><img src="assets/img/chat-birman-carre.jpg" alt="" width="246" height="246" decoding="async"></div>
   <div class="hero-mini hero-mini--dogs" data-parallax="0.1"><img src="assets/img/deux-chiens.jpg" alt="" width="96" height="96" decoding="async"></div>
   <div class="hero-mini hero-mini--hills" data-parallax="0.05"><img src="assets/img/collines.jpg" alt="" width="96" height="196" decoding="async"></div>
   <div class="float-card float-card--a"><span class="ico" aria-hidden="true">📸</span><span>Photos &amp; vidéos<small>chaque jour</small></span></div>
   <div class="float-card float-card--b"><span class="ico" aria-hidden="true">🏡</span><span>Il reste chez lui<small>zéro stress</small></span></div>
   <div class="float-card float-card--c"><span class="ico" aria-hidden="true">🐾</span><span>Formules dès 10 €<small>par jour</small></span></div>
  </div>
 </div>
</section>

<div class="marquee-clip"><div class="marquee" aria-label="Quelques Pattounes déjà gardées"><div class="marquee-track">{mq}{mq2}</div></div></div>

<section class="section" id="pourquoi">
 <div class="wrap">
  <div class="intro-split intro-split--rev">
   <div class="intro-text reveal reveal--right">{kicker("Pourquoi la garde à domicile ?")}<h2>Pas de stress, ni pour vous ni pour votre animal</h2><p class="subtitle">Un loulou bien dans ses pattounes jusqu’à votre retour</p><p>Pas de transport, pas de pension, pas de nouvelles habitudes. Votre compagnon reste dans son environnement, et vous choisissez librement le nombre de visites et leur durée. Photos, vidéos, appel et compte rendu écrit : vous savez chaque jour que tout va bien.</p></div>
   <div class="px reveal reveal--left" aria-hidden="true">
    <div class="px-clip"><img class="px-bg" data-parallax="0.12" src="assets/img/foret-lumiere-pau.jpg" alt="" width="1253" height="835" style="object-position:60% 50%" loading="lazy" decoding="async"></div>
    <figure class="px-fg" data-parallax="-0.07"><img src="assets/img/chat-sacre-portrait.jpg" alt="" width="398" height="578" loading="lazy" decoding="async"></figure>
   </div>
  </div>
  <div class="grid grid-3" data-stagger>
   <article class="card" data-tilt><div class="icon">{icon("i-home")}</div><h3>Animaux apaisés</h3><p>Il garde sa maison, ses odeurs et son rythme. Aucun déplacement, aucun stress.</p></article>
   <article class="card" data-tilt><div class="icon">{icon("i-smile")}</div><h3>Maîtres rassurés</h3><p>Une professionnelle de confiance s’occupe de votre compagnon comme du sien. Vous profitez vraiment de votre absence.</p></article>
   <article class="card" data-tilt><div class="icon">{icon("i-cap")}</div><h3>Pet sitter qualifiée</h3><p>ACACED, formation en éducation canine et élevage, premiers secours animaliers et assurance RC.</p></article>
   <article class="card" data-tilt><div class="icon">{icon("i-mobile")}</div><h3>Des nouvelles chaque jour</h3><p>Photos, vidéos, appel et compte rendu écrit : vous savez que tout va bien.</p></article>
   <article class="card" data-tilt><div class="icon">{icon("i-star")}</div><h3>100 % sur mesure</h3><p>Vous choisissez le nombre de visites et leur durée. Je m’adapte à votre animal.</p></article>
   <a class="card card--cta" href="#contact"><div class="icon">{icon("i-sms")}</div><h3>Une question&nbsp;?</h3><p>Écrivez-moi par SMS au <strong>{TEL}</strong> ou par e-mail.</p><span class="more">Me contacter <span>→</span></span></a>
  </div>
 </div>
</section>

{WAVE_DOWN("#FFFFFF")}
<section class="section section--white" id="alicia" style="padding-top:50px">
 <div class="wrap about">
  <div class="about-photo-wrap reveal reveal--left">
   <div class="about-photo"><img src="assets/img/alicia-pet-sitter-pau.jpg" alt="Alicia, pet sitter à Pau, assise dans l’herbe avec un shiba inu noir et feu" width="541" height="541" loading="lazy" decoding="async"></div>
   <div class="about-badge">🐾 Éleveuse familiale de Sacrés de Birmanie</div>
   <svg class="deco" style="width:120px;right:0;top:-10px;opacity:.15;color:var(--coral);transform:rotate(18deg)" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><use href="#paw"/></svg>
  </div>
  <div class="reveal reveal--right">
   {kicker("Qui suis-je ?")}
   <h2>Alicia, la pet sitter qui garde votre animal comme le sien</h2>
   <p class="subtitle">Diplômée de l’ACACED, formée à l’éducation canine et aux premiers secours animaliers.</p>
   <p>Passionnée d’animaux depuis toujours, j’ai moi-même plusieurs compagnons. Je sais donc à quel point les faire garder pendant les vacances ou un imprévu peut être un vrai casse-tête.</p>
   <p>J’ai créé le service que j’aurais aimé trouver : une garde sur mesure, chez vous, qui perturbe le moins possible votre animal. Très exigeante quand je fais garder les miens, je le suis tout autant avec les vôtres. Leur bien-être passe avant tout.</p>
   <ul class="checks">
    {li_check("Certificat professionnel des métiers animaliers, spécialité éducation et élevage")}
    {li_check("Titulaire de l’ACACED, obligatoire pour travailler avec les animaux")}
    {li_check("Formée aux premiers secours animaliers")}
    {li_check("Assurance responsabilité civile")}
   </ul>
   <a class="btn" href="#contact">Faire connaissance {ARROW}</a>
  </div>
 </div>
</section>

<section class="section" id="chien">
 <div class="wrap">
  <div class="intro-split">
   <div class="intro-text reveal reveal--left">{kicker("Formules chien")}<h2>Garde de chien à domicile à Pau</h2><p class="subtitle">Pour votre petit toutou</p><p>Calme, baladeur ou sportif ? Choisissez la formule qui lui ressemble : je viens le nourrir, le câliner et le promener, en ville, au bois de Pau ou en forêt. Prix par jour. Le déplacement est offert pour la première visite seulement (rencontre et signature du contrat), jusqu’à 4 km de Pau.</p></div>
   <div class="px reveal reveal--right" aria-hidden="true">
    <div class="px-clip"><img class="px-bg" data-parallax="0.12" src="assets/img/foret-lumiere-pau.jpg" alt="" width="1253" height="835" loading="lazy" decoding="async"></div>
    <figure class="px-fg" data-parallax="-0.07"><img src="assets/img/chien-laisse.jpg" alt="" width="442" height="642" loading="lazy" decoding="async"></figure>
   </div>
  </div>
  <div class="price-grid" data-stagger>
   <article class="price" data-tilt><h3>Chien tranquille</h3><div class="amount">26 €<small> /jour</small></div><p>Il préfère le canapé aux grandes balades : de petites sorties de quartier lui suffisent.</p><ul><li>2 visites de 30 min par jour</li><li>Idéal pour les chiens qui sortent peu</li></ul></article>
   <article class="price price--featured" data-tilt><span class="tag">Le bon équilibre</span><h3>Chien baladeur</h3><div class="amount">34 €<small> /jour</small></div><p>Il adore se promener et a besoin d’une bonne balade pour se dégourdir les pattounes.</p><ul><li>1 visite de 30 min + 1 visite d’1 h par jour</li><li>Balade en forêt ou grands espaces : +8 € la promenade</li></ul></article>
   <article class="price" data-tilt><h3>Chien sportif</h3><div class="amount">38 €<small> /jour</small></div><p>Il a besoin de se dépenser chaque jour dans de grands espaces.</p><ul><li>2 visites d’1 h, soit 2 h de balade par jour</li><li>Balade en plein air (forêt, bois de Pau…) : +15 €</li><li>En laisse, en longe ou en liberté s’il a un bon rappel, avec votre accord</li></ul></article>
  </div>
  <div class="sur-mesure reveal">
   <div><h3>Formule sur mesure</h3><p>Visites régulières, demi-journée privatisée… Parfait pour les chiens qui supportent mal la solitude ou qui ont tendance à faire des bêtises. Devis gratuit.</p></div>
   <a class="btn btn--light" href="#contact">Demander un devis {ARROW}</a>
  </div>
  <ul class="bonus" data-stagger>
   <li><span aria-hidden="true">🦮</span><span><strong>Longe fournie</strong> si vous n’en avez pas</span></li>
   <li><span aria-hidden="true">📍</span><span><strong>Collier GPS Tractive</strong> pour les balades en liberté en toute sécurité</span></li>
   <li><span aria-hidden="true">🚗</span><span><strong>Voiture équipée</strong> pour l’emmener en balade (harnais conseillé)</span></li>
  </ul>

  <div id="chien-carte" class="sub-head reveal"><h3>Visites et promenades à la carte</h3><p>Composez vos journées comme vous voulez, par exemple 8h30 et 15h le lundi, 10h et 17h30 le mardi. Choisissez la distance entre chez vous et Pau :</p></div>
  <div class="reveal">{zone_tabs("chien", dog_zones)}</div>

  <div class="sub-head reveal"><h3>Toujours inclus pour votre chien</h3></div>
  <ul class="included" data-stagger>
   <li><span>🥣</span> Remise à niveau des croquettes et de l’eau fraîche</li><li><span>🦴</span> Friandises à votre demande</li>
   <li><span>🎾</span> Jeux et caresses</li><li><span>🌳</span> Balades selon la formule</li>
   <li><span>🧽</span> Nettoyage des petites bêtises</li><li><span>🪮</span> Soins : yeux, oreilles, brossage</li>
   <li><span>💊</span> Médicaments si besoin</li><li><span>📸</span> Photos et nouvelles</li>
  </ul>
 </div>
</section>

{WAVE_DOWN("#FFFFFF")}
<section class="section section--white" id="chat" style="padding-top:50px">
 <div class="wrap">
  <div class="intro-split intro-split--rev">
   <div class="intro-text reveal reveal--right">{kicker("Formules chat")}<h2>Garde de chat à domicile à Pau</h2><p class="subtitle">Pour votre matou</p><p>Les chats détestent changer d’endroit. Le vôtre reste tranquillement chez lui : je passe le nourrir, m’occuper de sa litière et le câliner. Prix par jour. Le déplacement est offert pour la première visite seulement (rencontre et signature du contrat), jusqu’à 4 km de Pau.</p></div>
   <div class="px reveal reveal--left" aria-hidden="true">
    <div class="px-clip"><img class="px-bg" data-parallax="0.12" src="assets/img/salon-pau.jpg" alt="" width="1261" height="839" style="object-position:40% 50%" loading="lazy" decoding="async"></div>
    <figure class="px-fg" data-parallax="-0.07"><img src="assets/img/chat-sacre-de-birmanie.jpg" alt="" width="444" height="642" loading="lazy" decoding="async"></figure>
   </div>
  </div>
  <div class="price-grid" data-stagger>
   <article class="price" data-tilt><h3>Chat d’intérieur solitaire</h3><div class="amount">12 €<small> /jour</small></div><p>Un peu craintif, il aime les câlins… de loin, et préfère être seul.</p><ul><li>1 visite de 30 min par jour</li></ul></article>
   <article class="price price--featured" data-tilt><span class="tag">Câlins garantis</span><h3>Chat d’intérieur sociable</h3><div class="amount">22 €<small> /jour</small></div><p>Il vit en appartement, il est affectueux et a besoin de présence.</p><ul><li>2 visites de 30 min par jour</li></ul></article>
   <article class="price" data-tilt><h3>Chat d’extérieur</h3><div class="amount">10 €<small> /jour</small></div><p>Il sort à sa guise. Même s’il n’est pas là à mon passage, je m’assure de le voir pendant votre absence.</p><ul><li>1 visite de 20 min par jour</li></ul></article>
  </div>

  <div class="sub-head reveal"><h3>Visites à la carte</h3><p>Choisissez la distance entre chez vous et Pau :</p></div>
  <div class="reveal">{zone_tabs("chat", cat_zones)}</div>
  <p class="price-note">Visites d’1 h : 2 par jour maximum.</p>

  <div class="sub-head reveal"><h3>Toujours inclus pour votre chat</h3></div>
  <ul class="included" data-stagger>
   <li><span>🥣</span> Remise à niveau des croquettes et de l’eau fraîche</li><li><span>🧹</span> Litière nettoyée</li>
   <li><span>🗑️</span> Ma poubelle Litter Locker</li><li><span>🧶</span> Jeux et caresses</li>
   <li><span>🧽</span> Nettoyage des petites bêtises</li><li><span>🪮</span> Soins : yeux, oreilles, brossage</li>
   <li><span>💊</span> Médicaments si besoin</li><li><span>📸</span> Photos et nouvelles</li>
  </ul>
 </div>
</section>

<section class="section" id="famille">
 <div class="wrap">
  <div class="family reveal reveal--zoom">
   <div class="family-text">{kicker("Famille nombreuse")}<h2>Plusieurs compagnons ? Profitez du tarif de groupe</h2><p>Pas de soucis : à partir du deuxième animal, vous ne payez qu’un petit supplément.</p></div>
   <div class="family-prices">
    <div class="pill"><strong>+4 €</strong><span>par chat en plus</span></div>
    <div class="pill"><strong>+8 €</strong><span>par chien en plus</span></div>
   </div>
   <p class="family-ex">Exemple : 1 visite de 30 min par jour pour 2 chats = <strong>16 €</strong> au lieu de 24 €.</p>
  </div>
  <p class="price-note reveal" id="autres">Rongeurs, oiseaux et poissons sont aussi les bienvenus, sur devis (pas de reptiles).</p>
 </div>
</section>

<section class="section section--forest" id="reservation">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Réservation")}<h2>Réserver en 4 étapes simples</h2><p>Une garde de votre animal sans stress et en toute confiance.</p></div>
  <div class="steps" data-stagger>
   <div class="step"><h3>Vous me contactez</h3><p>Par e-mail ou SMS écrit, avec votre animal (race, âge), la formule, les dates et votre adresse.</p></div>
   <div class="step"><h3>On se rencontre</h3><p>Je vous envoie un devis et on organise une première visite chez vous pour faire connaissance et signer le contrat. Elle est gratuite jusqu’à 4 km de Pau.</p></div>
   <div class="step"><h3>On signe le contrat</h3><p>Un petit questionnaire pour bien connaître votre animal, puis vous me confiez un double des clés.</p></div>
   <div class="step"><h3>Vous partez serein</h3><p>Je m’occupe de tout et vous envoie photos, vidéos et nouvelles chaque jour.</p></div>
  </div>
  <div style="text-align:center;margin-top:44px" class="reveal"><a class="btn" href="#contact">Je réserve {ARROW}</a></div>
 </div>
</section>

<section class="section" id="avis">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Avis clients")}<h2>Ils m’ont confié leurs Pattounes</h2><p>Quelques avis laissés sur Google par les familles des animaux gardés.</p></div>
  <div class="rating reveal">
   <div class="score"><span class="big">5,0</span><div><div class="stars" aria-label="5 étoiles sur 5">★★★★★</div><strong>Note moyenne sur Google</strong><br><span style="color:var(--ink-soft)">Merci à toutes les familles des Pattounes gardées&nbsp;!</span></div></div>
   <a class="btn btn--ghost" href="{GOOGLE_AVIS}" target="_blank" rel="noopener">Tous les avis Google {ARROW}</a>
  </div>
  <div class="reviews">{reviews_html}</div>
 </div>
</section>

<section class="section" id="pattounes" style="padding-top:20px">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Les Pattounes gardées")}<h2>Ils ont été gardés chez eux, comme des rois</h2><p>Chats, chiens et même un lapin : voici quelques-uns des compagnons dont je me suis occupée à Pau et aux alentours.</p></div>
  <ul class="gallery" id="gallery" role="list">{gallery_html}</ul>
  <div class="gallery-actions reveal">
   <button class="btn" type="button" id="gallery-more" aria-expanded="false">Voir toutes les photos</button>
   <a class="btn btn--ghost" href="{IG}" target="_blank" rel="noopener">{icon("i-ig")} Suivre sur Instagram</a>
  </div>
 </div>
 <dialog class="lightbox" id="lightbox" aria-label="Photo agrandie">
  <figure class="lb-fig"><img class="lb-img" src="" alt=""><figcaption class="lb-count"></figcaption></figure>
  <button class="lb-btn lb-prev" type="button" aria-label="Photo précédente">&#8249;</button>
  <button class="lb-btn lb-next" type="button" aria-label="Photo suivante">&#8250;</button>
  <button class="lb-btn lb-close" type="button" aria-label="Fermer">&#215;</button>
 </dialog>
</section>

{WAVE_DOWN("#FFFFFF")}
<section class="section section--white" id="zone" style="padding-top:50px">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Zone d’intervention")}<h2>Pet sitter à Pau et dans un rayon de 12 km</h2><p>Je me déplace chez vous à Pau et dans toutes les communes à 12 km maximum.</p></div>
  <div class="about">
   <div class="zone-map reveal reveal--zoom" role="img" aria-label="Carte schématique : Pau au centre, cercles à 4, 8 et 12 km et principales communes desservies">
    <span class="ring" style="--i:0%" data-label="12 km"></span>
    <span class="ring" style="--i:16.7%" data-label="8 km"></span>
    <span class="ring" style="--i:33.3%" data-label="4 km"></span>
    <span class="center">Pau</span>
    {map_html}
   </div>
   <div class="reveal reveal--right">
    <h3>Combien coûte le déplacement ?</h3>
    <ul class="checks">
     {li_check("<strong>Jusqu’à 4 km</strong> : compris dans le prix, première rencontre et remise des clés offertes.")}
     {li_check("<strong>De 4 à 8 km</strong> : tarifs à la carte « 4-8 km », remise des clés 6 €.")}
     {li_check("<strong>De 8 à 12 km</strong> : tarifs à la carte « 8-12 km », remise des clés 9 €.")}
    </ul>
    <p>Un doute sur votre zone ? Envoyez-moi un SMS ou un e-mail, je vous le confirme rapidement.</p>
   </div>
  </div>
  <ul class="towns" data-stagger style="margin-top:50px">{"".join(f"<li><span>{t}</span></li>" for t in TOWNS)}</ul>
  <p class="seo-text reveal">Garde de chien et de chat à domicile, visites et promenades à <strong>Pau</strong> et dans l’agglomération : Billère, Lons, Jurançon, Gelos, Bizanos, Idron, Mazères-Lezons. À l’ouest jusqu’à Lescar, Laroin, Artiguelouve, Poey-de-Lescar et Saint-Faust. Au nord à Montardon, Serres-Castet et Buros. À l’est à Morlaàs, Sendets, Ousse et Lée. Au sud à Gan, Rontignon, Uzos, Aressy, Narcastet, Meillon, Assat et Bosdarros.</p>
 </div>
</section>

<section class="section" id="faq">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Questions fréquentes")}<h2>Tout savoir avant de me confier votre compagnon</h2></div>
  <div class="faq" data-stagger>{faq_items}</div>
 </div>
</section>

<section class="section section--white" id="contact">
 <div class="wrap">
  <div class="section-head reveal">{kicker("Contact")}<h2>Réservez la garde de votre animal</h2><p>Par e-mail ou SMS écrit uniquement. Je vous réponds rapidement avec un devis et on fixe ensemble la première rencontre.</p></div>
  <div class="contact-grid">
   <div class="reveal reveal--left">
    <div class="contact-note">
     <p class="contact-note__big">Écrivez-moi par SMS ou par e-mail, je vous réponds rapidement.</p>
     <p>Précisez : nom et prénom, téléphone, animal (race et âge), formule, dates et adresse. Merci&nbsp;!</p>
    </div>
    <ul class="contact-list">
     <li><a href="sms:{TEL_LINK}"><span class="ci">{icon("i-sms")}</span><span><strong>{TEL}</strong><small>Par SMS écrit uniquement</small></span></a></li>
     <li><a href="mailto:{MAIL}"><span class="ci">{icon("i-mail")}</span><span><strong>{MAIL}</strong><small>Réponse rapide par e-mail</small></span></a></li>
          <li><div><span class="ci">{icon("i-pin")}</span><span><strong>Pau (64000) et 12 km autour</strong><small>Je viens chez vous</small></span></div></li>
    </ul>
    <p style="margin-top:22px;color:var(--ink-soft)">WhatsApp possible si vous êtes à l’étranger. Paiement par chèque, virement, espèces ou PayPal.</p>
   </div>
   <form class="form reveal reveal--right" id="devis" novalidate>
    <h3 style="margin:0">Ma demande de garde</h3>
    <div class="row"><label for="f-nom">Nom Prénom<input id="f-nom" name="Nom Prénom" autocomplete="name" required></label><label for="f-tel">Téléphone<input id="f-tel" name="Téléphone" type="tel" autocomplete="tel" required></label></div>
    <div class="row"><label for="f-animal">Animal<select id="f-animal" name="Animal" required><option value="">Choisir…</option><option>Chien</option><option>Chat</option><option>Chien et chat</option><option>Rongeur</option><option>Oiseau</option><option>Poisson</option></select></label><label for="f-race">Race et âge<input id="f-race" name="Race et âge" placeholder="ex. Shiba Inu, 2 ans"></label></div>
    <div class="row"><label for="f-debut">Date de début<input id="f-debut" name="Début" type="date" required></label><label for="f-fin">Date de fin<input id="f-fin" name="Fin" type="date" required></label></div>
    <label for="f-formule">Formule souhaitée<input id="f-formule" name="Formule" placeholder="ex. Chien tranquille"></label>
    <label for="f-adresse">Adresse de la garde<input id="f-adresse" name="Adresse" autocomplete="street-address" placeholder="Rue, commune" required></label>
    <label for="f-msg">Message<textarea id="f-msg" name="Message" placeholder="Caractère, habitudes, horaires souhaités…"></textarea></label>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><button class="btn" type="submit" name="canal" value="mail">Envoyer par e-mail {ARROW}</button><button class="btn btn--ghost" type="submit" name="canal" value="sms">Envoyer par SMS</button></div>
    <p class="hint">Aucune donnée n’est stockée sur ce site : le formulaire ouvre simplement votre messagerie avec le message prêt à envoyer.</p>
   </form>
  </div>
 </div>
</section>'''

page("index.html", "Pet sitter à Pau : garde de chien et chat à domicile | Pattoune chez soi",
     "Pattoune chez soi, pet sitter diplômée à Pau : garde de chien et chat à votre domicile, visites et promenades à Pau, Billère, Lons, Lescar, Jurançon et jusqu’à 12 km. Dès 10 €/jour.",
     body, graph)


# --------------------------------------------------------------- MENTIONS
bc = [("Accueil", "index.html"), ("Mentions légales", "mentions-legales.html")]
ml = f'''<section class="page-hero"><div class="wrap">{crumbs_html(bc)}<h1>Mentions légales</h1></div></section>
<section class="section section--white" style="padding-top:60px"><div class="wrap prose">
 <h2>Éditeur du site</h2>
 <p>Pattoune chez soi, Alicia [NOM À COMPLÉTER], entrepreneur individuel<br>SIRET : 920 022 464 00019<br>Adresse : [ADRESSE À COMPLÉTER], 64000 Pau<br>Téléphone : {TEL} · E-mail : <a href="mailto:{MAIL}">{MAIL}</a><br>Directrice de la publication : Alicia [NOM À COMPLÉTER]</p>
 <h2>Hébergement</h2>
 <p>OVH SAS, 2 rue Kellermann, 59100 Roubaix, France · Téléphone : 1007 · <a href="https://www.ovhcloud.com" rel="noopener">www.ovhcloud.com</a></p>
 <h2>Données personnelles</h2>
 <p>Ce site ne dépose aucun cookie et n’utilise aucun outil de mesure d’audience. Le formulaire de contact ne stocke aucune donnée : il ouvre votre messagerie ou votre application SMS. Les informations que vous m’envoyez servent uniquement à organiser la garde de votre animal. Vous pouvez demander leur suppression à tout moment par e-mail.</p>
 <h2>Propriété intellectuelle</h2>
 <p>Les textes, photos et illustrations de ce site appartiennent à Pattoune chez soi. Toute reproduction sans autorisation est interdite.</p>
</div></section>'''
page("mentions-legales.html", "Mentions légales | Pattoune chez soi", "Mentions légales du site Pattoune chez soi, pet sitter à Pau.", ml, None, "noindex, follow")

# --------------------------------------------------------------- 404
nf = f'''<section class="page-hero" style="text-align:center;padding:100px 0"><div class="wrap">
 <h1>Oups, cette page s’est sauvée&nbsp;!</h1><p class="lead" style="margin-inline:auto">Elle a dû partir en promenade. Revenez à l’accueil pour retrouver toutes les Pattounes.</p>
 <a class="btn" href="index.html">Retour à l’accueil {ARROW}</a></div></section>'''
page("404.html", "Page introuvable | Pattoune chez soi", "Cette page n’existe pas.", nf, None, "noindex, follow")

# --------------------------------------------------------------- SEO files
from datetime import date
today = date.today().isoformat()
urls = [("", "1.0")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}/{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT, "site.webmanifest"), "w").write(json.dumps({
    "name": "Pattoune chez soi", "short_name": "Pattoune", "lang": "fr", "start_url": "/",
    "display": "standalone", "background_color": "#F3F3F6", "theme_color": "#414343",
    "icons": [{"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
              {"src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, ensure_ascii=False, indent=1))
print("ok")
