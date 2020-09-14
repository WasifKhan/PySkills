def test_solution():
    from solution import tower_of_hanoi

    assert tower_of_hanoi(2, [2, 1], [], []) == 3
    assert tower_of_hanoi(3, [3, 2, 1], [], []) == 7
    assert tower_of_hanoi(0, [], [], []) == 0
    assert tower_of_hanoi(1, [1], [], []) == 1
