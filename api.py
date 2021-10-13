#                      I.T.N.O.A

import sqlite3
import tabulate
from datetime import datetime

conn = sqlite3.connect("spend.db")
c = conn.cursor()

# creat table or reinitialize
def init():
    c.execute(
        """CREATE TABLE IF NOT EXISTS Spend(
                Amount real,
                Category text COLLATE NOCASE,
                Message text,
                Date text,
                Time text)"""
    )
    conn.commit()
    conn.close()
    print("Your table created")


# add item into db
def add(
    amount,
    category,
    message="",
    date=datetime.now().date(),
    time=datetime.now().strftime("%H:%M:%S"),
):
    c.execute(
        "INSERT INTO Spend VALUES(:amount , :category ,:message, :date, :time)",
        {
            "amount": amount,
            "category": category,
            "message": message,
            "date": date,
            "time": time,
        },
    )
    conn.commit()
    conn.close()
    print("Item added")


# show table
def show(category=None):
    if category:
        c.execute(
            "SELECT * FROM Spend WHERE Category = :category ", {"category": category}
        )
        result = c.fetchall()
        c.execute(
            f"SELECT sum(Amount)FROM Spend WHERE Category = :category ",
            {"category": category},
        )
        total = c.fetchone()[0]
    else:
        c.execute("SELECT * FROM Spend")
        result = c.fetchall()
        c.execute("SELECT sum(Amount)FROM Spend")
        total = c.fetchone()[0]

    conn.close()

    print("\n", f"Total expense : {total}", "T", "\n")
    print(
        tabulate.tabulate(
            result,
            headers=["Amount", "Category", "Message", "Date", "Time"],
            tablefmt="simple",
        ),
        "\n",
    )


# instructions for use
def help():
    print(
        """
(=-+This app helps you keep track of your expenses+-=)


*_*                                       *_*
    To use, follow the instructions below :

    * Create a table  or reinitialize ----> --init  
    !(You cannot use the other options without running this section)!

    * If you want to see expenses (by <category>) ----> --show [<category>]

    * If you want to add something to your expenses (by mentioning 
        <category> and <message>)  ----> --add <amount> <category> [<Message>]

    * If you want to see the program version ----> --version\n\n"""
    )