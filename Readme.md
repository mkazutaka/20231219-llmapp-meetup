# はじめかた

### Version

```
Python 3.10.4
Poetry (version 1.4.2)
```

### Required

- Install

```
poetry shell
poetry install
```

- get Data

```
mkdir -p data

# download https://www.jcci.or.jp/chusho/202203invoice_booklet.pdf
# and save it to data/invoice.pdf
```

### Run

```
export OPENAI_API_KEY=<your key>
poetry run python app/bench.py
```
