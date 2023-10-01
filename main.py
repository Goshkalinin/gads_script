from get_products import get_products
from get_draft import get_draft
from make_final_csv import make_final_csv
from make_ads import make_ads
from write_campaign_footer import write_campaign_footer


def main():


    products = get_products('data.csv')
    draft = get_draft('draft.csv')

    make_final_csv(draft)
    make_ads(products, draft)
    write_campaign_footer(draft)
    #print(draft)


if __name__ == '__main__':
    main()
