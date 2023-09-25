#!/usr/bin/env python3
import sys
from get_products import get_products
from get_draft import get_draft
from make_ads import make_ads

def main(data_path, draft_path):
    products = get_products(data_path)
    draft = get_draft(draft_path)

    make_ads(products, draft)



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Im help message, but u can gfu =)")
        exit()

    if len(sys.argv) == 2 and sys.argv[1] == '--test':
        print("test data!")
        main('data.csv', 'draft.csv')
        exit()


    if len(sys.argv) != 3:
        print(
            "ERR: usage: $ python3 main.py data.csv draft.csv"
            + "\n        OR: $ ./main.py data.csv draft.csv"
            + "\n    OR TRY: $ python3 main.py --help"
            + "\n  FOR TEST: $ python3 main.py --test (needed draft.csv and data.csv in working direcory)")
        exit()
    data_path = sys.argv[1]
    draft_path = sys.argv[2]

    main(data_path, draft_path)
