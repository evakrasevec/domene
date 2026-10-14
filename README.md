# Domene na prodaj

Enotna stran »domena na prodaj« za vse naše `.si` domene. Ena sama statična datoteka (`index.html`), brez strežnika.

Stran sama prepozna, katera domena je bila obiskana, in jo prikaže v naslovu:

- po imenu gostitelja (če vse domene kažejo na isto gostovanje), ali
- po parametru `?d=` (če registrar domeno preusmeri, npr. `https://<ime>.replit.app/?d=agentwork.si`).

Prodajo ureja DigiHelp (digihelp.si). Obiskovalec lahko pošlje ponudbo na info@digihelp.si (odpre se e-poštni odjemalec s pripravljenim sporočilom), spodaj pa so navedene vse ostale domene. Stran je v slovenščini in angleščini.

## Nastavitev

V `index.html` na vrhu skripte uredite:

```js
const CONTACT_EMAIL = "info@digihelp.si";      // kam pridejo ponudbe
const DOMAINS = [ ... ];                       // seznam domen
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
na Replit povežete samo eno domeno (npr. `domene.digihelp.si` ali `<ime>.replit.app`),
pri registrarju pa za vsako ostalo domeno nastavite preusmeritev (URL forwarding, 301) na:

```
https://<vaš-naslov>/?d=<domena>
```

npr. `https://<ime>.replit.app/?d=modelflow.si`. Stran bo prikazala `modelflow.si`.

## Domene

agentwork.si, agentworker.si, modelflow.si, cloude.si, agentish.si, arcee.si, gritt.si, ringg.si, featherless.si, lyrie.si, irisgo.si, overnight.si, findapp.si, mindcore.si, flowhub.si
