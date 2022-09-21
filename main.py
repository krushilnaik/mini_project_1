#! ./venv/Scripts/python

# INF601 - Advanced Programming in Python
# Krushil Naik
# Mini Project 1

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta

today = date.today()
buffer = today - timedelta(days=20)

# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to a ndarray in NumPy.

data = yf.download(
    tickers="aapl dis tsla crsr msft",
    start=buffer.isoformat(),
    end=today.isoformat(),
)

adj_close = data["Adj Close"]

# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
for i, ticker in enumerate(adj_close):
    # close any existing figures to avoid copying it over in our new PNG
    plt.close()

    # parse the price data
    array = np.array([price for price in adj_close[ticker][:10]])

    # plot and save the graphs
    fig, ax = plt.subplots()

    ax.set_title("Stock vs Trading Day")
    ax.set_xlabel("Num trading days ago")
    ax.set_ylabel("Stock")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(color="grey", linestyle="-", linewidth=0.25, alpha=0.5)

    # plt.show()
    plt.plot(array)
    plt.savefig(f"./charts/{ticker}.png")

# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.
