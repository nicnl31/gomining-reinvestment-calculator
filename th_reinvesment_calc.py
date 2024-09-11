import requests
import json

import numpy as np

from prices import TH_UPGRADE_PRICES


def get_btc_price(
        key: str="https://api.binance.com/api/v3/ticker/price?symbol=BTC{}", 
        quote_asset: str="USDT"
    ) -> float:
    """
    Retrieves the current price of Bitcoin in 
    """
    full_key = key.format(quote_asset)
    data = requests.get(full_key)
    data_json = data.json()
    btc_price_usdt = float(data_json["price"])
    return btc_price_usdt


def get_th_after_n_days(
        initial_th: float, 
        sats_per_th: float, 
        btc_price_usdt: float, 
        n_days: int,
        energy_efficiency: int=20,
        max_th_upgradable: float=5000.0,
        verbose=2
) -> float:
    """
    Calculates the total TH after n_days given the starting TH, and the 
    number of days of reinvesting.

    This is only an approximation, since it does not take into account the
    daily change in BTC price. Given that this script is produced in September
    2024

    Does not take BTC halving into consideration, which halves the 
    sats_per_th approximately every 4 years.
    """
    all_th_array = np.array(list(TH_UPGRADE_PRICES[energy_efficiency].keys()))
    current_th = 0.0
    current_th += initial_th
    for d in range(n_days):
        day_reward_in_btc = (0.00000001 * sats_per_th) * current_th
        day_reward_in_dollar = btc_price_usdt * day_reward_in_btc
        # Retrieve the current TH tier
        current_th_tier = int(all_th_array[all_th_array < current_th].max())
        # Get the current upgrade price per TH for the current tier
        current_upgrade_price_per_th = TH_UPGRADE_PRICES[energy_efficiency][current_th_tier]
        # Calculate the upgrade amount for this day
        day_upgrade_amount_in_th = day_reward_in_dollar/current_upgrade_price_per_th
        # New TH amount
        current_th += day_upgrade_amount_in_th
        # Print results:
        if verbose:
            print(f"Day {d+1} upgrade: {day_upgrade_amount_in_th:.2f}TH, new TH: {current_th:.2f}TH")
    
    print(f"Final TH balance after {n_days} days: {min(current_th, max_th_upgradable):.2f}TH. ")