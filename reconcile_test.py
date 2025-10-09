import csv
import tempfile
import os
from reconcile import reconcile_transactions


def test_reconcile_amount_change():
    """Test case where transaction amounts changed: 50.00 → 49.99"""
    # Create temporary CSV files
    file1_data = [
        ["Date", "Dept", "Amount", "Payee"],
        ["2000-12-05", "Engineering", "50.00", "Zapier"]
    ]
    file2_data = [
        ["Date", "Dept", "Amount", "Payee"],
        ["2000-12-05", "Engineering", "49.99", "Zapier"]
    ]

    # Write to temporary files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
        writer = csv.writer(f1)
        writer.writerows(file1_data)
        file1_path = f1.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
        writer = csv.writer(f2)
        writer.writerows(file2_data)
        file2_path = f2.name

    try:
        removed, added, differences = reconcile_transactions(file1_path, file2_path)

        # Should detect this as an amount change, not separate add/remove
        assert len(differences) == 1
        assert len(removed) == 0
        assert len(added) == 0
    finally:
        # Clean up temporary files
        os.unlink(file1_path)
        os.unlink(file2_path)