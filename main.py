from th_reinvesment_calc import get_btc_price, get_th_after_n_days


if __name__ == "__main__":
    print("Welcome to this simple TH price calculator.\n")
    user_starting_th = float(input("Enter your starting TH: "))
    user_n_years = int(input("Reinvesting for how many years? Enter a positive number, can be with a floating point e.g. 3.5: "))
    user_enable_verbose = input("Would you like to see daily TH upgrade amounts? If no, only the final TH amount is printed out to the screen. (y/n): ")
    
    BTC_PRICE_USDT_BINANCE = "https://api.binance.com/api/v3/ticker/price?symbol=BTC{}"
    current_btc_price_in_usdt = get_btc_price(
        key=BTC_PRICE_USDT_BINANCE,
        quote_asset="USDT"
    )
    get_th_after_n_days(
        initial_th=user_starting_th,
        sats_per_th=70,
        btc_price_usdt=current_btc_price_in_usdt*1.5,
        n_days=int(365*user_n_years),
        verbose=True if user_enable_verbose=="y" else False
    )