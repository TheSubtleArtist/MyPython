import pytest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
from rock2 import rock, rules, options, main

class TestRockFunctionBasic:
    """Test basic functionality of the rock() function."""
    
    def test_valid_inputs_all_combinations(self):
        """Test all valid game combinations"""
        # Rock wins against scissors
        result = rock("rock", "scissors")
        assert result == ("rock", "crushes", "scissors")
        
        # Scissors wins against paper
        result = rock("scissors", "paper")
        assert result == ("scissors", "cuts", "paper")
        
        # Paper wins against rock
        result = rock("paper", "rock")
        assert result == ("paper", "covers", "rock")
    
    def test_reverse_order_combinations(self):
        """Test that order doesn't matter for determining winner"""
        # Test reverse order gives same winner but different loser position
        result1 = rock("rock", "scissors")
        result2 = rock("scissors", "rock")
        
        assert result1 == ("rock", "crushes", "scissors")
        assert result2 == ("rock", "crushes", "scissors")
        
        result1 = rock("scissors", "paper")
        result2 = rock("paper", "scissors")
        
        assert result1 == ("scissors", "cuts", "paper")
        assert result2 == ("scissors", "cuts", "paper")
    
    def test_tie_conditions(self):
        """Test all tie conditions return None"""
        assert rock("rock", "rock") is None
        assert rock("paper", "paper") is None
        assert rock("scissors", "scissors") is None

