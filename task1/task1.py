from pathlib import Path

def total_salary(path):
    total_salary_amount = 0
    records_len = 0
    try:
        with open(path, "r", encoding="utf-8") as records:
            for record in records.readlines():
                salary = int(record.split(",")[1])
                total_salary_amount += salary
                records_len += 1
    except FileNotFoundError:
        print("File was not found. Try again please.")
        return (0, 0)
    except (IndexError, ValueError):
        print("File content has wrong format")
        return (0, 0)
    try:
        return (total_salary_amount, int(total_salary_amount / records_len))
    except ZeroDivisionError:
        print("There are no records in this file. Try another one please.")
        return (0, 0)

print(total_salary(Path(__file__).parent / "salaries.txt"))
print(total_salary("empty.txt"))
print(total_salary("wrong-format.txt"))
print(total_salary(Path(__file__).parent / "no-salaries.txt"))
print(total_salary("no_found_file.txt"))