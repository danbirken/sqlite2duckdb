# sqlite2duckdb-native

A tool for converting a [sqlite](https://www.sqlite.org/) database into a [duckdb](https://duckdb.org/) database


## Description 

Sqlite is an embedded online database designed for transactional reading and writing.
Duckdb is also an embedded database, but column-oriented, designed for analytical process with a very high reading efficiency.

For more details [https://towardsdatascience.com/forget-about-sqlite-use-duckdb-instead-and-thank-me-later-df76ee9bb777](https://towardsdatascience.com/forget-about-sqlite-use-duckdb-instead-and-thank-me-later-df76ee9bb777)

Uses the native "COPY" statement in duckdb, which preserves constraints

## Installation 

```
pip install sqlite2duckdb-native
```

## Usage 

### As a command line 

```

usage: sqlite2duckdb <sqlite_path> <duckdb_path>

Convert Sqlite database to Duckdb database

positional arguments:
  sqlite_path    sqlite file path
  duckdb_path    duckdb file path

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit


```

### Examples 

```bash
sqlite2duckdb source.db target.db
```

### From python 

```python

from sqlite2duckdb  import sqlite_to_duckdb
sqlite_to_duckdb("source.sqlite", "target.duckdb")

```
