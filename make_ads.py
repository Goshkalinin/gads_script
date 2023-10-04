from dataclasses import dataclass
import csv

import checkers


def make_keywords(vendor, name):
    keywords = []

    #keyword 1: poduct.Name
    keyword = name
    keywords.append(keyword)

    #keyword 2: poduct.Vendor
    keyword = name.replace('-', '')
    keywords.append(keyword)

    #keyword 3: poduct.Vendor + poduct.Name
    keyword = vendor + " " + name
    keywords.append(keyword)

    #keyword 4: poduct.Vendor + poduct.Name, last '-$part' replaced with ''
    keyword = vendor + " " + name
    parts = keyword.split('-')
    keyword = '-'.join(parts[:-1])
    keywords.append(keyword)

    return keywords


def make_ads(products, draft):
    with open('final.csv', 'a', encoding='utf-8') as file:

        fieldnames = [
                'Campaign', 'Labels', 'Budget', 'Budget type', 'Standard conversion goals',
                'Custom conversion goal', 'Campaign Type', 'Networks', 'Languages',
                'Bid Strategy Type', 'Bid Strategy Name', 'Target CPA', 'Start Date',
                'End Date', 'Ad Schedule', 'Ad rotation', 'Targeting method',
                'Exclusion method', 'Audience targeting', 'Flexible Reach', 'Ad Group',
                'Max CPC', 'Max CPM', 'Max CPV', 'Percent CPC', 'Target CPM',
                'Target ROAS', 'Desktop Bid Modifier', 'Mobile Bid Modifier',
                'Tablet Bid Modifier', 'TV Screen Bid Modifier',
                'Display Network Custom Bid Type', 'Optimized targeting',
                'Ad Group Type', 'Audience name', 'Tracking template',
                'Final URL suffix', 'Custom parameters', 'ID', 'Location', 'Reach',
                'Location groups', 'Location groups legacy', 'Feed', 'Radius', 'Unit',
                'Bid Modifier', 'Keyword', 'Criterion Type', 'First page bid',
                'Top of page bid', 'First position bid', 'Quality score',
                'Landing page experience', 'Expected CTR', 'Ad relevance',
                'Final URL', 'Final mobile URL', 'Image Size', 'Link source',
                'Business name', 'Ad type', 'Headline 1', 'Headline 1 position',
                'Headline 2', 'Headline 2 position', 'Headline 3',
                'Headline 3 position', 'Headline 4', 'Headline 4 position',
                'Headline 5', 'Headline 5 position', 'Headline 6',
                'Headline 6 position', 'Headline 7', 'Headline 7 position',
                'Headline 8', 'Headline 8 position', 'Headline 9',
                'Headline 9 position', 'Headline 10', 'Headline 10 position',
                'Headline 11', 'Headline 11 position', 'Headline 12',
                'Headline 12 position', 'Headline 13', 'Headline 13 position',
                'Headline 14', 'Headline 14 position', 'Headline 15',
                'Headline 15 position', 'Description 1', 'Description 1 position',
                'Description 2', 'Description 2 position', 'Description 3',
                'Description 3 position', 'Description 4', 'Description 4 position',
                'Path 1', 'Path 2', 'Campaign Status', 'Ad Group Status',
                'Status', 'Approval Status', 'Comment'
            ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)


        fourth_keywords = []
        not_writed_products = []

        for product in products:

            # есть ли у нас моральное право объявление пилить?
            if checkers.check_headline_length(product, not_writed_products):
                continue

            # пилим хедер группы объявлений:
            header = {'Campaign': draft.Campaign,
                             'Audience targeting': draft.Audience_targeting,
                             'Flexible Reach': draft.Flexible_Reach,
                             'Ad Group': product.name,
                             'Max CPC': draft.Max_CPC,
                             'Max CPM': draft.Max_CPM,
                             'Target CPM': draft.Target_CPM,
                             'Display Network Custom Bid Type': draft.Display_Network_Custom_Bid_Type,
                             'Optimized targeting': draft.Optimized_targeting,
                             'Ad Group Type': draft.Ad_Group_Type,
                             }

            writer.writerow(header)

            # генерячим ключи:
            keywords = make_keywords(product.vendor, product.name)
            checkers.is_in_fourth_keywords(keywords, fourth_keywords)

            for keyword in keywords:
                writer.writerow({'Campaign': draft.Campaign,
                                 'Ad Group': product.name,'Ad Group': product.name,
                                 'Keyword': keyword,
                                 'Criterion Type': 'Broad',
                                 })

            # пилим футер группы объявлений
            writer.writerow({'Campaign': draft.Campaign,
                             'Ad Group': product.name,
                             'Final URL': 'https://ipc2u.com/catalog/' + product.url + '/',
                             'Ad type': draft.Ad_type,

                             'Headline 1': product.vendor,
                             'Headline 1 position': '1',
                             'Headline 2': product.name,
                             'Headline 2 position': '2',
                             'Headline 3': product.product_type,
                             'Headline 3 position': '3',
                             'Headline 4': 'buy ' + product.vendor,
                             'Headline 4 position': '1',
                             'Headline 5': product.name,
                             'Headline 5 position': '2',
                             'Headline 6': 'product.product_type GPT',
                             'Headline 6 position': '3',
                             'Headline 7': 'product.Headline_7',
                             'Headline 7 position': '7',
                             'Headline 8': 'product.Headline_8',
                             'Headline 8 position': '8',
                             'Headline 9': 'product.Headline_9',
                             'Headline 9 position': '9',
                             'Headline 10': '',
                             'Headline 10 position': '',
                             'Headline 11': '',
                             'Headline 11 position': '',
                             'Headline 12': '',
                             'Headline 12 position': '',
                             'Headline 13': '',
                             'Headline 13 position': '',
                             'Headline 14': '',
                             'Headline 14 position': '',
                             'Headline 15': '',
                             'Headline 15 position': '',

                             'Description 1': checkers.check_description(product.description_en),
                             'Description 1 position': '',
                             'Description 2': checkers.check_description(product.description_ru),
                             'Description 2 position': '',
                             'Description 3': checkers.check_description(''),
                             'Description 3 position': '',
                             'Description 4': checkers.check_description(''),
                             'Description 4 position': '',
                             'Path 1': draft.Path_1,
                             'Path 2': product.url,

                             })


        with open('NOT_WRITED.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in not_writed_products:
                writer.writerow([item])




