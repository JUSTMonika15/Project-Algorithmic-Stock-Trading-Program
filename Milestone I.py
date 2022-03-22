"""CSC 161 Project: Milestone I

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


def test_data(filename, col, day):
    """A test function to query the data you loaded into your program.

    Args:
        filename: A string for the filename containing the stock data,
                  in CSV format.

        col: A string of either "date", "open", "high", "low", "close",
             "volume", or "adj_close" for the column of stock market data to
             look into.

             The string arguments MUST be LOWERCASE!

        day: An integer reflecting the absolute number of the day in the
             data to look up, e.g. day 1, 15, or 1200 is row 1, 15, or 1200
             in the file.

    Returns:
        A value selected for the stock on some particular day, in some
        column col. The returned value *must* be of the appropriate type,
        such as float, int or str.
    """
    file_name = open(filename, "r")
    lines = file_name.readlines()  # Use filename to locate file
    day_line = lines[day]  # Use day to locate the horizontal file
    col_line = day_line.split(",")

    if col == "date":
        val = col_line[0]
    elif col == 'open':  # Use col to locate value
        val = float(col_line[1])
    elif col == 'high':
        val = float(col_line[2])
    elif col == 'low':
        val = float(col_line[3])
    elif col == 'close':
        val = float(col_line[4])
    elif col == "adj_close":
        val = float(col_line[5])
    elif col == "volume":
        val = int(col_line[6])

    print(val)
    return val


def transact(funds, stocks, qty, price, buy=False, sell=False):
    """A bookkeeping function to help make stock transactions.

       Args:
           funds: An account balance, a float; it is a value of how much money you have,
                  currently.

           stocks: An int, representing the number of stock you currently own.

           qty: An int, representing how many stock you wish to buy or sell.

           price: An float reflecting a price of a single stock.

           buy: This option parameter, if set to true, will initiate a buy.

           sell: This option parameter, if set to true, will initiate a sell.

       Returns:
           Two values *must* be returned. The first (a float) is the new
           account balance (funds) as the transaction is completed. The second
           is the number of stock now owned (an int) after the transaction is
           complete.

           Error condition #1: If the `buy` and `sell` keyword parameters
           are both set to true, or both false. You *must* raise an
           ValueError exception with an appropriate error message since this
           is an ambiguous transaction.

           Error condition #2: If you buy, or sell without enough funds or
           stocks to sell, respectively.  You *must* raise an
           ValueError exception with an appropriate error message since this
           is an ambiguous transaction.
    """
    money_changed = qty * float(price)  # The change of the money

    if buy is False and sell is True:  # Sell stocks
        if stocks < qty:
            raise ValueError(f"Insufficient stock owned to sell {qty} stocks!")
        
        funds += money_changed
        stocks -= qty
    elif buy is True and sell is False:  # Buy stocks
        
        if funds < money_changed:
            raise ValueError(f"Insufficient funds to purchase {qty} stock at ${price:0.2f}!")
        funds -= money_changed
        stocks += qty
    elif buy is True and sell is True:
        raise ValueError("Ambiguous transaction!"
                         "Can't determine whether to buy or sell!")
    elif buy is False and sell is False:
        raise ValueError("Ambiguous transaction!"
                         "Can't determine whether to buy or sell!")

    return funds, stocks


def main():
    pass  # Do nothing, just passing through!


if __name__ == '__main__':
    main()
