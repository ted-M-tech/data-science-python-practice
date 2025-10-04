from guessing_game import guessing_game

def test_correct_guess_first_try():
    """Test winning on the first guess"""
    import random
    from io import StringIO
    import sys

    # Mock random and input
    random.randint = lambda a, b: 500
    sys.stdin = StringIO('500\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "You got it!" in output
    assert "It took you 1 guess(es)" in output

    # Reset
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__


def test_multiple_guesses():
    """Test winning after multiple guesses"""
    import random
    from io import StringIO
    import sys

    random.randint = lambda a, b: 500
    sys.stdin = StringIO('250\n750\n500\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "too low" in output
    assert "too high" in output
    assert "You got it!" in output
    assert "It took you 3 guess(es)" in output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__


def test_max_guesses_exceeded():
    """Test game over after 10 guesses"""
    import random
    from io import StringIO
    import sys

    random.randint = lambda a, b: 500
    sys.stdin = StringIO('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "Game over!" in output
    assert "You've used all 10 guess(es)" in output
    assert "The hidden number is 500" in output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__


def test_invalid_input():
    """Test handling of non-numeric input"""
    import random
    from io import StringIO
    import sys

    random.randint = lambda a, b: 500
    sys.stdin = StringIO('abc\n500\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "Invalid input!" in output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__


def test_empty_input():
    """Test handling of empty input"""
    import random
    from io import StringIO
    import sys

    random.randint = lambda a, b: 500
    sys.stdin = StringIO('\n500\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "Empty input is not allowed" in output
    assert "You got it!" in output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__


def test_out_of_range():
    """Test handling of out of range guesses"""
    import random
    from io import StringIO
    import sys

    random.randint = lambda a, b: 500
    sys.stdin = StringIO('1500\n0\n500\n')
    sys.stdout = StringIO()

    guessing_game()
    output = sys.stdout.getvalue()

    assert "Your guess must be between" in output
    assert "You got it!" in output

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    print("Running tests...\n")

    test_correct_guess_first_try()
    print("✓ test_correct_guess_first_try passed")

    test_multiple_guesses()
    print("✓ test_multiple_guesses passed")

    test_max_guesses_exceeded()
    print("✓ test_max_guesses_exceeded passed")

    test_invalid_input()
    print("✓ test_invalid_input passed")

    test_empty_input()
    print("✓ test_empty_input passed")

    test_out_of_range()
    print("✓ test_out_of_range passed")

    print("\nAll tests passed!")
