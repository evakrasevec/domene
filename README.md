# Domene na prodaj – dobava.si

Enotna stran za prodajo naših `.si` domen na **https://www.dobava.si**. Vsaka domena ima svojo podstran:

- `https://www.dobava.si/` – seznam vseh domen
- `https://www.dobava.si/agentwork.si` – stran posamezne domene (ime, cena, obrazec za ponudbo)

Vsako prodajano domeno pri registrarju preusmerite na njeno podstran (glej spodaj).
Stran je statična (brez strežnika), v slovenščini in angleščini. Ponudbe pridejo po e-pošti.

## Nastavitev

V `index.html` na vrhu skripte uredite:

```js
const CONTACT_EMAIL = "info@digihelp.si";      // kam pridejo ponudbe
const DOMAINS = [ ... ];                       // seznam domen
```

## Podstrani

Za vsako domeno obstaja mapa `<domena>/index.html` (kopija `index.html`), da deluje naslov
`https://<vaš-naslov>/agentwork.si`. Po vsaki spremembi `index.html` (cene, e-naslov, domene) zaženite:

```
python3 build.py
```

## Objava na Replitu (www.dobava.si)

1. Na Replitu ustvarite nov Repl z uvozom tega GitHub repozitorija (*Import from GitHub*).
   Datoteka `.replit` je že pripravljena za **statično objavo** (Static deployment).
2. Kliknite **Deploy / Publish** → izberite **Static** → objavite.
3. V nastavitvah objave (*Settings → Link a domain*) dodajte `www.dobava.si` in `dobava.si`.
   Replit izpiše zapisa **A** in **TXT**, ki ju vpišete v DNS domene dobava.si pri registrarju.
   Certifikat HTTPS uredi Replit sam.
4. Če uporabljate Cloudflare, nastavite zapise na »DNS only« (siva oblačka), sicer obnova certifikata lahko ne uspe.

## Preusmeritev prodajanih domen

Pri registrarju za vsako domeno nastavite preusmeritev (URL forwarding, **301**) na njeno podstran:

| Domena | Preusmeri na |
|---|---|
| agentwork.si | https://www.dobava.si/agentwork.si |
| modelflow.si | https://www.dobava.si/modelflow.si |
| … | https://www.dobava.si/&lt;domena&gt; |

Če registrar ponuja izbiro, vključite preusmeritev tudi za `www.<domena>`.

## Cene in kartično plačilo (Stripe)

Cene so v `index.html` v seznamu `DOMAINS` (`price` v EUR). `price: null` pomeni, da je možna samo ponudba.

Gumb »Kupi s kartico« se pri domeni prikaže šele, ko vpišete `pay` povezavo:

1. Ustvarite račun na [stripe.com](https://stripe.com).
2. *Product catalog → Add product*: ime npr. »Domena agentwork.si«, enkratna cena po seznamu.
3. *Payment Links → New*: izberite ta izdelek, omejite na 1 nakup (*Limit the number of payments*: 1),
   dodajte polje za telefon / naslov za račun. Pod *After payment* izberite preusmeritev na
   `https://www.dobava.si/agentwork.si?placano=1`.
4. Povezavo (`https://buy.stripe.com/...`) prilepite v `pay` pri tej domeni.

Po plačilu dobite e-pošto od Stripa. Kupcu pošljete **kodo za prenos (AuthInfo)** od registrarja
in mu izstavite račun. Ko je domena prodana, jo odstranite s seznama.

## Domene

agentwork.si, agentworker.si, modelflow.si, agentish.si, gritt.si, ringg.si, lyrie.si, irisgo.si, overnight.si, findapp.si, mindcore.si, flowhub.si
