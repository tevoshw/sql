# SQL Cheat Sheet

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