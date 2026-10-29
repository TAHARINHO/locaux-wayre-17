#!/usr/bin/env python3.12
"""Fiches WAYRE — A4 2 pages, données du site way-re.com."""
import pathlib

IMG = "/var/www/way-re.com/images"
OUT = pathlib.Path("/root/work/locaux-wayre-17/fiches")
OUT.mkdir(exist_ok=True)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;500;600;700&family=Hanken+Grotesk:wght@300;400;500;600&display=swap');
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
:root{--bg:#0B0A09;--card:#17140F;--ink:#F1EEE8;--muted:#AAA397;--gold:#EBCB70;--gold-l:#F5D89A;
--gold-d:#CF9F3D;--gold-ink:#1A1204;--line:rgba(235,203,112,.16);--slate:#7E94A8}
html,body{background:#fff}
body{font-family:'Hanken Grotesk',Arial,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.page{width:210mm;height:297mm;background:var(--bg);position:relative;overflow:hidden;display:flex;flex-direction:column}
.page+.page{page-break-before:always}
.glow{position:absolute;border-radius:50%;filter:blur(150px);pointer-events:none;z-index:0}
.g1{width:520px;height:520px;background:var(--gold);opacity:.15;top:-280px;right:-200px}
.g2{width:480px;height:480px;background:#26333F;opacity:.5;bottom:-280px;left:-220px}

/* bandeau */
.hero{position:relative;height:84mm;flex:none;overflow:hidden}
.hero>img{width:100%;height:100%;object-fit:cover;display:block;filter:brightness(.88) contrast(1.05) saturate(.95)}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,10,9,.30) 0%,rgba(11,10,9,.10) 26%,rgba(11,10,9,.72) 62%,rgba(11,10,9,.96) 84%,var(--bg) 100%)}
.badge{position:absolute;top:11mm;left:14mm;z-index:3;display:inline-flex;align-items:center;gap:7px;
background:rgba(251,248,242,.96);color:#1A1204;border-radius:99px;padding:6px 14px;font-size:7.6pt;font-weight:600;letter-spacing:.04em}
.badge i{width:5px;height:5px;border-radius:50%;background:var(--gold-d);display:block}
.hero img.logo{position:absolute;top:11mm;right:14mm;z-index:3;height:5mm;width:auto;object-fit:contain;opacity:.92}

/* tête */
.head{padding:0 14mm;margin-top:-9mm;position:relative;z-index:2}
.kicker{font-family:'Sora';font-size:7.6pt;letter-spacing:.34em;color:var(--gold);font-weight:500;text-transform:uppercase}
h1{font-family:'Sora';font-weight:200;font-size:23pt;line-height:1.14;letter-spacing:-.02em;margin-top:4.5mm;color:var(--ink);max-width:152mm}
h1 b{font-weight:600;color:var(--gold)}
.sub{margin-top:4mm;font-size:9pt;color:var(--muted);line-height:1.5;max-width:130mm;font-weight:300}

/* chiffres */
.figs{display:grid;grid-template-columns:repeat(4,1fr);margin:7mm 14mm 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.fig{padding:4.6mm 3mm;border-right:1px solid var(--line)}
.fig:last-child{border-right:none}
.fig .v{font-family:'Sora';font-weight:300;font-size:20pt;line-height:1;letter-spacing:-.02em}
.fig .v em{font-style:normal;font-size:9.5pt;color:var(--gold);margin-left:2px;font-weight:400}
.fig .l{font-size:6.6pt;color:var(--muted);margin-top:2.4mm;letter-spacing:.02em;line-height:1.35}

/* corps */
.body{display:grid;grid-template-columns:1fr 66mm;gap:10mm;padding:6.5mm 14mm 5mm}
.prose p{font-size:9pt;line-height:1.62;color:#D8D2C6;font-weight:300;margin-bottom:3.2mm}
.prose p strong{color:var(--ink);font-weight:500}
.quote{margin-top:4mm;padding:4mm 0 4mm 5mm;border-left:2px solid var(--gold);
font-family:'Sora';font-weight:200;font-size:11pt;line-height:1.4;color:var(--gold-l);font-style:italic}

.tech h3{font-family:'Sora';font-size:7pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);
font-weight:500;margin-bottom:3mm}
.tech table{width:100%;border-collapse:collapse}
.tech td{font-size:7.5pt;line-height:1.45;padding:2.1mm 0;border-bottom:1px solid rgba(235,203,112,.10);vertical-align:top}
.tech td:first-child{color:#8C8478;width:26mm;padding-right:3mm}
.tech td:last-child{color:#E7E2D7;font-weight:400}

.strip{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin:0 14mm 6mm;padding-top:4.5mm;border-top:1px solid var(--line)}
.strip .t{font-family:'Sora';font-size:7.6pt;font-weight:500;color:var(--gold);margin-bottom:1.6mm;letter-spacing:.02em}
.strip .d{font-size:7.2pt;line-height:1.5;color:#9E968A;font-weight:300}

/* pied */
.foot{margin-top:auto;padding:0 14mm 8mm;display:flex;justify-content:space-between;align-items:flex-end;
font-size:6pt;color:#6E675C;line-height:1.55}
.foot .l{max-width:120mm}
.foot .r{text-align:right}
.foot b{color:var(--gold);font-weight:500}

/* ═══ PAGE 2 ═══ */
.top2{display:flex;justify-content:space-between;align-items:baseline;padding:12mm 14mm 0;position:relative;z-index:2}
.top2 .k{font-family:'Sora';font-size:7.4pt;letter-spacing:.32em;color:var(--gold);text-transform:uppercase}
.top2 .r{font-size:7.6pt;color:var(--muted)}
.photos{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;padding:7mm 14mm 0}
.ph{position:relative}
.ph img{width:100%;height:64mm;object-fit:cover;display:block;border-radius:2px;filter:brightness(.92) contrast(1.04)}
.ph .cap{font-size:6.6pt;color:var(--muted);margin-top:2.2mm;line-height:1.4}
.p2h{font-family:'Sora';font-weight:200;font-size:15.5pt;letter-spacing:-.01em;padding:9mm 14mm 0;position:relative;z-index:2}
.p2h b{font-weight:600;color:var(--gold)}

.hl{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;padding:6mm 14mm 0}
.hl .t{font-family:'Sora';font-size:9pt;font-weight:500;color:var(--ink);margin-bottom:2mm}
.hl .d{font-size:7.6pt;line-height:1.55;color:#9E968A;font-weight:300}

.dossier{margin:10mm 14mm 0;background:var(--card);border:1px solid var(--line);border-radius:3px;padding:6mm 7mm}
.dossier h4{font-family:'Sora';font-size:7.4pt;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);font-weight:500}
.dossier .lead{font-size:8pt;color:#B9B1A4;margin-top:2.6mm;line-height:1.5;font-weight:300}
.dossier ul{list-style:none;margin-top:4mm;display:grid;grid-template-columns:1fr 1fr;gap:1.6mm 8mm}
.dossier li{font-size:7.6pt;color:#DDD7CB;font-weight:300;padding-left:4mm;position:relative;line-height:1.5}
.dossier li:before{content:"";position:absolute;left:0;top:1.6mm;width:3px;height:3px;background:var(--gold);border-radius:50%}

.cta{margin:9mm 14mm 0;display:flex;justify-content:space-between;align-items:center;gap:10mm;position:relative;z-index:2}
.cta .l .t{font-family:'Sora';font-size:12pt;font-weight:300}
.cta .l .t b{font-weight:600;color:var(--gold)}
.cta .l .d{font-size:7.6pt;color:#9E968A;margin-top:2mm;line-height:1.5;max-width:95mm;font-weight:300}
.cta .r{text-align:right;flex:none}
.cta .mail{display:inline-block;background:var(--gold);color:var(--gold-ink);font-family:'Sora';font-weight:600;
font-size:8.4pt;padding:3.4mm 6mm;border-radius:2px;letter-spacing:.02em}
.cta .site{font-size:7pt;color:var(--muted);margin-top:2.6mm}
.signature{margin:9mm 14mm 0;padding:6.5mm 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
display:flex;justify-content:space-between;align-items:center;gap:8mm}
.signature .m{font-family:'Sora';font-weight:200;font-size:12.5pt;line-height:1.3;letter-spacing:-.01em}
.signature .m b{font-weight:600;color:var(--gold)}
.signature .s{font-size:7.2pt;color:#9E968A;text-align:right;line-height:1.5;max-width:62mm;font-weight:300}
"""

DONNEES = {
    "loue": {
        "fichier": "fiche-local-loue-wayre",
        "badge": "À vendre, loué avec bail commercial",
        "kicker": "75017 · Paris",
        "h1": "Un bail commercial en place,<br><b>7 % brut</b> et 77,40 m² dans le 17e",
        "sub": "Même immeuble, même prix. Ici, vous achetez un revenu déjà versé.",
        "figs": [("650 000", "€", "Prix de vente"), ("41 000", "€", "Loyer annuel hors charges"),
                 ("7", "%", "Rentabilité brute"), ("77,40", "m²", "Surface Carrez")],
        "prose": [
            "Un local de <strong>77,40 m² Carrez</strong>, rez-de-chaussée en duplex sur rue, déjà loué à un exploitant en place.",
            "Le loyer est de <strong>41 000 € par an hors charges</strong>, soit <strong>7 % brut</strong> sur le prix de vente, avant frais d’acquisition.",
            "Vous n’achetez pas un local à louer : vous achetez un bail qui tourne, et un loyer déjà encaissé.",
        ],
        "quote": "Un loyer déjà versé,<br>par un exploitant déjà installé.",
        "tech": [
            ("Surface Carrez", "77,40 m² — certificat de juin 2026"),
            ("Niveau", "Rez-de-chaussée en duplex sur rue"),
            ("Loyer", "41 000 € par an hors charges"),
            ("Rendement", "7 % brut, avant frais d’acquisition"),
            ("Occupation", "Vendu occupé"),
            ("Immeuble", "Copropriété de 1950, 56 lots"),
            ("Taxe foncière", "1 111 € (2026)"),
            ("Diagnostics", "Juin 2026 : pas d’amiante repéré, pas d’indice de termites. DPE vierge."),
        ],
        "photos": [("ecole_hero.jpg", "Le local loué, rez-de-chaussée sur rue."),
                   ("ecole_g1.jpg", "Les bureaux en place, aménagés par l’exploitant."),
                   ("ecole_g2.jpg", "L’espace de travail tel qu’il est aujourd’hui.")],
        "p2h": "Un revenu dès l’acquisition,<br><b>un bail déjà en place.</b>",
        "hl": [("Un revenu dès l’acquisition", "41 000 € par an hors charges, versés par un exploitant déjà installé."),
               ("Un bail commercial", "Un contrat en place, un locataire identifié, une occupation réelle."),
               ("Un seul lot, deux niveaux", "77,40 m² Carrez, rez-de-chaussée en duplex sur rue.")],
        "dossier": ["Bail commercial et quittances de loyer", "Certificats de surface Carrez",
                    "Diagnostics complets (amiante, termites, DPE, risques)", "Titres de propriété",
                    "Procès-verbaux d’assemblées générales", "État des charges de copropriété", "Plans des locaux"],
        "strip": [("Un revenu immédiat", "Le loyer est déjà versé, chaque mois, par l’exploitant en place."),
                  ("Un dossier vérifié", "Surfaces certifiées, diagnostics de juin 2026, bail et quittances."),
                  ("Une visite sur rendez-vous", "L’adresse exacte est communiquée après accord de confidentialité.")],
        "top2r": "Local loué · 650 000 € · 7 % brut",
    },
    "libre": {
        "fichier": "fiche-local-libre-wayre",
        "badge": "À vendre, libre de toute occupation",
        "kicker": "75017 · Paris",
        "h1": "80 m² aménagés, <b>libres</b>,<br>au rez-de-chaussée sur rue",
        "sub": "Même immeuble, même prix. Ici, vous choisissez : occuper, ou louer.",
        "figs": [("650 000", "€", "Prix de vente"), ("80", "m²", "Surface Carrez"),
                 ("3", "", "Bureaux fermés"), ("Libre", "", "Occupation")],
        "prose": [
            "Un rez-de-chaussée sur rue, <strong>libre</strong>, déjà aménagé : un espace ouvert, trois bureaux fermés, sanitaires et rangements intégrés.",
            "Un <strong>sous-sol indépendant de 13 m²</strong> aménagé en bureaux complète l’ensemble. L’accès est adapté aux personnes à mobilité réduite.",
            "Vous l’occupez pour votre activité, ou vous le louez à un utilisateur. Le choix reste ouvert.",
        ],
        "quote": "Vous l’occupez,<br>ou vous le louez.",
        "tech": [
            ("Surface Carrez", "80 m² — certificat de juin 2026"),
            ("Niveau", "Rez-de-chaussée sur rue"),
            ("Composition", "Espace ouvert, 3 bureaux, sanitaires, rangements"),
            ("Annexe", "Sous-sol indépendant de 13 m² aménagé en bureaux"),
            ("Accès", "Rez-de-chaussée sur rue, accès handicapés"),
            ("Occupation", "Libre de toute occupation"),
            ("Immeuble", "Copropriété de 1950, 56 lots"),
            ("Diagnostics", "Juin 2026 : pas d’amiante repéré, pas d’indice de termites. DPE vierge."),
        ],
        "photos": [("vide_hero.jpg", "Le local libre, rez-de-chaussée sur rue."),
                   ("vide_g1.jpg", "L’espace ouvert, prêt à être occupé."),
                   ("vide_g2.jpg", "Les bureaux fermés, déjà aménagés.")],
        "p2h": "Le plan de travail est déjà là,<br><b>il ne reste qu’à s’installer.</b>",
        "hl": [("Aménagement en place", "Espace ouvert, bureaux fermés, point d’eau et rangements intégrés."),
               ("Une vitrine sur rue", "Un rez-de-chaussée visible, pour accueillir clients, patients ou collaborateurs."),
               ("Deux usages possibles", "Occuper les locaux, ou les louer à un utilisateur : le choix reste ouvert.")],
        "dossier": ["Certificats de surface Carrez", "Diagnostics complets (amiante, termites, DPE, risques)",
                    "Titres de propriété", "Procès-verbaux d’assemblées générales",
                    "État des charges de copropriété", "Plans des locaux"],
        "strip": [("Prêt à occuper", "Aménagé, libre : vous entrez et vous travaillez."),
                  ("Une vitrine sur rue", "Visible depuis la rue, pour accueillir clients et collaborateurs."),
                  ("Une visite sur rendez-vous", "L’adresse exacte est communiquée après accord de confidentialité.")],
        "top2r": "Local libre · 650 000 €",
    },
}

PAGE = """<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>WAYRE — {titre}</title><style>{css}</style></head><body>

<section class="page">
  <div class="glow g1"></div>
  <div class="hero">
    <img src="{img}/{hero}" alt="">
    <span class="badge"><i></i>{badge}</span>
    <img class="logo" src="{img}/logo-wayre.png" alt="WAYRE">
  </div>
  <div class="head">
    <div class="kicker">{kicker}</div>
    <h1>{h1}</h1>
    <div class="sub">{sub}</div>
  </div>
  <div class="figs">{figs}</div>
  <div class="body">
    <div class="prose">{prose}<div class="quote">{quote}</div></div>
    <div class="tech"><h3>Le bien</h3><table>{tech}</table></div>
  </div>
  <div class="strip">{strip}</div>
  <div class="foot">
    <div class="l">Informations non contractuelles. Surfaces Carrez issues des certificats de juin 2026. Photos non contractuelles.</div>
    <div class="r"><b>contact@way-re.com</b><br>way-re.com · 1/2</div>
  </div>
</section>

<section class="page">
  <div class="glow g1"></div><div class="glow g2"></div>
  <div class="top2"><div class="k">{kicker}</div><div class="r">{top2r}</div></div>
  <div class="photos">{photos}</div>
  <div class="p2h">{p2h}</div>
  <div class="hl">{hl}</div>
  <div class="dossier">
    <h4>Le dossier complet</h4>
    <div class="lead">Remis après signature d’un accord de confidentialité. L’adresse exacte est communiquée à ce moment-là.</div>
    <ul>{dossier}</ul>
  </div>
  <div class="cta">
    <div class="l"><div class="t">Recevoir le dossier,<br><b>et visiter.</b></div>
      <div class="d">Indiquez votre budget, votre calendrier et votre mode de financement. Visite sur rendez-vous.</div></div>
    <div class="r"><span class="mail">contact@way-re.com</span><div class="site">way-re.com · 2/2</div></div>
  </div>
  <div class="signature">
    <div class="m">Vous parlez enfin au propriétaire.<br><b>Sans agence. Sans commission.</b></div>
    <div class="s">Deux locaux, un seul interlocuteur, un dossier remis en direct après accord de confidentialité.</div>
  </div>
  <div class="foot">
    <div class="l">Informations non contractuelles. Surfaces Carrez issues des certificats de juin 2026. Rendement brut calculé sur le loyer annuel hors charges et le prix de vente, hors frais d’acquisition.</div>
    <div class="r">WAYRE · Paris 17e</div>
  </div>
</section>
</body></html>"""


def construire(cle, d):
    figs = "".join(
        f'<div class="fig"><div class="v">{v}<em>{u}</em></div><div class="l">{l}</div></div>'
        for v, u, l in d["figs"])
    prose = "".join(f"<p>{p}</p>" for p in d["prose"])
    tech = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in d["tech"])
    photos = "".join(
        f'<div class="ph"><img src="{IMG}/{f}" alt=""><div class="cap">{c}</div></div>'
        for f, c in d["photos"])
    hl = "".join(f'<div><div class="t">{t}</div><div class="d">{x}</div></div>' for t, x in d["hl"])
    dossier = "".join(f"<li>{i}</li>" for i in d["dossier"])
    strip = "".join(f'<div><div class="t">{t}</div><div class="d">{x}</div></div>' for t, x in d["strip"])
    html = PAGE.format(css=CSS, img=IMG, titre=d["fichier"].replace("-", " ").title(),
                       hero=d["photos"][0][0], badge=d["badge"], kicker=d["kicker"],
                       h1=d["h1"], sub=d["sub"], figs=figs, prose=prose, quote=d["quote"],
                       tech=tech, photos=photos, p2h=d["p2h"], hl=hl, dossier=dossier,
                       top2r=d["top2r"], strip=strip)
    p = OUT / f"{d['fichier']}.html"
    p.write_text(html, encoding="utf-8")
    print("écrit :", p)
    return p


for cle, d in DONNEES.items():
    construire(cle, d)
