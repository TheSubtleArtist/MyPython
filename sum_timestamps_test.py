# sum_timestamps_test.py
import pytest
import csv
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Import the functions we're testing
from sum_timestamps import sum_track_times, main

class TestSumTrackTimes:
    """Tests for the sum_track_times function."""
    
    def test_simple_track_times(self, tmp_path):
        """Test with a simple CSV file containing multiple track times."""
        # Create a test CSV file with track times
        test_file = tmp_path / "tracks.csv"
        csv_content = """Title,Time
Song 1,3:45
Song 2,4:20
Song 3,2:15
Song 4,5:30"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 3:45 + 4:20 + 2:15 + 5:30 = 15:110 = 16:50
        assert result == "16:50"
    
    def test_empty_csv_file(self, tmp_path):
        """Test with an empty CSV file (header only)."""
        # Create a CSV file with only headers
        test_file = tmp_path / "empty_tracks.csv"
        csv_content = "Title,Time"
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        assert result == "0:00"
    
    def test_single_track(self, tmp_path):
        """Test with a CSV file containing a single track."""
        test_file = tmp_path / "single_track.csv"
        csv_content = """Title,Time
Only Song,3:42"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        assert result == "3:42"
    
    def test_times_with_seconds_overflow(self, tmp_path):
        """Test with times that cause seconds to overflow into minutes."""
        test_file = tmp_path / "overflow_tracks.csv"
        csv_content = """Title,Time
Song 1,2:45
Song 2,3:50
Song 3,1:35"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 2:45 + 3:50 + 1:35 = 6:130 = 8:10
        assert result == "8:10"
    
    def test_zero_minute_tracks(self, tmp_path):
        """Test with tracks that have zero minutes."""
        test_file = tmp_path / "short_tracks.csv"
        csv_content = """Title,Time
Short 1,0:30
Short 2,0:45
Short 3,0:25"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 0:30 + 0:45 + 0:25 = 0:100 = 1:40
        assert result == "1:40"
    
    def test_large_numbers(self, tmp_path):
        """Test with longer track times."""
        test_file = tmp_path / "long_tracks.csv"
        csv_content = """Title,Time
Epic Song,12:30
Another Long One,8:45
Medium Track,6:20"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 12:30 + 8:45 + 6:20 = 26:95 = 27:35
        assert result == "27:35"
    
    def test_exact_minute_boundaries(self, tmp_path):
        """Test with times that are exact minutes (no seconds)."""
        test_file = tmp_path / "exact_minutes.csv"
        csv_content = """Title,Time
Song 1,3:00
Song 2,5:00
Song 3,2:00"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        assert result == "10:00"

class TestSumTrackTimesErrorHandling:
    """Tests for error handling in sum_track_times function."""
    
    def test_file_not_found(self):
        """Test behavior when file doesn't exist."""
        with pytest.raises(FileNotFoundError):
            sum_track_times("nonexistent_file.csv")
    
    def test_invalid_time_format(self, tmp_path):
        """Test with invalid time format in CSV."""
        test_file = tmp_path / "invalid_format.csv"
        csv_content = """Title,Time
Bad Song,3-45"""  # Using dash instead of colon
        test_file.write_text(csv_content)
        
        with pytest.raises(ValueError):
            sum_track_times(test_file)
    
    def test_non_numeric_time_values(self, tmp_path):
        """Test with non-numeric time values."""
        test_file = tmp_path / "non_numeric.csv"
        csv_content = """Title,Time
Bad Song,a:b"""
        test_file.write_text(csv_content)
        
        with pytest.raises(ValueError):
            sum_track_times(test_file)
    
    def test_missing_time_column(self, tmp_path):
        """Test with CSV missing the Time column."""
        test_file = tmp_path / "no_time_column.csv"
        csv_content = """Title,Duration
Song 1,3:45"""
        test_file.write_text(csv_content)
        
        with pytest.raises(KeyError):
            sum_track_times(test_file)
    
    def test_malformed_csv(self, tmp_path):
        """Test with malformed CSV content."""
        test_file = tmp_path / "malformed.csv"
        csv_content = "This is not a valid CSV file"
        test_file.write_text(csv_content)
        
        # This should raise either KeyError or another CSV-related error
        with pytest.raises((KeyError, csv.Error)):
            sum_track_times(test_file)

