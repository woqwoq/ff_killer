from ff_killer import evaluate_truth_table


def main():
    expr = "( A n B ) / C v R"

    evaluate_truth_table(expr)


if __name__ == "__main__":
    main()
