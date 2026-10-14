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

## Kako deluje

- `index.html` – celotna stran (seznam domen, cene, obrazec). Nič ni treba gradit.
- `vercel.json` – na Vercelu:
  - naslov `/agentwork.si` (in vsaka druga `.si` pot) prikaže `index.html`, stran pa sama prepozna domeno;
  - obisk katerekoli prodajane domene (npr. `agentwork.si` ali `www.agentwork.si`) se samodejno
    preusmeri na `https://www.dobava.si/agentwork.si`.

## Objava na Vercelu (GitHub → Vercel)

1. Na [vercel.com](https://vercel.com) se prijavite z GitHub računom.
2. **Add New → Project → Import** repozitorij `evakrasevec/domene`.
   Framework: **Other**, Build Command in Output Directory pustite prazno → **Deploy**.
3. Vsak nov `git push` na glavno vejo se samodejno objavi.

## Domene na Vercelu

V projektu **Settings → Domains** dodajte:

1. `www.dobava.si` in `dobava.si` (Vercel ponudi preusmeritev `dobava.si` → `www.dobava.si`, sprejmite).
2. Vse prodajane domene: `agentwork.si`, `modelflow.si`, … (lahko tudi `www.` različice).

Za vsako domeno pri registrarju nastavite DNS, kot ga izpiše Vercel – običajno:

| Zapis | Ime | Vrednost |
|---|---|---|
| A | `@` | `76.76.21.21` |
| CNAME | `www` | `cname.vercel-dns.com` |

Certifikate HTTPS uredi Vercel sam. Preusmeritve na registrarju (URL forwarding) **niso potrebne** –
prodajane domene preusmeri `vercel.json`.

Če domene ne želite dodajati na Vercel, lahko namesto tega pri registrarju nastavite preusmeritev (301)
na `https://www.dobava.si/<domena>`.

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
