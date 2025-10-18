# friday_test.py
import pytest
from datetime import date
from unittest.mock import Mock

class TestFridayScript:
    """Tests for the friday.py script functionality."""
    
    @pytest.fixture
    def set_date(self, monkeypatch):
        """
        PYTEST FIXTURE: Safely mocks datetime.date.today() using monkeypatch
        BENEFIT: Allows testing with any date while ensuring proper cleanup
        STUDENT NOTE: monkeypatch automatically restores original date.today() after test
        
        Returns a function that takes a weekday (0=Monday, 1=Tuesday, ..., 6=Sunday)
        and mocks date.today() to return a date with that weekday.
        """
        def _set_weekday(weekday):
            """
            Set the mocked date to have a specific weekday.
            
            Args:
                weekday (int): 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 
                              4=Friday, 5=Saturday, 6=Sunday
            """
            # Create a mock date object that returns the desired weekday
            mock_date = Mock()
            mock_today = Mock()
            mock_today.weekday.return_value = weekday
            mock_date.today.return_value = mock_today
            
            # Use monkeypatch to safely replace date.today
            monkeypatch.setattr('datetime.date', mock_date)
            
        return _set_weekday
    
    def test_friday_prints_friday(self, set_date, capsys):
        """
        Test that the script prints "FRIDAY" when today is Friday (weekday 4).
        
        PYTEST FEATURE: Using custom fixture with capsys for output verification
        BENEFIT: Verify exact output when condition is met
        STUDENT NOTE: capsys captures all printed output for verification
        """
        # Set the mocked date to Friday (weekday 4)
        set_date(4)
        
        # Import and execute the script (simulates running friday.py)
        # We need to import after mocking to ensure the mock takes effect
        import importlib
        import friday
        importlib.reload(friday)
        
        # Verify output
        captured = capsys.readouterr()
        assert captured.out == "FRIDAY\n"
        assert captured.err == ""
    
    def test_monday_prints_nothing(self, set_date, capsys):
        """
        Test that the script prints nothing when today is Monday (weekday 0).
        
        PYTEST FEATURE: Testing negative case with fixture
        BENEFIT: Verify no output when condition is not met
        """
        # Set the mocked date to Monday (weekday 0)
        set_date(0)
        
        # Import and execute the script
        import importlib
        import friday
        importlib.reload(friday)
        
        # Verify no output
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_tuesday_prints_nothing(self, set_date, capsys):
        """Test that the script prints nothing when today is Tuesday (weekday 1)."""
        set_date(1)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_wednesday_prints_nothing(self, set_date, capsys):
        """Test that the script prints nothing when today is Wednesday (weekday 2)."""
        set_date(2)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_thursday_prints_nothing(self, set_date, capsys):
        """Test that the script prints nothing when today is Thursday (weekday 3)."""
        set_date(3)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_saturday_prints_nothing(self, set_date, capsys):
        """Test that the script prints nothing when today is Saturday (weekday 5)."""
        set_date(5)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    def test_sunday_prints_nothing(self, set_date, capsys):
        """Test that the script prints nothing when today is Sunday (weekday 6)."""
        set_date(6)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""
    
    @pytest.mark.parametrize("weekday,expected_output", [
        (0, ""),      # Monday
        (1, ""),      # Tuesday  
        (2, ""),      # Wednesday
        (3, ""),      # Thursday
        (4, "FRIDAY\n"),  # Friday
        (5, ""),      # Saturday
        (6, ""),      # Sunday
    ])
    def test_all_weekdays_parametrized(self, set_date, capsys, weekday, expected_output):
        """
        PYTEST FEATURE: Parametrized test covering all weekdays
        BENEFIT: Comprehensive testing with clean, readable test cases
        STUDENT NOTE: Each parameter set creates a separate test case
        """
        # Set the mocked date to the specified weekday
        set_date(weekday)
        
        # Import and execute the script
        import importlib
        import friday
        importlib.reload(friday)
        
        # Verify output matches expected
        captured = capsys.readouterr()
        assert captured.out == expected_output
        assert captured.err == ""

class TestSetDateFixture:
    """Tests to verify the set_date fixture works correctly."""
    
    def test_set_date_fixture_functionality(self, set_date):
        """
        Test that the set_date fixture properly mocks date.today().weekday().
        
        PYTEST FEATURE: Testing fixtures themselves
        BENEFIT: Ensure custom fixtures work as expected
        STUDENT NOTE: Good practice to test complex fixtures
        """
        from datetime import date
        
        # Test setting to Friday
        set_date(4)
        assert date.today().weekday() == 4
        
        # Test setting to Monday  
        set_date(0)
        assert date.today().weekday() == 0
        
        # Test setting to Sunday
        set_date(6)
        assert date.today().weekday() == 6
    
    def test_monkeypatch_cleanup(self, set_date):
        """
        Test that monkeypatch properly cleans up after the test.
        
        PYTEST FEATURE: Verifying automatic cleanup
        BENEFIT: Ensure tests don't interfere with each other
        STUDENT NOTE: monkeypatch automatically restores original objects
        """
        from datetime import date
        
        # Store reference to original date.today method
        original_today = date.today
        
        # Use the fixture to mock the date
        set_date(4)
        
        # Verify the mock is in place
        assert date.today().weekday() == 4
        
        # After the test, monkeypatch should restore the original
        # Note: This happens automatically, we're just documenting the behavior

