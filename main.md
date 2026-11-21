# SQL Cheat Sheet

## CREATE

Creates a table. The table starts empty. Rows are added later with `INSERT`.

```sql
CREATE TABLE IF NOT EXISTS <name> (
    <column> <type> <constraints>
);
```

`IF NOT EXISTS` makes the statement safe to run again. Without it, a second run fails because the table already exists. With it, SQLite skips creation when that name is already taken.

A column can have more than one constraint. Write them on the same line, after the type.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER CHECK (age >= 0),
    active INTEGER NOT NULL DEFAULT 1
);
```

### Types

SQLite stores a value in a storage class and tries to match the declared type. `VARCHAR(255)` is stored as `TEXT`. The `255` does not limit the length.

| Type | Stores | Also written as |
|------|--------|-----------------|
| `INTEGER` | Whole number | `INT`, `BIGINT` |
| `REAL` | Decimal number | `FLOAT`, `DOUBLE` |
| `TEXT` | Text | `VARCHAR`, `CHAR` |
| `BLOB` | Raw bytes (files, images) | |
| `NUMERIC` | A number, or an integer when it fits | `BOOLEAN`, `DECIMAL`, `DATE` |

`NULL` is not a column type. It means "no value".

### Constraints

Rules the column must follow. A column can combine several of them.

| Constraint | What it requires |
|------------|------------------|
| `PRIMARY KEY` | Identifies the row. Unique and never null. One per table. |
| `AUTOINCREMENT` | Only with `INTEGER PRIMARY KEY`. The database picks the next number and does not reuse deleted ids. |
| `NOT NULL` | The column must receive a value. |
| `UNIQUE` | That value can appear only once in the column. |
| `DEFAULT <value>` | Value used when `INSERT` omits the column. |
| `CHECK (<condition>)` | The row is saved only when the condition is true. |
| `FOREIGN KEY` | The value must exist in the referenced column of another table. |

`PRIMARY KEY` already means unique and not null, so those two do not need to be repeated on it.

`UNIQUE` allows several `NULL`s. `NULL` is not equal to another `NULL`.

Usual order on a column: type, then `PRIMARY KEY` or `UNIQUE`, then `NOT NULL`, then `DEFAULT`, then `CHECK`.


## SELECT

Chooses which columns to show.

```sql
SELECT <columns> FROM <table>;
```

```sql
SELECT name FROM demo;
```

---

## WHERE

Filters rows by a condition.

```sql
SELECT <columns> FROM <table> WHERE <conditions>;
```

```sql
SELECT name FROM demo WHERE name = 'DELETE';
SELECT name FROM demo WHERE name = 'DELETE' AND x = 1;
```

| I want...         | Use                |
|-------------------|--------------------|
| equal to          | `=`                |
| different from    | `!=` or `<>`       |
| greater / less    | `>` `<` `>=` `<=`  |
| both conditions   | `AND`              |
| one or the other  | `OR`               |
| in a list         | `IN (...)`         |
| in a range        | `BETWEEN a AND b`  |
| contains text     | `LIKE '%text%'`    |
| is empty          | `IS NULL`          |
| invert            | `NOT`              |

---

## ORDER BY

Sorts the result.

- Default (`ASC`): smallest → largest
- `DESC`: largest → smallest

```sql
ORDER BY <column>
ORDER BY <column> DESC
```

---

## LIMIT

Sets how many rows to return.

```sql
LIMIT <amount>
```

---

## Aggregate Functions

| Function | What it does        |
|----------|---------------------|
| `COUNT`  | Counts rows         |
| `SUM`    | Sums values         |
| `AVG`    | Average             |
| `MIN`    | Minimum             |
| `MAX`    | Maximum             |

```sql
SELECT COUNT(*) FROM <table>;
```