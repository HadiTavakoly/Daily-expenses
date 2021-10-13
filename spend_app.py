#                      I.T.N.O.A

from docopt import docopt
import api

try:
    Usage = """

  Usage:
    spend_app.py --init
    spend_app.py --show [<catgory>]
    spend_app.py --add <amount> <catgory> [<Message>]
    spend_app.py --help | -h
    spend_app.py --version
    """

    a = docopt(Usage, help=False, version="1.0.0")

    if a["--init"]:
        api.init()

    if a["--add"]:
        try:
            message = a["<Message>"]
            api.add(a["<amount>"], a["<catgory>"], message)
        except:
            print(Usage)

    if a["--show"]:
        api.show(a["<catgory>"])

    if a["--help"] or a["-h"]:
        api.help()

except api.sqlite3.OperationalError:
    print(
        """\nFirst you need to create the table with (--init)

  Use (--help) or (-h) for more information"""
    )

    print(Usage)
