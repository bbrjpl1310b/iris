# Basic usage

## Initializing API

For eduVULCAN:

```py
from iris.api import IrisHebeCeApi

api = IrisHebeCeApi(your_credential)
```

For Dzienniczek VULCAN:

```py
from iris.api import IrisHebeApi

api = IrisHebeApi(your_credential)
```

## Basic api functions

Fetching account list:

```py
accounts = await api.get_accounts()
```

Fetching lucky number:

```py
lucky = await api.get_lucky_number(
    rest_url=account.unit.rest_url,
    pupil_id=account.pupil.id,
    constituent_unit_id=account.constituent_unit.id
)
```

Fetching grades:

```py
grades = await api.get_grades(
    rest_url=account.unit.rest_url,
    unit_id=account.unit.id,
    pupil_id=account.pupil.id,
    period_id=account.periods[-1].id,
)
```

Fetching exams:

```py
from datetime import date

exams = await api.get_exams(
    rest_url=account.unit.rest_url,
    pupil_id=account.pupil.id,
    date_from=date(2020, 9, 1),
    date_to=date(2020, 9, 7)
)
```

