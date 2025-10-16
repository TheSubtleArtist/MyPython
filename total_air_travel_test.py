# test_expense_calculator.py
import pytest
import csv
import tempfile
import os
import sys
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from io import StringIO
import logging

# Import the function we're testing
from total_air_travel_refactor import calculate_air_travel_expenses, main

# ==============================================================================
# 1. FIXTURES - Reusable Test Data and Setup
# ==============================================================================

@pytest.fixture
def sample_csv_data():
    """
    PYTEST FEATURE: Basic fixture
    BENEFIT: Reusable test data, consistent across tests
    STUDENT NOTE: Fixtures run before each test that uses them
    """
    return [
        {"Category": "Air Travel", "Cost": "$150.00", "Description": "Flight to NYC"},
        {"Category": "Hotel", "Cost": "$200.00", "Description": "Hotel stay"},
        {"Category": "Air Travel", "Cost": "$75.50", "Description": "Baggage fee"},
        {"Category": "Food", "Cost": "$45.00", "Description": "Dinner"},
        {"Category": "Air Travel", "Cost": "$300.25", "Description": "Return flight"},
    ]

@pytest.fixture
def csv_file_content(sample_csv_data):
    """
    PYTEST FEATURE: Fixture depending on another fixture
    BENEFIT: Build complex test data from simpler components
    STUDENT NOTE: pytest automatically handles fixture dependencies
    """
    # Convert list of dicts to CSV string
    if not sample_csv_data:
        return "Category,Cost,Description\n"
    
    fieldnames = sample_csv_data[0].keys()
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sample_csv_data)
    return output.getvalue()

@pytest.fixture
def temp_csv_file(csv_file_content, tmp_path):
    """
    PYTEST FEATURE: tmp_path fixture (built-in) + custom fixture combination
    BENEFIT: Automatic temporary file creation and cleanup
    STUDENT NOTE: tmp_path is a pytest built-in that creates temp directories
    """
    csv_file = tmp_path / "test_expenses.csv"
    csv_file.write_text(csv_file_content)
    return str(csv_file)

@pytest.fixture(scope="session")
def test_data_directory(tmp_path_factory):
    """
    PYTEST FEATURE: Session-scoped fixture with tmp_path_factory
    BENEFIT: Create shared resources once per test session
    STUDENT NOTE: scope="session" means this runs once for entire test session
    """
    temp_dir = tmp_path_factory.mktemp("test_data")
    return temp_dir

@pytest.fixture(autouse=True)
def reset_environment():
    """
    PYTEST FEATURE: autouse fixture
    BENEFIT: Automatically runs before every test without explicit declaration
    STUDENT NOTE: Good for cleanup or environment setup that every test needs
    """
    # Store original sys.argv
    original_argv = sys.argv.copy()
    yield  # This is where the test runs
    # Restore original sys.argv after test
    sys.argv = original_argv

@pytest.fixture(params=["utf-8", "utf-16", "latin-1"])
def csv_encoding(request):
    """
    PYTEST FEATURE: Parametrized fixture
    BENEFIT: Test the same functionality with different configurations
    STUDENT NOTE: request.param gives access to the current parameter value
    """
    return request.param

# ==============================================================================
# 2. PARAMETRIZED TESTS - Testing Multiple Scenarios
# ==============================================================================

