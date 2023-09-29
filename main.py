from get_products import get_products
from get_draft import get_draft
from make_final_csv import make_final_csv
from make_ads import make_ads

def main():
    make_final_csv()

    products = get_products('data.csv')
    draft = get_draft('draft.csv')
    make_ads(products, draft)
    #print(draft)


if __name__ == '__main__':
    main()
