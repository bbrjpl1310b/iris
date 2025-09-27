# Getting started

## Generating a credential

```py
from iris.credentials import RsaCredential

credential = RsaCredential.create_new("Android", "SM-A525F")
```

## Registering the credential

When you have your credential, you need to register it. The registration method depends on the app. **After**
registering the credential, save it.

### Dzienniczek VULCAN

This application uses token (not jwt) and PIN registration. You can obtain this data in the *Dostęp mobilny* tab in the
*Uczeń* module in the web version of e-register.

> It is important to use `IrisHebeApi` instead of `IrisHebeCeApi`. The latter is intended for the eduVULCAN app.

```py
from iris.api import IrisHebeApi

api = IrisHebeApi(credential)

await api.register_by_token(security_token="<token>", pin="<pin>", tenant="<symbol>")
```

### eduVULCAN

The registration process in eduVULCAN is a little more complicated. You need to obtain jwt tokens (each for one
student).

At first you need to decode the jwt tokens. They should look like:

```js
{
  "name": "Jan Marek Kowalski (Fake123456)",
  "uid": "bdacb05d-f964-496d-9775-6f4cc26bf8e9",
  "tenant": "warszawa",
  "unituid": "3c000f77-bb3c-4514-8537-b9949b55c161",
  "uri": "http://uczen.eduvulcan.pl/warszawa/start?profil=bdacb05d-f964-496d-9775-6f4cc26bf8e9",
  "service": "False",
  "caps": [],
  "nbf": 0,
  "exp": 0,
  "iat": 0
}
```

And then register the credential:

> It is important to use `IrisHebeCeApi` instead of `IrisHebeApi`. The latter is intended for the Dzienniczek VULCAN
> app.

```py
from iris.api import IrisHebeCeApi

api = IrisHebeCeApi(credential)

await api.register_by_jwt(tokens=["<jwt>"], tenant="<tenant from jwt>")
```

### How does the eduVULCAN app obtain tokens?

> Note: This section describes how the eduVULCAN app does this (probably). It is not a recommendation on how you should
> do it. The implementation should comply with eduVULCAN ToS.

The app displays a web browser with the address https://eduvulcan.pl/api/ap. This redirects user to the eduVULCAN login
page. After logging in, the user is redirected to https://eduvulcan.pl/api/ap. The page will contain a hidden input (
`<input type="hidden" value="...">`). The input value should look like:

```json
{
  "Tokens": ["<jwt>"],
  "Alias": "<username>",
  "Email": "<email>",
  "EmailCandidate": null,
  "GivenName": "<frist name>",
  "Surname": "<last name>",
  "IsConsentAccepted": true,
  "CanAcceptConsent": true,
  "AccessToken": "<jwt>",
  "Capabilities": ["EMAIL_CONFIRMATION"],
  "Success": true,
  "ErrorMessage": null
}
```

> Note: App does not register when:
> 1. `Success` is `false`
> 2. `IsConsentAccepted` is `false`
> 3. `Tokens` is empty array

`AccessToken` allows using some parts of eduVULCAN site without logging in, eg. `/api/ap`. The app adds the
`Authorization` header to request:

```http
Authorization: <AccessToken> Bearer
```

## Getting account list

When you have the certificate, you can download the list of accounts. The account list contains data about the student,
school, journal and periods.

```py
accounts = await api.get_accounts()
```

## Serialization and deserialization the credential

### Serialization

```py
serialized = credential.model_dump_json()
```

### Deserialization

For RSA credentials:

```py
from iris.credentials import RSACredential

deserialized = RSACredential.model_validate_json(serialized)
```