class TestCalculateAirTravelExpenses:
    """
    PYTEST FEATURE: Test class organization
    BENEFIT: Group related tests together, share setup methods
    """

    @pytest.mark.parametrize("csv_data,expected_total", [
        # Test case 1: Normal data with multiple air travel entries
        ([
            {"Category": "Air Travel", "Cost": "$100.00", "Description": "Flight"},
            {"Category": "Hotel", "Cost": "$200.00", "Description": "Stay"},
            {"Category": "Air Travel", "Cost": "$50.50", "Description": "Baggage"},
        ], 150.50),
        
        # Test case 2: No air travel entries
        ([
            {"Category": "Hotel", "Cost": "$200.00", "Description": "Stay"},
            {"Category": "Food", "Cost": "$45.00", "Description": "Dinner"},
        ], 0.0),
        
        # Test case 3: Only air travel entries
        ([
            {"Category": "Air Travel", "Cost": "$300.00", "Description": "Flight 1"},
            {"Category": "Air Travel", "Cost": "$150.75", "Description": "Flight 2"},
        ], 450.75),
        
        # Test case 4: Empty file
        ([], 0.0),
    ])
    def test_various_csv_scenarios(self, csv_data, expected_total, tmp_path):
        """
        PYTEST FEATURE: @pytest.mark.parametrize decorator
        BENEFIT: Run same test logic with different input data
        STUDENT NOTE: Each parameter set becomes a separate test case
        """
        # Create CSV file with test data
        csv_file = tmp_path / "test.csv"
        
        if csv_data:
            fieldnames = csv_data[0].keys()
            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)
        else:
            # Empty file case
            csv_file.write_text("Category,Cost,Description\n")
        
        result = calculate_air_travel_expenses(str(csv_file))
        assert result == expected_total

    @pytest.mark.parametrize("cost_format,expected", [
        ("$100.00", 100.00),
        ("$50.50", 50.50),
        ("$1000.99", 1000.99),
        ("$0.01", 0.01),
    ])
    def test_cost_parsing(self, cost_format, expected, tmp_path):
        """
        PYTEST FEATURE: Focused parametrized testing
        BENEFIT: Test specific functionality (cost parsing) in isolation
        """
        csv_data = [{"Category": "Air Travel", "Cost": cost_format, "Description": "Test"}]
        csv_file = tmp_path / "test.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "Cost", "Description"])
            writer.writeheader()
            writer.writerows(csv_data)
        
        result = calculate_air_travel_expenses(str(csv_file))
        assert result == expected

# ==============================================================================
# 3. EXCEPTION TESTING AND ERROR HANDLING
# ==============================================================================

class TestErrorHandling:
    """Testing various error conditions and edge cases."""

    def test_file_not_found(self):
        """
        PYTEST FEATURE: Exception testing with pytest.raises
        BENEFIT: Verify proper error handling
        STUDENT NOTE: Context manager captures and validates exceptions
        """
        with pytest.raises(FileNotFoundError):
            calculate_air_travel_expenses("nonexistent_file.csv")

    def test_invalid_csv_format(self, tmp_path):
        """Test handling of malformed CSV files."""
        # Create invalid CSV
        invalid_csv = tmp_path / "invalid.csv"
        invalid_csv.write_text("This is not a valid CSV file")
        
        with pytest.raises(KeyError):
            calculate_air_travel_expenses(str(invalid_csv))

    def test_missing_cost_column(self, tmp_path):
        """Test CSV missing required Cost column."""
        csv_file = tmp_path / "no_cost.csv"
        csv_file.write_text("Category,Description\nAir Travel,Flight\n")
        
        with pytest.raises(KeyError, match="Cost"):
            calculate_air_travel_expenses(str(csv_file))

    def test_invalid_cost_format(self, tmp_path):
        """
        PYTEST FEATURE: Exception matching with regex
        BENEFIT: Verify specific error messages
        """
        csv_data = [{"Category": "Air Travel", "Cost": "invalid", "Description": "Test"}]
        csv_file = tmp_path / "test.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "Cost", "Description"])
            writer.writeheader()
            writer.writerows(csv_data)
        
        with pytest.raises(ValueError, match="could not convert string to float"):
            calculate_air_travel_expenses(str(csv_file))

# ==============================================================================
# 4. MOCKING AND PATCHING
# ==============================================================================

