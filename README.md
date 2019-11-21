# PySupplyGraph

PySupplyGraph (Assignment 2) is a school project, it will parse a csv file in order to get data and based on it, will create a supply and demand curve on a graph.

## Installation

Python 3 is required in order to run this program

### OSX

```bash
brew install python3
```

Then we will need Matplotlib in order to create a graph

```bash
pip install matplotlib
```

If you have any trouble installing matplotlib go check the [official website](https://matplotlib.org/users/installing.html)

## Usage

```bash
$ pysupplygraph.py
Usage: pysupplygraph.py [file]

Command:
file - path to a data.csv file
```

csv file format example:
```bash
price, quanity demanded, quantity supplied
50, 10, 100
45, 14, 97
40, 18, 94
35, 22, 89
30, 28, 84
25, 35, 77
20, 45, 68
15, 57, 57
10, 73, 40
5,  100,  0 
```

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)