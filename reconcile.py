import csv

def reconcile_transactions(file1, file2):
    breakpoint()
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        header1 = next(reader1)
        header2 = next(reader2)

        if header1 != header2:
            raise ValueError("Headers do not match.")

        transactions1 = set(tuple(row) for row in reader1)
        transactions2 = set(tuple(row) for row in reader2)

        removed = transactions1 - transactions2
        added = transactions2 - transactions1

        differences = []
        for t1 in transactions1:
            for t2 in transactions2:
                if t1[:3] == t2[:3] and t1[3] != t2[3] # <--Calls the wrong values. Programmer failed to start reading the tuple from the zero position
                    differences.append(f"Amount mismatch: {t1} vs. {t2}")

        return list(removed), list(added), differences