class TestRockFunctionInputValidation:
    """Test input validation of the rock() function."""
    
    def test_invalid_player1_input(self):
        """Test invalid input for player1"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock("stone", "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("lizard", "paper")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("", "rock")
    
    def test_invalid_player2_input(self):
        """Test invalid input for player2"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock", "stone")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("paper", "lizard")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("scissors", "")
    
    def test_both_players_invalid(self):
        """Test when both players have invalid input"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock("stone", "lizard")
    
    def test_case_sensitivity(self):
        """Test case sensitivity of inputs
        
        This reveals that the function is case-sensitive and will reject
        uppercase or mixed-case inputs.
        """
        with pytest.raises(ValueError, match="Invalid input"):
            rock("ROCK", "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("Rock", "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock", "SCISSORS")
    
    def test_whitespace_handling(self):
        """Test handling of whitespace in inputs"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock(" rock", "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock ", "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock", " scissors ")
    
    def test_none_inputs(self):
        """Test None inputs"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock(None, "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock", None)
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock(None, None)
    
    def test_numeric_inputs(self):
        """Test numeric inputs"""
        with pytest.raises(ValueError, match="Invalid input"):
            rock(1, "scissors")
        
        with pytest.raises(ValueError, match="Invalid input"):
            rock("rock", 2)

class TestRockFunctionReturnTypes:
    """Test return value types and structure."""
    
    def test_win_return_tuple_structure(self):
        """Test that winning results return proper tuple structure"""
        result = rock("rock", "scissors")
        
        assert isinstance(result, tuple)
        assert len(result) == 3
        
        winner, action, loser = result
        assert isinstance(winner, str)
        assert isinstance(action, str)
        assert isinstance(loser, str)
    
    def test_tie_return_type(self):
        """Test that ties return None (not False, 0, etc.)"""
        result = rock("rock", "rock")
        assert result is None
        assert result != False
        assert result != 0
        assert result != ""

class TestRulesDataStructure:
    """Test the rules dictionary structure and completeness."""
    
    def test_rules_completeness(self):
        """Test that all winning combinations are covered"""
        # There should be exactly 3 rules for 3 winning combinations
        assert len(rules) == 3
        
        # Test each expected rule exists
        assert frozenset(("rock", "scissors")) in rules
        assert frozenset(("scissors", "paper")) in rules
        assert frozenset(("paper", "rock")) in rules
    
    def test_rules_structure(self):
        """Test the structure of each rule"""
        for key, value in rules.items():
            assert isinstance(key, frozenset)
            assert len(key) == 2
            assert isinstance(value, tuple)
            assert len(value) == 2
            
            winner, action = value
            assert winner in key  # Winner should be one of the players
            assert isinstance(action, str)
    
    def test_rules_consistency(self):
        """Test that rules are consistent with expected outcomes"""
        assert rules[frozenset(("rock", "scissors"))] == ("rock", "crushes")
        assert rules[frozenset(("scissors", "paper"))] == ("scissors", "cuts")
        assert rules[frozenset(("paper", "rock"))] == ("paper", "covers")

class TestOptionsDataStructure:
    """Test the options set."""
    
    def test_options_completeness(self):
        """Test that options contains all expected choices"""
        assert len(options) == 3
        assert "rock" in options
        assert "paper" in options
        assert "scissors" in options
    
    def test_options_type(self):
        """Test that options is a set"""
        assert isinstance(options, set)

class TestMainFunctionIntegration:
    """Test the main() function integration."""
    
    @patch('sys.argv', ['rock2.py', 'rock', 'scissors'])
    @patch('builtins.print')
    def test_main_player1_wins(self, mock_print):
        """Test main function when player1 wins"""
        main()
        
        # Verify the expected print calls
        mock_print.assert_any_call("Player 1 played", "rock")
        mock_print.assert_any_call("Player 2 played", "scissors")
        mock_print.assert_any_call("Rock crushes scissors")
        mock_print.assert_any_call("Player 1 wins")
    
    @patch('sys.argv', ['rock2.py', 'scissors', 'rock'])
    @patch('builtins.print')
    def test_main_player2_wins(self, mock_print):
        """Test main function when player2 wins"""
        main()
        
        mock_print.assert_any_call("Player 1 played", "scissors")
        mock_print.assert_any_call("Player 2 played", "rock")
        mock_print.assert_any_call("Rock crushes scissors")
        mock_print.assert_any_call("Player 2 wins")
    
    @patch('sys.argv', ['rock2.py', 'rock', 'rock'])
    @patch('builtins.print')
    def test_main_tie_game(self, mock_print):
        """Test main function with tie game"""
        main()
        
        mock_print.assert_any_call("Player 1 played", "rock")
        mock_print.assert_any_call("Player 2 played", "rock")
        mock_print.assert_any_call("It's a tie")
    
    @patch('sys.argv', ['rock2.py', '--help'])
    def test_main_help_option(self):
        """Test that help option works"""
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0  # Help exits with code 0
    
    @patch('sys.argv', ['rock2.py', 'invalid'])
    def test_main_invalid_single_argument(self):
        """Test main with invalid single argument"""
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 2  # argparse exits with code 2 for errors
    
    @patch('sys.argv', ['rock2.py', 'rock', 'invalid'])
    def test_main_invalid_second_argument(self):
        """Test main with invalid second argument"""
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 2
    
    @patch('sys.argv', ['rock2.py'])
    def test_main_missing_arguments(self):
        """Test main with missing arguments"""
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 2

class TestMainFunctionBugs:
    """Test to identify specific bugs in the main() function."""
    
    @patch('sys.argv', ['rock2.py', 'rock', 'scissors'])
    @patch('builtins.print')
    def test_main_exception_handling_bug(self, mock_print):
        """Test reveals exception handling bug in main()
        
        The main() function has a try-except block but doesn't handle
        the case where result is not None after the exception.
        """
        main()
        
        # The code will try to access result even if an exception occurred
        # This specific test passes, but shows the logic flaw structure
    
    @patch('sys.argv', ['rock2.py', 'rock', 'scissors'])
    @patch('builtins.print')
    @patch('rock2.rock')
    def test_main_exception_flow_bug(self, mock_rock, mock_print):
        """Test the exception handling flow bug
        
        If rock() raises an exception, the code prints the error
        but then continues to check if result is None, which will
        cause a NameError since result was never assigned.
        """
        # Make rock() raise an exception
        mock_rock.side_effect = ValueError("Invalid input")
        
        # This should raise NameError because result is never defined
        with pytest.raises(NameError):
            main()
    
    @patch('sys.argv', ['rock2.py', 'paper', 'rock'])
    @patch('builtins.print')
    def test_main_output_format_issue(self, mock_print):
        """Test reveals output formatting inconsistency"""
        main()
        
        # Check the actual calls to see formatting issues
        calls = [str(call) for call in mock_print.call_args_list]
        
        # The output has inconsistent spacing/formatting
        # Empty print() calls create extra lines
        assert any("call()" in call for call in calls)  # Empty print calls

class TestEdgeCasesAndErrorConditions:
    """Test edge cases and error conditions."""
    
    def test_frozenset_key_lookup(self):
        """Test that frozenset keys work correctly for lookups"""
        # Test that the order doesn't matter for frozenset keys
        key1 = frozenset(("rock", "scissors"))
        key2 = frozenset(("scissors", "rock"))
        
        assert key1 == key2
        assert key1 in rules
        assert key2 in rules
        assert rules[key1] == rules[key2]
    
    def test_winner_determination_logic(self):
        """Test the winner determination logic"""
        # Test that winner is correctly identified from the rule
        result = rock("scissors", "rock")
        winner, action, loser = result
        
        # Winner should be "rock", loser should be "scissors"
        assert winner == "rock"
        assert loser == "scissors"
        assert action == "crushes"
    
    def test_comprehensive_game_matrix(self):
        """Test all possible game combinations systematically"""
        expected_outcomes = {
            ("rock", "rock"): None,
            ("rock", "paper"): ("paper", "covers", "rock"),
            ("rock", "scissors"): ("rock", "crushes", "scissors"),
            ("paper", "rock"): ("paper", "covers", "rock"),
            ("paper", "paper"): None,
            ("paper", "scissors"): ("scissors", "cuts", "paper"),
            ("scissors", "rock"): ("rock", "crushes", "scissors"),
            ("scissors", "paper"): ("scissors", "cuts", "paper"),
            ("scissors", "scissors"): None,
        }
        
        for (p1, p2), expected in expected_outcomes.items():
            result = rock(p1, p2)
            assert result == expected, f"Failed for {p1} vs {p2}"

class TestCodeStructureIssues:
    """Test to identify code structure and design issues."""
    
    def test_global_variables_usage(self):
        """Test that global variables are properly defined and used"""
        # Test that options and rules are accessible
        assert 'options' in globals()
        assert 'rules' in globals()
        
        # Test that they're used consistently
        from rock2 import options as imported_options, rules as imported_rules
        assert imported_options == {"rock", "paper", "scissors"}
        assert len(imported_rules) == 3
    
    def test_function_isolation(self):
        """Test that rock() function works independently of main()"""
        # The rock function should work without any dependency on main()
        result = rock("rock", "scissors")
        assert result is not None
        assert result[0] == "rock"