class TestMainFunction:
    """Tests for the main function."""
    
    def test_main_function_integration(self, capsys, tmp_path, monkeypatch):
        """Test the main function with mocked command line arguments."""
        # Create a test CSV file
        test_file = tmp_path / "test_tracks.csv"
        csv_content = """Title,Time
Track 1,2:30
Track 2,3:15"""
        test_file.write_text(csv_content)
        
        # Mock sys.argv to simulate command line arguments
        test_args = ["sum_timestamps.py", str(test_file)]
        with patch('sys.argv', test_args):
            main()
        
        # Check the output
        captured = capsys.readouterr()
        assert captured.out.strip() == "5:45"
        assert captured.err == ""
    
    def test_main_with_pathlib_path(self, capsys, tmp_path, monkeypatch):
        """Test main function handles Path objects correctly."""
        # Create a test CSV file
        test_file = tmp_path / "path_test.csv"
        csv_content = """Title,Time
Song,1:30"""
        test_file.write_text(csv_content)
        
        # Mock sys.argv
        test_args = ["sum_timestamps.py", str(test_file)]
        with patch('sys.argv', test_args):
            main()
        
        captured = capsys.readouterr()
        assert captured.out.strip() == "1:30"

class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    def test_very_large_time_sum(self, tmp_path):
        """Test with times that sum to a very large value."""
        test_file = tmp_path / "large_sum.csv"
        csv_content = """Title,Time
Long 1,59:59
Long 2,59:59
Long 3,59:59"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 59:59 + 59:59 + 59:59 = 177:177 = 179:57
        assert result == "179:57"
    
    def test_maximum_seconds_boundary(self, tmp_path):
        """Test with exactly 59 seconds to verify boundary handling."""
        test_file = tmp_path / "boundary_test.csv"
        csv_content = """Title,Time
Song 1,1:59
Song 2,2:01"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        # Expected: 1:59 + 2:01 = 3:60 = 4:00
        assert result == "4:00"
    
    def test_csv_with_extra_columns(self, tmp_path):
        """Test CSV with additional columns beyond Title and Time."""
        test_file = tmp_path / "extra_columns.csv"
        csv_content = """Title,Artist,Time,Genre
Song 1,Artist 1,3:30,Rock
Song 2,Artist 2,4:15,Pop"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        assert result == "7:45"
    
    def test_csv_with_different_column_order(self, tmp_path):
        """Test CSV with columns in different order."""
        test_file = tmp_path / "different_order.csv"
        csv_content = """Time,Title
2:30,First Song
3:45,Second Song"""
        test_file.write_text(csv_content)
        
        result = sum_track_times(test_file)
        assert result == "6:15"

class TestParametrizedScenarios:
    """Parametrized tests for various scenarios."""
    
    @pytest.mark.parametrize("track_times,expected_result", [
        (["1:00", "2:00", "3:00"], "6:00"),
        (["0:30", "0:30"], "1:00"),
        (["5:45"], "5:45"),
        (["0:59", "0:01"], "1:00"),
        (["10:30", "5:45", "2:15"], "18:30"),
    ])
    def test_various_time_combinations(self, track_times, expected_result, tmp_path):
        """Test various combinations of track times."""
        test_file = tmp_path / "param_test.csv"
        
        # Build CSV content
        csv_lines = ["Title,Time"]
        for i, time in enumerate(track_times, 1):
            csv_lines.append(f"Song {i},{time}")
        
        test_file.write_text("\n".join(csv_lines))
        
        result = sum_track_times(test_file)
        assert result == expected_result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])