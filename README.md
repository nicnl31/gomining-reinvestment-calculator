# GoMining Reinvestment Calculator

This is a personal calculator that I made that can calculate the number of THs
you can get for a miner after reinvesting.

# How to run this repo

In the command line, run the following:

$ `git clone https://github.com/nicnl31/gomining-reinvestment-calculator`
$ `cd gomining-reinvestment_calculator`
$ `pip install -r requirements.txt`
$ `python main.py`

# Structure

prices.py
th_reinvestment_calc.py:
    get_th_after(initial_th, sats_per_th, btc_price_usd, n_days)