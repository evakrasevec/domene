# Domene na prodaj

Enotna stran »domena na prodaj« za vse naše `.si` domene. Ena sama statična datoteka (`index.html`), brez strežnika.

Stran sama prepozna, katera domena je bila obiskana, in jo prikaže v naslovu:

- po imenu gostitelja (če vse domene kažejo na isto gostovanje), ali
- po parametru `?d=` (če registrar domeno preusmeri, npr. `https://hub.example/?d=agentwork.si`).

Obiskovalec lahko pošlje ponudbo (odpre se e-poštni odjemalec s pripravljenim sporočilom), spodaj pa so navedene vse ostale domene. Stran je v slovenščini in angleščini.

## Nastavitev

V `index.html` na vrhu skripte uredite:

```js
const CONTACT_EMAIL = "prodaja@example.com";   // vaš e-naslov
const DOMAINS = [ ... ];                       // seznam domen
```

## Objava – dve možnosti

**A) Vse domene na isto gostovanje (priporočeno)**
Objavite repozitorij na Cloudflare Pages ali Netlify in tam vsako domeno dodajte kot »custom domain«. Pri registrarju za vsako domeno nastavite DNS zapise, ki jih ponudnik izpiše. Naslov v brskalniku ostane npr. `agentwork.si`.

**B) Preusmeritev pri registrarju**
Stran objavite na enem naslovu (npr. GitHub Pages), pri registrarju pa za vsako domeno nastavite preusmeritev (URL forwarding, 301) na:

```
https://<vaš-naslov>/?d=<domena>
```

npr. `https://<vaš-naslov>/?d=modelflow.si`.

## Domene

agentwork.si, agentworker.si, modelflow.si, cloude.si, agentish.si, arcee.si, gritt.si, ringg.si, featherless.si, lyrie.si, irisgo.si, overnight.si, findapp.si, mindcore.si, flowhub.si
