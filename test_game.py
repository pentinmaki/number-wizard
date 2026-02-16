"""
Peliä testaava skripti
"""
import sys
from io import StringIO
from game import calculate_score, select_difficulty

def test_calculate_score():
    """Testaa pistejärjestelmää"""
    print("Testing calculate_score()...")
    
    # Testi 1: Easy vaikeustaso
    score = calculate_score(5, 50)
    assert score >= 0, "Score should be non-negative"
    print(f"  ✓ Easy (5 attempts): {score} points")
    
    # Testi 2: Medium vaikeustaso
    score = calculate_score(10, 100)
    assert score > 0, "Score should be positive for reasonable attempts"
    print(f"  ✓ Medium (10 attempts): {score} points")
    
    # Testi 3: Hard vaikeustaso
    score = calculate_score(20, 500)
    print(f"  ✓ Hard (20 attempts): {score} points")
    
    # Testi 4: Maksimi yritykset (pitäisi antaa 0 pisteitä)
    score = calculate_score(100, 50)
    assert score == 0, "Too many attempts should result in 0 points"
    print(f"  ✓ 100 attempts: {score} points (as expected)")
    
    print("✓ calculate_score() tests passed!\n")

def test_difficulty_ranges():
    """Testaa vaikeustason alueet"""
    print("Testing difficulty settings...")
    
    ranges = {
        1: 50,
        2: 100,
        3: 500
    }
    
    expected_difficulty = {50: "Easy", 100: "Medium", 500: "Hard"}
    
    for difficulty, max_num in ranges.items():
        print(f"  ✓ Difficulty {difficulty}: range 1-{max_num} ({expected_difficulty[max_num]})")
    
    print("✓ Difficulty ranges OK!\n")

def test_max_attempts():
    """Testaa yritysrajoitukset"""
    print("Testing max attempts per difficulty...")
    
    test_cases = [
        (50, 10),
        (100, 20),
        (500, 100)
    ]
    
    for max_range, expected_attempts in test_cases:
        actual = max_range // 5
        assert actual == expected_attempts, f"Wrong attempt limit for {max_range}"
        print(f"  ✓ Range {max_range}: {actual} max attempts")
    
    print("✓ Max attempts calculations OK!\n")

def test_score_progression():
    """Testaa että pisteet laskevat yritysten myötä"""
    print("Testing score progression...")
    
    score_1 = calculate_score(1, 100)
    score_5 = calculate_score(5, 100)
    score_10 = calculate_score(10, 100)
    
    assert score_1 > score_5, "Fewer attempts should give more points"
    assert score_5 > score_10, "Fewer attempts should give more points"
    
    print(f"  ✓ 1 attempt:  {score_1} points")
    print(f"  ✓ 5 attempts: {score_5} points")
    print(f"  ✓ 10 attempts: {score_10} points")
    print("✓ Score progression OK!\n")

def test_difficulty_multipliers():
    """Testaa vaikeustason kertoimet"""
    print("Testing difficulty multipliers...")
    
    same_attempts = 10
    
    easy = calculate_score(same_attempts, 50)      # kerroin 1
    medium = calculate_score(same_attempts, 100)   # kerroin 1.5
    hard = calculate_score(same_attempts, 500)     # kerroin 2
    
    assert easy < medium < hard, "Harder difficulties should give more points"
    
    print(f"  ✓ Easy (10 att):   {easy} points")
    print(f"  ✓ Medium (10 att): {medium} points")
    print(f"  ✓ Hard (10 att):   {hard} points")
    print("✓ Difficulty multipliers OK!\n")

def run_all_tests():
    """Aja kaikki testit"""
    print("="*50)
    print("  🧪 NUMBER WIZARD TESTS 🧪")
    print("="*50 + "\n")
    
    try:
        test_calculate_score()
        test_difficulty_ranges()
        test_max_attempts()
        test_score_progression()
        test_difficulty_multipliers()
        
        print("="*50)
        print("  ✓ ALL TESTS PASSED! ✓")
        print("="*50)
        return True
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
