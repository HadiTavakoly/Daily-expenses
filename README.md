# 📝 Daily-expenses
## 🔧 A tool for accurate storage of daily expenses 🔧
## Do you remember which restaurant you ate at last Monday or how much it cost to take the taxi home?

Each of us does things during the day, month and year that we pay for some of them.
It must have happened to you that you want to control the expenses of a certain day or the expenses of your life, or you want to have a list of your expenses, or you even want to control the expenses of a job for a certain period of time.

With this program, you can easily list your expenses with exact time and date and based on a specific topic, and see the list whenever you need it.
### Usage
| Command | Description |
| --- | --- |
| --init | Create a table  or reinitialize |
| --show|See total expenses based special category |
| --add|Add something to your expenses |
| --version | See the program version |
| --help or -h | Help|



#### Tip: First you need to create the table .
```
spend_app.py --init
```

#### If you want to see all expenses (or based by category) 
```
spend_app.py --show [<catgory>]
```
#### If you want to add something to your expenses (by mentioning category and message)
```
spend_app.py --add <amount> <catgory> [<Message>]]
```
#### When you want to see the program version
```
spend_app.py --version
```
#### When you need help about app
```
spend_app.py --help 
```
or
```
spend_app.py -h
```
