Dokumentasjon Prosjektoppgave
Prosjekt navn: IRONE CORE
IRONCORE – Samlet Dokumentasjon
 Introduksjon
IRONCORE er en moderne nettbutikk utviklet for salg av treningsutstyr som treningsflasker, lifting straps og compression shirts. Nettbutikken er bygget med HTML, CSS, Python og JavaScript, og alle sidene deler samme mørke, minimalistiske og profesjonelle designprofil.
Dokumentasjonen beskriver hele nettstedet, inkludert:
•	Forsiden (Home)
•	Produktsiden
•	Om oss
•	Kontakt
•	Navigasjon
•	Designprofil
•	Teknisk struktur

 Arkitektur og Teknologi
Frontend
•	HTML for struktur
•	CSS for styling og responsivitet
•	JavaScript for interaktivitet og handlekurvlogikk
Backend
•	Python (flask/django eller annen server) for:
o	Routing
o	Rendering av sider
o	Produktdata
o	Handlekurv og ordrelogikk
Database (hvis brukt)
•	Enkel JSON, Python-datastruktur eller database som MongoDB/MySQL

 Design og Stilprofil (Felles for alle sider)
•	Mørkt tema med sort og grå bakgrunn
•	Hvit tekst for god kontrast
•	Røde detaljer (logo, knapper, rammer) for tydelig merkevareprofil
•	Store overskrifter, god spacing og minimalistisk oppsett
•	Responsivt design:
o	Produkter brytes til én kolonne på mobil
o	Navigasjon skalerer pent
•	Samme navigasjonsmeny og footer på alle sider

 Navigasjonsmeny (Felles Element)
Øverst på alle sider ligger en sticky navbar med:
•	Logoen IRONCORE i rødt
•	Menyvalg:
o	Hjem
o	Produkter
o	Om oss
o	Kontakt
•	Et handlekurv-ikon til høyre
•	Sort bakgrunn og hvit tekst
Dette gir en tydelig og enkel navigasjon gjennom hele nettbutikken.

 1. Forsiden (Home)
Forsiden er bygget for å skape et sterkt førsteinntrykk.
Hero-seksjon
•	Stor kraftfull overskrift:
"Bygg styrke. Bli sterkere hver dag."
•	Undertekst:
"Premium utstyr for deg som tar trening på alvor."
•	Fremhevet rød knapp: "Se produkter", som leder til produktsiden
•	Mørkt bannerområde som fyller skjermen
Populære produkter
Under hero-seksjonen vises en rekke av butikkens mest populære produkter.
•	Produkter vises i et grid
•	Kortene er identiske i stil med produktsiden
•	Brukeren får rask tilgang til bestselgere

 2. Produktsiden
Produktsiden viser hele sortimentet i et strukturert og brukervennlig layout.
Produktsamlingsvisning
Hvert produkt består av et “card” som inneholder:
•	Produktbilde
•	Produktnavn
•	Pris
•	Antall-felt
•	Knapp: "Legg i handlekurv"
Interaktivitet (JavaScript)
•	Registrerer valgt antall
•	Legger produktet i handlekurven
•	Oppdaterer handlekurv-ikonet
•	Kan lagre handlekurven i localStorage eller backend
Backend (Python)
•	Leverer produktdata
•	Håndterer handlekurv og ordre

 3. Om oss-siden
Denne siden gir brukeren innsikt i hva IRONCORE står for.
Innholdstema
•	Merkevarens historie eller visjon
•	Hvorfor nettbutikken eksisterer
•	Hva som gjør produktene premium
•	Fokus på trening, kvalitet og dedikasjon
•	Mørkt design, samme layout som resten
Formål
•	Skape tillit hos kunden
•	Fortelle hva IRONCORE representerer
•	Bygge identitet og troverdighet

 4. Kontakt-siden
Kontakt-siden gjør det enkelt for kunder å få hjelp.
Typiske elementer
•	Kontaktinformasjon (e-post, evt. telefon)
•	Et kontaktskjema
o	Navn
o	E-post
o	Melding
o	Send-knapp
•	Bekreftelse via Python-backend eller JS
Design
•	Samme mørke tema og røde detaljer
•	Overskrifter og input-felt med god lesbarhet

 Handlekurv (Ikon + Logikk)
Handlekurven er tilgjengelig via ikonet øverst til høyre.
Funksjonalitet
•	Viser antall varer
•	Oppdateres automatisk når produkter legges i
•	Kan vises som egen side eller som pop-up (avhengig av implementasjon)
•	Lagres i Python-backend eller lokalt i nettleseren

 Prosjektstruktur (Eksempel)
IRONCORE/
│
├── static/
│   ├── css/          # Globale stiler
│   ├── js/           # Handlekurv og interaktivitet
│   └── images/       # Produktbilder
│
├── templates/
│   ├── index.html    # Forsiden
│   ├── products.html # Produktsiden
│   ├── about.html    # Om oss
│   └── contact.html  # Kontakt
│
├── app.py            # Python-backend med ruter
└── README.md         # Dokumentasjon

🔧 Teknisk Funksjonalitet
HTML
•	Strukturerer alle sider
•	Bruker standard semantiske tagger
CSS
•	Global mørk tema
•	Layout for alle sider
•	Produktrutenett
•	Responsiv design
JavaScript
•	Handlekurvlogikk
•	Klikkhendelser
•	Oppdatering av antall varer
•	Navigasjonsinteraksjoner
Python
•	Serverer sidene
•	Tilbyr ruter: /, /produkter, /om-oss, /kontakt
•	Kan håndtere skjema og ordre
•	Henter produktdata
Git Hub
 <img width="945" height="442" alt="image" src="https://github.com/user-attachments/assets/7505b339-08ea-42f3-ae58-a1595c2bbc54" />

Jeg fikk hjelp av Tarald til å forstå GitHubs Projects-funksjon. Han viste hvordan den kan brukes til å organisere oppgaver og få bedre oversikt over prosjektet. Projects gjorde det enklere å planlegge arbeidet, følge fremdriften og holde struktur, spesielt med flere samtidige oppgaver. Etter å ha brukt det, ser jeg det som et nyttig verktøy jeg vil bruke i fremtidige prosjekter.
 
 Oppsummering
IRONCORE-nettbutikken består av fire helhetlig utformede sider, alle med samme designprofil, samme navigasjonsmeny, og samme mørke estetikk. Kombinasjonen av HTML, CSS, JavaScript og Python gjør prosjektet både visuelt tiltalende og teknisk robust.
Sidenes oppgaver:
•	Forside: Presentere merkevaren og lede brukeren inn i butikken
•	Produkter: Vise hele sortimentet med handlekurvfunksjon
•	Om oss: Bygge troverdighet og forklare hvem IRONCORE er
•	Kontakt: Gi brukeren mulighet til å ta direkte kontakt


