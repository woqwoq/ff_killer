import argparse 

from ff_killer import evaluate_truth_table


def main():
    #Parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help="the expression to be evaluated (in quoutes)")
    args = parser.parse_args()

    expr = args.expression

    evaluate_truth_table(expr)


if __name__ == "__main__":
    main()
