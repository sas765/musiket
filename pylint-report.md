# Pylint report

Pylint returns the following report for this program:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:143:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:149:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:178:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:197:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:228:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:228:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:252:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:262:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:271:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:294:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:310:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:336:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:351:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:351:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:368:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:368:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:385:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:392:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:420:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:420:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:442:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:21:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module entries
entries.py:1:0: C0114: Missing module docstring (missing-module-docstring)
entries.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:134:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:141:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:148:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:161:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:166:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:171:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:175:0: C0116: Missing function or method docstring (missing-function-docstring)
entries.py:179:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.55/10 (previous run: 8.53/10, +0.02)
```

Let's go through the report and reason why these remarks don't need our immediate attention:

## Docstring comments

Most of the remarks in the report are of the following types:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
```

These remarks note that the program's modules and functions don't have docstring comments. It has been decided that docstring comments won't be utilised in the development of this program.

## Missing return statement

The report contains the following remarks concerning functions' return values:

```
app.py:228:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:351:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:368:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:420:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

These concern cases where the function handles methods `GET` and `POST`, ignoring other methods. The first remark for example points to the following function:

```python
@app.route("/remove_entry/<int:entry_id>", methods=["GET", "POST"])
def remove_entry(entry_id):
    require_login()

    if request.method == "GET":
        entry = entries.get_entry(entry_id)
        if not entry:
            abort(404)
        if entry["user_id"] != session["user_id"]:
            abort(403)
        return render_template("remove_entry.html", entry=entry)

    if request.method == "POST":
        if "remove" in request.form:
            entry = entries.get_entry(entry_id)
            csrf_token = request.form["csrf_token"]
            check_csrf(csrf_token)
            if not entry:
                abort(404)
            check_user(entry["user_id"])
            entries.remove_entry(entry_id)
            return redirect("/")
        return redirect("/entry/" + str(entry_id))
```

Here the function returns a value when `request.method` is `GET` or `POST`, but there exists a theoretical situation where `request.method` is something beyond these two options, resulting in the function not returning a value. In practice however, this situation is not possible, since the function's decorator has a requirement for the method to be either `GET` or `POST`. Thus, there is no risk for the function to not return a value.

## Constant name

The report contains the following remark concerning the name of a constant:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

Here the name of a variable defined on the main level of the code is interpreted to be a constant that should be written with capitalised lettering. In the view of the developer of this program it looks more appropriate in lowercase. The variable is used as follows:

```python
app.secret_key = config.secret_key
```

## Dangerous default value

The report contains the following remarks concerning a dangerous default value:

```
db.py:11:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:21:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

The first remark for example points to the following function:

```python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```

Here the parameter default value `[]` is an empty list. A theoretical problem following this could be that the same list might be shared by all calls to the function, resulting in the possibility of other functions also getting affected by a possible change to the list. In practice this isn't possible, since the code doesn't manipulate the list object.