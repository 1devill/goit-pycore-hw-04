from pathlib import Path

def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as records:
            for record in records.readlines():
                id, name, age = record.split(",")
                cat = {}
                cat["id"] = id.strip()
                cat["name"] = name.strip()
                cat["age"] = age.strip()
                cats.append(cat)
    except FileNotFoundError:
        print("File was not found. Try again please.")
        return cats
    except (IndexError, ValueError):
        print("File content has wrong format")
        return cats
    return cats

print(get_cats_info(Path(__file__).parent / "cats.txt"))
print(get_cats_info("wrong-format.txt"))
print(get_cats_info("empty.txt"))
print(get_cats_info("not-found.txt"))