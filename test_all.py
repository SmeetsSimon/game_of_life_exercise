from main import (
    count_neighbours,
    create_empty_grid,
    create_row_zeros,
    get_bottom,
    get_bottomleft,
    get_bottomright,
    get_left,
    get_neighbours,
    get_right,
    get_top,
    get_topleft,
    get_topright,
    live_or_die,
    update_grid,
)


def test_create_row_zeros_2():
    """Test if a list of 2 zeros is created"""
    result = create_row_zeros(2)
    expected = [0, 0]
    assert result == expected


def test_create_row_zeros_3():
    """Test if a list of 3 zeros is created"""
    result = create_row_zeros(3)
    expected = [0, 0, 0]
    assert result == expected


def test_create_row_zeros_5():
    """Test if a list of 5 zeros is created"""
    result = create_row_zeros(5)
    expected = [0, 0, 0, 0, 0]
    assert result == expected


def test_create_empty_grid_2_by_2():
    """Test if the function creates an empty grid of 2x2

    This indicates that all cells are dead.
    """
    result = create_empty_grid(2, 2)
    expected = [
        [0, 0],
        [0, 0],
    ]
    assert result == expected


def test_create_empty_grid_3_by_3():
    """Test if the function creates an empty grid of 3x3

    This indicates that all cells are dead.
    """
    result = create_empty_grid(3, 3)
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert result == expected


def test_create_empty_grid_5_by_5():
    """Test if the function creates an empty grid of 5x5

    This indicates that all cells are dead.
    """
    result = create_empty_grid(5, 5)
    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert result == expected


def test_left_2x2_a():
    """Tests that the left neighbour of 4 is 3"""
    grid = [
        [1, 2],
        [3, 4],
    ]

    result = get_left(grid, 1, 1)
    assert result == 3


def test_left_2x2_b():
    """Tests that the left neighbour of 2 is 1"""
    grid = [
        [1, 2],
        [3, 4],
    ]

    result = get_left(grid, 1, 0)
    assert result == 1


def test_left_2x2_on_first_column_a():
    """Tests that the left neighbour of 1 does not exist and thus returns 0"""
    grid = [
        [1, 2],
        [3, 4],
    ]

    result = get_left(grid, 0, 0)
    assert result == 0


def test_left_2x2_on_first_column_b():
    """Tests that the left neighbour of 3 does not exist and thus returns 0"""
    grid = [
        [1, 2],
        [3, 4],
    ]

    result = get_left(grid, 0, 1)
    assert result == 0


def test_left():
    """Tests that the left neighbour of 5 is 4"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_left(grid, 1, 1)
    assert result == 4


def test_left_on_left_column():
    """Tests that the left neighbour of 4 does not exist and thus returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_left(grid, 0, 1)
    assert result == 0


def test_right():
    """Tests that the right neighbour of 5 is 6"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_right(grid, 3, 1, 1)
    assert result == 6


def test_right_on_last_border():
    """Tests that the right neighbour of 6 does not exist and thus returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_right(grid, 3, 2, 1)
    assert result == 0


def test_top():
    """Tests that the top neighbour of 5 is 2"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_top(grid, 1, 1)
    assert result == 2


def test_top_on_first_row():
    """Tests that the top neighbour of 2 does not exist and thus returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_top(grid, 1, 0)
    assert result == 0


def test_bottom():
    """Tests that the bottom neighbour of 5 is 8"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottom(grid, 3, 1, 1)
    assert result == 8


def test_bottom_on_last_row():
    """Tests that the bottom neighbour of 8 does not exist and
    thus returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottom(grid, 3, 1, 2)
    assert result == 0


def test_topleft():
    """Tests that the top left neighbour of 5 is 1"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_topleft(grid, 1, 1)
    assert result == 1


def test_topleft_on_first_column():
    """Tests that the top left neighbour of 4 does not exist and thus
    returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_topleft(grid, 0, 1)
    assert result == 0


def test_topleft_on_top_left_corner():
    """Tests that the top left neighbour of 1 does not exist and thus
    returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_topleft(grid, 0, 0)
    assert result == 0


def test_topright():
    """Tests that the top right neighbour of 5 is 3"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_topright(grid, 3, 1, 1)
    assert result == 3


def test_topright_on_top_right():
    """Tests that the top right neighbour of 3 does not exist and thus
    returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_topright(grid, 3, 2, 1)
    assert result == 0


def test_bottomleft():
    """Tests that the bottom left neighbour of 5 is 7"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottomleft(grid, 3, 1, 1)
    assert result == 7


def test_bottomleft_on_bottom_left():
    """Tests that the bottom left neighbour of 7 does not exist and thus
    returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottomleft(grid, 3, 0, 2)
    assert result == 0


def test_bottomright():
    """Tests that the bottom right neighbour of 5 is 9"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottomright(grid, 3, 3, 1, 1)
    assert result == 9


