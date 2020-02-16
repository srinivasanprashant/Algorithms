def bottom_up_cut_rod(n: int, prices: list):
    """
    Constructs a bottom-up dynamic programming solution for the rod-cutting problem
    Runtime: O(n^2)
    Arguments
    ----------
    n: int, the maximum length of the rod.
    prices: list, the prices for each piece of rod. ``p[i-i]`` is the
    price for a rod of length ``i``
    Returns
    -------
    The maximum revenue obtainable from cutting a rod of length n given
    the prices for each piece of rod p.
    Examples
    -------
    >>> bottom_up_cut_rod(4, [1, 5, 8, 9])
    10
    >>> bottom_up_cut_rod(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """
    _enforce_args(n, prices)

    # length(max_rev) = n + 1, to accommodate for the revenue obtainable from a rod of length 0.
    max_rev = [float("-inf") for _ in range(n + 1)]
    max_rev[0] = 0

    for i in range(1, n + 1):
        max_revenue_i = max_rev[i]
        for j in range(1, i + 1):
            max_revenue_i = max(max_revenue_i, prices[j - 1] + max_rev[i - j])

        max_rev[i] = max_revenue_i

    return max_rev[n]


def _enforce_args(n: int, prices: list):
    """
        Basic checks on the arguments to the rod-cutting algorithms
        n: int, the length of the rod
        prices: list, the price list for each piece of rod.
        Throws ValueError:
        if n is negative or there are fewer items in the price list than the length of the rod
        """
    if n < 0:
        raise ValueError(f"n must be greater than or equal to 0. Got n = {n}")

    if n > len(prices):
        raise ValueError(
            f"Each integral piece of rod must have a corresponding "
            f"price. Got n = {n} but length of prices = {len(prices)}"
        )


def main():
    prices = [6, 10, 12, 15, 20, 23]
    n = len(prices)

    # the best revenue comes from cutting the rod into 6 pieces, each
    # of length 1 resulting in a revenue of 6 * 6 = 36.
    expected_max_revenue = 36

    max_rev_bottom_up = bottom_up_cut_rod(n, prices)

    assert max_rev_bottom_up == expected_max_revenue


if __name__ == "__main__":
    main()