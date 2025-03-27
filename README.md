# Logical Expression Evaluator (a.k.a ff_killer)

## Overview

This project is a Python-based logical expression evaluator that constructs and evaluates truth tables for given Boolean expressions. It supports standard logical operations and provides an easy way to compute truth tables and evaluate expressions.

## Features

- Supports logical operators: and, or, not (also supports shorthand: n/^, v/u, ~)

- Obeys to brackets

- Converts set notation (/) to logical operations

- Generates truth tables dynamically

- Reads allowed variables from a configuration file (config.ini)

- Can be executed via command-line

## Requirements
`Python 3.x`

## Installation
```
git clone https://github.com/woqwoq/leetcode-cv-updater.git
cd leetcode-stats-updater
```

## Config
Make sure to set your own variables in `config.ini`
```
ALLOWED_VARS = P,Q,R
```
Keep in mind using `OR` as a string in an expression and `R` as a prime proposition will cause an error.

## Usage Requirements

The expression MUST have an empty space between each of its characters as follows:
```
"( A n B ) u C"
```

The next example would be an invalid expression:
```
"(A n B )u C"
 ^      ^
```

## Example Usage

```
python3 ff_killer_cli.py "P and ( Q or ~ R )"     
```
### Example Output
```
P        Q       R       P and ( Q or ~ R ) 
0        0       0       0       
0        0       1       0       
0        1       0       0       
0        1       1       0       
1        0       0       1       
1        0       1       0       
1        1       0       1
1        1       1       1
```

## TODO
- Fix the issue requiring an empty space between each char
- Optimizations???

