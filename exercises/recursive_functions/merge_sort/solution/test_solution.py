def test_solution():
    from solution import custom_sort

    assert custom_sort([1, 7, 4, 2]) == [1, 2, 4, 7]
    assert custom_sort([2, 1]) == [1, 2]
    assert custom_sort([1]) == [1]
    assert custom_sort([]) == []
    assert custom_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
