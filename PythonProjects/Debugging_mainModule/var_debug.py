def calculate_position_pnl(quantity, price_change):
    """Calculate P&L for one position."""
    position_pnl = abs(quantity) * price_change  # BUG
    return position_pnl


def calculate_portfolio_pnl(positions, price_changes):
    """Calculate total P&L for the portfolio."""
    total_pnl = 0.0

    for i in range(len(positions)):
        quantity = positions[i]
        change = price_changes[i]

        position_pnl = calculate_position_pnl(quantity, change)
        total_pnl += position_pnl

        print(
            f"Position {i}: "
            f"quantity={quantity}, "
            f"change={change}, "
            f"P&L={position_pnl}"
        )

    return total_pnl


def calculate_historical_var(pnl_scenarios, confidence):
    """Simplified historical VaR from scenario P&Ls."""
    sorted_pnl = sorted(pnl_scenarios)

    index = int((1 - confidence) * len(sorted_pnl))
    var = -sorted_pnl[index]

    return var


def main():
    positions = [100, -50, 0]
    price_changes = [-2, 3, -1]

    portfolio_pnl = calculate_portfolio_pnl(positions, price_changes)
    print(f"\nPortfolio P&L: {portfolio_pnl:.2f}")
    historical_scenarios = [-500, -300, -200, -100, 50,100, -400, 200, -150, 80]
    var_95 = calculate_historical_var(historical_scenarios, 1.05)
    print(f"95% historical VaR: {var_95:.2f}")


if __name__ == "__main__":
    main()