class TestMockingExamples:
    """Demonstrate various mocking techniques."""

    @patch('builtins.open')
    def test_file_operations_mocked(self, mock_open_func):
        """
        PYTEST FEATURE: @patch decorator for mocking
        BENEFIT: Test without actual file I/O, control return values
        STUDENT NOTE: mock_open is a special mock for file operations
        """
        # Set up mock file content
        mock_file_content = "Category,Cost,Description\nAir Travel,$100.00,Flight\n"
        mock_open_func.return_value.__enter__.return_value = StringIO(mock_file_content)
        
        result = calculate_air_travel_expenses("fake_file.csv")
        assert result == 100.00
        mock_open_func.assert_called_once_with("fake_file.csv")

    @patch('csv.DictReader')
    def test_csv_reader_mocked(self, mock_dict_reader):
        """
        PYTEST FEATURE: Mocking specific modules/functions
        BENEFIT: Control exactly what the CSV reader returns
        """
        # Mock CSV reader to return specific data
        mock_dict_reader.return_value = [
            {"Category": "Air Travel", "Cost": "$200.00", "Description": "Test flight"}
        ]
        
        with patch('builtins.open', mock_open()):
            result = calculate_air_travel_expenses("fake.csv")
        
        assert result == 200.00
        mock_dict_reader.assert_called_once()

    def test_main_function_with_mocking(self, capsys, monkeypatch):
        """
        PYTEST FEATURE: monkeypatch fixture + capsys
        BENEFIT: Test command-line interface without actual command line
        STUDENT NOTE: monkeypatch is pytest's built-in mocking utility
        """
        # Mock sys.argv
        test_args = ["script_name", "test.csv"]
        monkeypatch.setattr(sys, 'argv', test_args)
        
        # Mock the calculate function
        mock_total = 525.75
        monkeypatch.setattr(
            'total_air_travel_refactor.calculate_air_travel_expenses', 
            lambda x: mock_total
        )
        
        # Run main function
        main()
        
        # Check output
        captured = capsys.readouterr()
        assert captured.out == "Total air travel expenses: $525.75\n"

# ==============================================================================
# 5. CUSTOM MARKERS AND TEST CATEGORIZATION
# ==============================================================================

@pytest.mark.integration
class TestIntegrationScenarios:
    """
    PYTEST FEATURE: Custom markers
    BENEFIT: Categorize tests, run specific test types
    STUDENT NOTE: Run with: pytest -m integration
    """

    @pytest.mark.slow
    def test_large_csv_file(self, tmp_path):
        """
        PYTEST FEATURE: Multiple markers on one test
        BENEFIT: Tag tests with multiple categories
        STUDENT NOTE: Run with: pytest -m "integration and slow"
        """
        # Create large CSV file
        csv_file = tmp_path / "large.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "Cost", "Description"])
            writer.writeheader()
            
            # Write 1,000 rows (reduced for demo)
            for i in range(1000):
                category = "Air Travel" if i % 3 == 0 else "Other"
                cost = f"${i + 1}.00"
                writer.writerow({
                    "Category": category, 
                    "Cost": cost, 
                    "Description": f"Item {i}"
                })
        
        result = calculate_air_travel_expenses(str(csv_file))
        # Calculate expected total (sum of 1, 4, 7, 10, ... up to appropriate number)
        expected = sum(i + 1 for i in range(1000) if i % 3 == 0)
        assert result == expected

    @pytest.mark.edge_case
    def test_unicode_csv_content(self, tmp_path):
        """
        PYTEST FEATURE: Custom marker for edge cases
        BENEFIT: Easy to run just edge case tests
        """
        csv_data = [
            {"Category": "Air Travel", "Cost": "$100.00", "Description": "Flight to café"},
            {"Category": "Hôtel", "Cost": "$200.00", "Description": "Stay at hôtel"},
            {"Category": "Air Travel", "Cost": "$50.50", "Description": "Ñoño baggage"},
        ]
        
        csv_file = tmp_path / "unicode.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "Cost", "Description"])
            writer.writeheader()
            writer.writerows(csv_data)
        
        result = calculate_air_travel_expenses(str(csv_file))
        assert result == 150.50

# ==============================================================================
# 6. CONDITIONAL TESTING AND SKIPPING
# ==============================================================================

class TestConditionalScenarios:
    """Demonstrate conditional test execution."""

    @pytest.mark.skipif(sys.version_info < (3, 9), reason="Requires Python 3.9+ for removeprefix")
    def test_removeprefix_functionality(self, tmp_path):
        """
        PYTEST FEATURE: Conditional test skipping
        BENEFIT: Skip tests based on environment conditions
        STUDENT NOTE: Test only runs on Python 3.9+
        """
        csv_data = [{"Category": "Air Travel", "Cost": "$100.00", "Description": "Test"}]
        csv_file = tmp_path / "test.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Category", "Cost", "Description"])
            writer.writeheader()
            writer.writerows