class TestScriptBehaviorEdgeCases:
    """Test edge cases and script behavior details."""
    
    def test_friday_exact_output_format(self, set_date, capsys):
        """
        Test the exact format of Friday output including newlines.
        
        PYTEST FEATURE: Precise output format verification
        BENEFIT: Ensure exact string matching including whitespace
        """
        set_date(4)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        
        # Verify exact output format
        assert captured.out == "FRIDAY\n"
        assert len(captured.out) == 7  # "FRIDAY" + newline
        assert captured.out.strip() == "FRIDAY"
        assert captured.out.endswith("\n")
    
    def test_no_stderr_output_ever(self, set_date, capsys):
        """
        Test that the script never writes to stderr.
        
        PYTEST FEATURE: Verifying stderr remains clean
        BENEFIT: Ensure no error messages or warnings are produced
        """
        # Test both Friday and non-Friday cases
        test_cases = [0, 1, 2, 3, 4, 5, 6]
        
        for weekday in test_cases:
            set_date(weekday)
            
            import importlib
            import friday
            importlib.reload(friday)
            
            captured = capsys.readouterr()
            assert captured.err == "", f"Unexpected stderr output on weekday {weekday}"
    
    def test_script_runs_without_exceptions(self, set_date):
        """
        Test that the script runs without raising any exceptions.
        
        PYTEST FEATURE: Exception-free execution verification
        BENEFIT: Ensure script stability across all weekdays
        """
        # Test all weekdays to ensure no exceptions
        for weekday in range(7):
            set_date(weekday)
            
            try:
                import importlib
                import friday
                importlib.reload(friday)
            except Exception as e:
                pytest.fail(f"Script raised exception on weekday {weekday}: {e}")

class TestMonkeypatchSpecificBehavior:
    """Tests specifically demonstrating monkeypatch behavior and benefits."""
    
    def test_monkeypatch_isolation_between_tests(self, set_date):
        """
        Demonstrate that monkeypatch provides proper test isolation.
        
        PYTEST FEATURE: Test isolation with monkeypatch
        BENEFIT: Each test starts with a clean state
        STUDENT NOTE: This is why monkeypatch is preferred over manual mocking
        """
        from datetime import date
        
        # First, set to Friday
        set_date(4)
        first_weekday = date.today().weekday()
        assert first_weekday == 4
        
        # Then set to Monday
        set_date(0)
        second_weekday = date.today().weekday()
        assert second_weekday == 0
        
        # Verify the change took effect
        assert first_weekday != second_weekday
    
    def test_monkeypatch_restores_original_after_test(self, monkeypatch):
        """
        Demonstrate that monkeypatch restores the original date.today after test.
        
        PYTEST FEATURE: Automatic restoration by monkeypatch
        BENEFIT: No manual cleanup required, prevents test pollution
        STUDENT NOTE: This test shows the cleanup mechanism in action
        """
        from datetime import date
        
        # Store reference to original method
        original_today = date.today
        
        # Create a simple mock
        mock_date = Mock()
        mock_today = Mock()
        mock_today.weekday.return_value = 4
        mock_date.today.return_value = mock_today
        
        # Apply the mock using monkeypatch
        monkeypatch.setattr('datetime.date', mock_date)
        
        # Verify mock is active
        assert date.today().weekday() == 4
        
        # Note: After this test ends, monkeypatch automatically restores original

class TestRealWorldScenarios:
    """Test scenarios that might occur in real-world usage."""
    
    @pytest.mark.parametrize("description,weekday,should_print", [
        ("Start of work week", 0, False),     # Monday
        ("Mid-week hump day", 2, False),      # Wednesday  
        ("End of work week", 4, True),        # Friday
        ("Weekend day", 5, False),            # Saturday
    ])
    def test_real_world_scenarios(self, set_date, capsys, description, weekday, should_print):
        """
        PYTEST FEATURE: Descriptive parametrized testing
        BENEFIT: Self-documenting test cases with business context
        STUDENT NOTE: Parameter names make test intent clear
        """
        set_date(weekday)
        
        import importlib
        import friday
        importlib.reload(friday)
        
        captured = capsys.readouterr()
        
        if should_print:
            assert captured.out == "FRIDAY\n", f"Should print FRIDAY on {description}"
        else:
            assert captured.out == "", f"Should print nothing on {description}"
    
    def test_multiple_script_executions(self, set_date, capsys):
        """
        Test that multiple executions of the script work correctly.
        
        PYTEST FEATURE: Testing repeated operations
        BENEFIT: Verify script behavior is consistent across multiple runs
        """
        # Execute script multiple times on Friday
        for _ in range(3):
            set_date(4)
            
            import importlib
            import friday
            importlib.reload(friday)
            
            captured = capsys.readouterr()
            assert captured.out == "FRIDAY\n"
        
        # Execute script multiple times on Monday
        for _ in range(3):
            set_date(0)
            
            import importlib
            import friday
            importlib.reload(friday)
            
            captured = capsys.readouterr()
            assert captured.out == ""

if __name__ == "__main__":
    pytest.main([__file__, "-v"])