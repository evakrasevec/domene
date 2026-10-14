# Domene na prodaj – dobava.si

Enotna stran za prodajo naših `.si` domen na **https://www.dobava.si**. Vsaka domena ima svojo podstran:

- `https://www.dobava.si/` – seznam vseh domen
- `https://www.dobava.si/agentwork.si` – stran posamezne domene (ime in obrazec za ponudbo)

Vsako prodajano domeno pri registrarju preusmerite na njeno podstran (glej spodaj).
Stran je statična (brez strežnika), v slovenščini in angleščini. Ponudbe pridejo po e-pošti.

## Nastavitev

V `index.html` na vrhu skripte uredite:

```js
const CONTACT_EMAIL = "info@digihelp.si";      // kam pridejo ponudbe
const DOMAINS = [ ... ];                       // seznam domen (brez cen)
```

## Kako deluje

- `index.html` – celotna stran (seznam domen, obrazec za ponudbe). Nič ni treba gradit.
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

## Ponudbe

Cene na strani niso objavljene. Kupci oddajo ponudbo (znesek v EUR) prek obrazca, ki odpre
e-pošto na `CONTACT_EMAIL`. Ko se dogovorite, kupcu izstavite predračun ali uporabite posrednika
(npr. Escrow.com), po plačilu pa mu pošljete **kodo za prenos (AuthInfo)** od registrarja.
Ko je domena prodana, jo odstranite s seznama `DOMAINS`.

## Domene

agentwork.si, agentworker.si, modelflow.si, agentish.si, gritt.si, ringg.si, lyrie.si, irisgo.si, overnight.si, findapp.si, mindcore.si, flowhub.si
