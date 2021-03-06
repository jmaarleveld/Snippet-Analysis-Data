# Snippet-Analysis-Data

This repository contains the raw data required to reproduce figures
used in my thesis.

## Layout

Every `iteration_X` directory contains files corresponding to a single set
of added changes. This process is incremental. Hence, iteration X also
includes all changes made in prior iterations.

Iterations:
0) Base line
1) Included start nonterminals and backward compatibility for older Java versions
2) Included nonterminals for partial comments
3) Included nonterminals for lists of syntactic units (statements, methods, etc.)
4) Included nonterminals for incomplete blocks
5) Included nonterminals for empty module and comments. Added comment stripping
6) Nonterminals merged under one top-level nonterminal

NOTE: iteration 5 and 6 should yield the same results. Any difference
can be considered a bug.

Additionally, the `benchmarks` directory contains benchmark data.
The files with the suffix `toplevel` are benchmarks for parsing
with a specific top-level nonterminal (iteration 6),
while the other files are benchmarks
made with specific nonterminals used for parsing (i.e. the classification).

The `diffs` directory contains metadata files required to run the
benchmarks.

Note that data corresponding to jEdit has been named with "trunk" due
to a typo early on in the project.

## How to generate the data

In order to generate the data for a specific iteration, the necessary
changed to the Rascal code must be done manually. Next, the grammar
must be generated using the `makeGrammar` function.

Next, the following repositories must be cloned:

[Apache Commons Collections](https://github.com/apache/commons-collections)

[Apache Commons IO](https://github.com/apache/commons-io)

[JPacMan](https://github.com/SERG-Delft/jpacman)

[jEdit](https://sourceforge.net/projects/jedit/)

Next, the data can be generated by running the following set of commands:

```
python main.py -d commons-collections -c 0 1 2 3 -m 300 --diff-method myers
python main.py -d commons-collections -c 0 1 2 3 -m 300 --diff-method minimal
python main.py -d commons-collections -c 0 1 2 3 -m 300 --diff-method patience
python main.py -d commons-collections -c 0 1 2 3 -m 300 --diff-method histogram
python main.py -d commons-io -c 0 1 2 3 -m 300
python main.py -d jpacman -c 0 1 2 3 -m 300
python main.py -d jedit -c 0 1 2 3 -m 300
```

Note that this required that all repositories required are cloned into
the same directory where the Python program is located. Additionally,
the jedit repository must be converted to Git first.
