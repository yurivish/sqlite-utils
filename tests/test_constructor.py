from sqlite_utils import Database


def test_recursive_triggers():
    db = Database(memory=True)
    assert db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_recursive_triggers_off():
    db = Database(memory=True, recursive_triggers=False)
    assert not db.execute("PRAGMA recursive_triggers").fetchone()[0]


def test_memory_name():
    db1 = Database(memory_name="shared")
    db2 = Database(memory_name="shared")
    db1["dogs"].insert({"name": "Cleo"})
    assert list(db2["dogs"].rows) == [{"name": "Cleo"}]


def test_sqlite_version():
    db = Database(memory=True)
    version = db.sqlite_version
    assert isinstance(version, tuple)
    as_string = ".".join(map(str, version))
    actual = next(db.query("select sqlite_version() as v"))["v"]
    assert actual == as_string
