# Hebe/HebeCE API Python

Unofficial API client for Dziennik VULCAN e-register from VULCAN. It's using the mobile API, imitates the eduVULCAN and
Dzienniczek VULCAN apps.

This library was created as an alternative to https://github.com/kapi2289/vulcan-api (and some things are based on this
library), which does not work with eduVULCAN accounts.

This library works:

- in schools where the *Dzienniczek VULCAN* app is used for all users,
- in schools where the *eduVULCAN* app is used for eduVULCAN account owners.

> Note: **It's not official API. In eduVULCAN it does not allow access to premium features without
a *Usługa Rozszerzona*. We are not responsible for the incorrect use of this library. This library may contain bugs.**

```sh
python3 -m pip install -r requirements.txt
```

See [docs](./docs/getting-started.md).