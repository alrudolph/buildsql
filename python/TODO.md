# not really an orm but a sql builder -- need better name to match
> BECAUSE THINGS ARE PARSED OUT I CAN GENERATE EVEN MORE METADATA
    * I know the root table name
    * I can know whether its select or insert
    * can generate summary (get user by id) | (select orders) etc... allow people to custom override?
> Typing for Limit 1 to be retruning 1 item, otherwise select. `.require()` or something for `get` vs `find`

1. orders
2. joins
3. inserts
4. 



```python
(
    select("")
    .select_distinct("name")
    .distinct_on("name") # cols to be on, remaining cols
    .from_("table_name")
    .left_join("some table name", on="on part")
    .left_join("table_b", on="table_a.id = table_b.a_id")
    .right_join("table_c", on="...")
    .inner_join("table_d", on="...")
    .full_join("table_e", on="...")
    .cross_join("table_f")
    # LATERAL JOIN
    .where("some clause")
    .group_by("a")
    .having("count(*) > 5")
)
```

* Window functions, int("count(*)").gt(5) <--- some sort of this thing?
* alias - `as_`

```python
users_cte = (
    select("id", "email")
    .from_("users")
    .where("active = true")
    .as_cte("active_users")
)

(
    with_(users_cte)
    .select("*")
    .from_("active_users")
)
```

```python
(
    insert("user_id", "name", "email")
    .into("users")
    .values(123, "Alex", "alex@voker.ai")
    .on_conflict("user_id")
    .do_update_set(
        "name = EXCLUDED.name",
        "email = EXCLUDED.email",
    )
    .returning("*")
    .do_nothing()
)
```

```
.insert_into("archive")
.from_select(
    select("id", "email").from_("users").where("deleted = true")
)
```

```
(
    update("users")
    .set(name="Alex", email="alex@ai.com")
)
```

```
(
    delete_from("users")
    .where("inactive = true")
    .returning("id")
)
```


Be able to do `and` or `or`, equals not equals, greater than, less than, ge, le, datetime stuff?

```
.union_all(q3)
.intersect(q4)
```


Need create table, create schema, etc... (and the columns?)












```
type Builder[T] interface {

    build() T;

}

type Buildable[T] = T | Builder[T];

type execute template {

    fn build;

}

type limit_or_terminal template {

    limit(limit Buildable[int]) {

        ...execute;

    }

    ...execute;

}

type where_or_terminal template {

    where(clause Buildable[string]) {

        ...limit_or_terminal;

    }

    ...limit_or_terminal;

}

Query {

    select(columns ...Buildable[string]) {

        from_(source Buildable[string]) {

            ...where_or_terminal;

        }

    }

}
```

> Just have my builder stuff create a string and then use sqlalchemy for to just execute the raw string