def test_bottomright_on_bottom_right():
    """Tests that the bottom right neighbour of 9 does not exist and thus
    returns 0"""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    result = get_bottomright(grid, 3, 3, 2, 2)
    assert result == 0


def test_left2():
    """Tests that the left neighbour of 5 is 4"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_left(grid, 2, 2)
    assert result == 4


def test_right2():
    """Tests that the right neighbour of 5 is 6"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_right(grid, 5, 2, 2)
    assert result == 6


def test_top2():
    """Tests that the top neighbour of 5 is 2"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_top(grid, 2, 2)
    assert result == 2


def test_bottom2():
    """Tests that the bottom neighbour of 5 is 8"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_bottom(grid, 5, 2, 2)
    assert result == 8


def test_topleft2():
    """Tests that the top left neighbour of 5 is 1"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_topleft(grid, 2, 2)
    assert result == 1


def test_topright2():
    """Tests that the top right neighbour of 5 is 3"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_topright(grid, 5, 2, 2)
    assert result == 3


def test_bottomleft2():
    """Tests that the bottom left neighbour of 5 is 7"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_bottomleft(grid, 5, 2, 2)
    assert result == 7


def test_bottomright2():
    """Tests that the bottom right neighbour of 5 is 9"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0],
    ]

    result = get_bottomright(grid, 5, 5, 2, 2)
    assert result == 9


def test_get_neighbours_small_grid():
    """Tests that we get a list with all neighbours"""
    grid = [
        [8, 7, 6],
        [1, 1, 5],
        [2, 3, 4],
    ]
    result = get_neighbours(grid, 3, 3, 1, 1)
    expected = [8, 7, 6, 5, 4, 3, 2, 1]
    assert result == expected


def test_get_neighbours_large_grid():
    """Tests that we get a list with all neighbours"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 8, 1, 4, 0],
        [0, 7, 6, 5, 0],
        [0, 0, 0, 0, 0],
    ]
    result = get_neighbours(grid, 5, 5, 2, 2)
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert result == expected


def test_count_neighbours():
    """Tests that we get 0 alive neighbours"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 0


def test_count_neighbours1():
    """Tests that we get 1 alive neighbour"""
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 1


def test_count_neighbours2():
    """Tests that we get 2 alive neighbours"""
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 2


def test_count_neighbours3():
    """Tests that we get 3 alive neighbours"""
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 3


def test_count_neighbours3b():
    """Tests that we get 3 alive neighbours"""
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [1, 0, 0],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 3


def test_count_neighbours7():
    """Tests that we get 7 alive neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 7


def test_count_neighbours8():
    """Tests that we get 8 alive neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    result = count_neighbours(grid, 3, 3, 1, 1)
    assert result == 8


def test_live_or_die_alive_2n():
    """The current cell lives as it is alive and has 2 neighbours"""
    grid = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is True


def test_live_or_die_alive_3n():
    """The current cell lives as it is alive and has 3 neighbours"""
    grid = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 0, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is True


def test_live_or_die_alive_4n():
    """The current cell dies as it is alive and has 4 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [0, 0, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_alive_5n():
    """The current cell dies as it is alive and has 5 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_alive_6n():
    """The current cell dies as it is alive and has 6 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_alive_7n():
    """The current cell dies as it is alive and has 7 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 0, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_alive_8n():
    """The current cell dies as it is alive and has 8 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_1n():
    """The current cell does not resurrect as it was dead
    and has 1 neighbour"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_2n():
    """The current cell does not resurrect as it was dead and
    has 2 neighbours"""
    grid = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_3n():
    """The current cell resurrects as it was dead and has 3 neighbours"""
    grid = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is True


def test_live_or_die_dead_4n():
    """The current cell does not resurrect as it was dead and
    has 4 neighbours"""
    grid = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_5n():
    """The current cell does not resurrect as it was dead and
    has 5 neighbours"""
    grid = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_6n():
    """The current cell does not resurrect as it was dead and
    has 6 neighbours"""
    grid = [
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_7n():
    """The current cell does not resurrect as it was dead and
    has 7 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_live_or_die_dead_8n():
    """The current cell does not resurrect as it was dead and
    has 8 neighbours"""
    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    result = live_or_die(grid, 3, 3, 1, 1)
    assert result is False


def test_game_still_block():
    """Test still game of life Block"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert grid == expected


def test_game_osc_blinker():
    """Test oscillating game of life Blinker"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert grid == expected


def test_game_osc_toad():
    """Test oscillating game of life Toad"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
    ]
    assert grid == expected


def test_game_osc_beacon():
    """Test oscillating game of life Beacon"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    assert grid == expected


def test_game_ss_glider_step1():
    """Test moving game of life Glider step 1"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
    ]
    assert grid == expected


def test_game_ss_glider_step2():
    """Test moving of life Glider step 2"""
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
    ]
    update_grid(grid, 5, 5)

    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
    ]
    assert grid == expected
