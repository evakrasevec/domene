# Domene na prodaj

Enotna stran »domena na prodaj« za vse naše `.si` domene. Ena sama statična datoteka (`index.html`), brez strežnika.

Stran sama prepozna, katera domena je bila obiskana, in jo prikaže v naslovu:

- po poti, npr. `https://<vaš-naslov>/agentwork.si` (vsaka domena ima svojo podstran),
- po imenu gostitelja (če vse domene kažejo na isto gostovanje), ali
- po parametru `?d=` (če registrar domeno preusmeri, npr. `https://<ime>.replit.app/?d=agentwork.si`).

Obiskovalec lahko pošlje ponudbo na nastavljeni e-naslov (odpre se e-poštni odjemalec s pripravljenim sporočilom), spodaj pa so navedene vse ostale domene. Stran je v slovenščini in angleščini.

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

## Objava na Replitu

1. Na Replitu ustvarite nov Repl z uvozom tega GitHub repozitorija (*Import from GitHub*).
   Datoteka `.replit` je že pripravljena za **statično objavo** (Static deployment).
2. Kliknite **Deploy / Publish** → izberite **Static** → objavite. Stran dobi naslov `https://<ime>.replit.app`.
3. V nastavitvah objave (*Settings → Link a domain*) dodajte domeno, npr. `agentwork.si`.
   Replit izpiše zapisa **A** in **TXT**, ki ju vpišete v DNS pri registrarju. Certifikat HTTPS uredi Replit sam.
   Ponovite za vsako domeno. Stran po imenu gostitelja sama prikaže pravo domeno.
4. Če uporabljate Cloudflare, nastavite zapise na »DNS only« (siva oblačka), sicer obnova certifikata lahko ne uspe.

**Če Replit ne dovoli toliko domen na eni objavi** (ali tega ne želite urejati za vsako domeno):
na Replit povežete samo eno domeno (npr. `<ime>.replit.app`),
pri registrarju pa za vsako ostalo domeno nastavite preusmeritev (URL forwarding, 301) na:

```
https://<vaš-naslov>/<domena>
```

npr. `https://<ime>.replit.app/modelflow.si`. Stran bo prikazala `modelflow.si`.

## Cene in kartično plačilo (Stripe)

Cene so v `index.html` v seznamu `DOMAINS` (`price` v EUR). `price: null` pomeni, da je možna samo ponudba.

Gumb »Kupi s kartico« se pri domeni prikaže šele, ko vpišete `pay` povezavo:

1. Ustvarite račun na [stripe.com](https://stripe.com).
2. *Product catalog → Add product*: ime npr. »Domena agentwork.si«, enkratna cena 990 EUR.
3. *Payment Links → New*: izberite ta izdelek, omejite na 1 nakup (*Limit the number of payments*: 1),
   dodajte polje za telefon / naslov za račun. Pod *After payment* izberite preusmeritev na
   `https://agentwork.si/?d=agentwork.si&placano=1`.
4. Povezavo (`https://buy.stripe.com/...`) prilepite v `pay` pri tej domeni.

Po plačilu dobite e-pošto od Stripa. Kupcu pošljete **kodo za prenos (AuthInfo)** od registrarja
in mu izstavite račun. Ko je domena prodana, jo odstranite s seznama.

## Domene

agentwork.si, agentworker.si, modelflow.si, agentish.si, gritt.si, ringg.si, lyrie.si, irisgo.si, overnight.si, findapp.si, mindcore.si, flowhub.si
