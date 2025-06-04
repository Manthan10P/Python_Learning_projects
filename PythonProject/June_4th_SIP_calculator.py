def calculate_sip_nav(sip_amount, nav_list):
    total_units = 0
    total_invested = 0
    print("Month\tNAV\tUnits Purchased")
    for i, nav in enumerate(nav_list):
        units = sip_amount / nav
        total_units += units
        total_invested += sip_amount
        print(f"{i + 1}\t{nav:.2f}\t{units:.2f}")

    latest_nav = nav_list[-1]  # Or ask user for current NAV
    current_value = total_units * latest_nav
    gain = current_value - total_invested

    print(f"\nTotal Units: {total_units:.2f}")
    print(f"Total Invested: ₹{total_invested:.2f}")
    print(f"Current Value (NAV ₹{latest_nav}): ₹{current_value:.2f}")
    print(f"Gain/Loss: ₹{gain:.2f}")


# Example usage:
sip_amount = 5000
navs = [50.0, 52.0, 48.0, 54.0]  # You can modify this list
calculate_sip_nav(sip_amount, navs)
