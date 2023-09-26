import csv
from dataclasses import dataclass

import checkers


@dataclass
class Ad:
    Campaign: str
    Labels: str
    Budget: str
    Budget_type: str
    Standard_conversion_goals: str
    Custom_conversion_goal: str
    Campaign_Type: str
    Networks: str
    Languages: str
    Bid_Strategy_Type: str
    Bid_Strategy_Name: str
    Target_CPA: str
    Start_Date: str
    End_Date: str
    Ad_Schedule: str
    Ad_Rotation: str
    Targeting_method: str
    Exclusion_method: str
    Audience_targeting: str
    Flexible_Reach: str
    Ad_Group: str
    Max_CPC: str
    Max_CPM: str
    Max_CPV: str
    Percent_CPC: str
    Target_CPM: str
    Target_ROAS: str
    Desktop_Bid_Modifier: str
    Mobile_Bid_Modifier: str
    Tablet_Bid_Modifier: str
    TV_Screen_Bid_Modifier: str
    Display_Network_Custom_Bid_Type: str
    Optimized_targeting: str
    Ad_Group_Type: str
    Audience_name: str
    Tracking_template: str
    Final_URL_suffix: str
    Custom_parameters: str
    ID: str
    Location: str
    Reach: str
    Location_groups: str
    Location_groups_legacy: str
    Feed: str
    Radius: str
    Unit: str
    Bid_Modifier: str
    Keyword: str
    Criterion_Type: str
    First_page_bid: str
    Top_of_page_bid: str
    First_position_bid: str
    Quality_score: str
    Landing_page_experience: str
    Expected_CTR: str
    Ad_relevance: str
    Final_URL: str
    Final_mobile_URL: str
    Image_Size: str
    Link_source: str
    Business_name: str
    Ad_type: str
    Headline_1: str
    Headline_1_position: str
    Headline_2: str
    Headline_2_position: str
    Headline_3: str
    Headline_3_position: str
    Headline_4: str
    Headline_4_position: str
    Headline_5: str
    Headline_5_position: str
    Headline_6: str
    Headline_6_position: str
    Headline_7: str
    Headline_7_position: str
    Headline_8: str
    Headline_8_position: str
    Headline_9: str
    Headline_9_position: str
    Headline_10: str
    Headline_10_position: str
    Headline_11: str
    Headline_11_position: str
    Headline_12: str
    Headline_12_position: str
    Headline_13: str
    Headline_13_position: str
    Headline_14: str
    Headline_14_position: str
    Headline_15: str
    Headline_15_position: str
    Description_1: str
    Description_1_position: str
    Description_2: str
    Description_2_position: str
    Description_3: str
    Description_3_position: str
    Description_4: str
    Description_4_position: str
    Path_1: str
    Path_2: str
    Campaign_Status: str
    Ad_Group_Status: str
    Status: str
    Approval_Status: str
    Comment: str

def make_ad_object(product, draft, keyword):
    ad_object = Ad(
        Campaign = draft.Campaign,
        Labels = '',
        Budget = '',
        Budget_type = '',
        Standard_conversion_goals = '',
        Custom_conversion_goal = '',
        Campaign_Type = '',
        Networks = '',
        Languages = '',
        Bid_Strategy_Type = '',
        Bid_Strategy_Name = '',
        Target_CPA = '',
        Start_Date = '',
        End_Date = '',
        Ad_Schedule = '',
        Ad_Rotation = '',
        Targeting_method = '',
        Exclusion_method = '',
        Audience_targeting = draft.Audience_targeting,
        Flexible_Reach = draft.Flexible_Reach,
        Ad_Group = product.name,
        Max_CPC = draft.Max_CPC,
        Max_CPM = draft.Max_CPM,
        Max_CPV = '',
        Percent_CPC = '',
        Target_CPM = draft.Target_CPM,
        Target_ROAS = '',
        Desktop_Bid_Modifier = '',
        Mobile_Bid_Modifier = '',
        Tablet_Bid_Modifier = '',
        TV_Screen_Bid_Modifier = '',
        Display_Network_Custom_Bid_Type = draft.Display_Network_Custom_Bid_Type,
        Optimized_targeting = draft.Optimized_targeting,
        Ad_Group_Type = draft.Ad_Group_Type,
        Audience_name = '',
        Tracking_template = '',
        Final_URL_suffix = '',
        Custom_parameters = '',
        ID = '',
        Location = '',
        Reach = '',
        Location_groups = '',
        Location_groups_legacy = '',
        Feed = '',
        Radius = '',
        Unit = '',
        Bid_Modifier = '',
        Keyword = keyword,
        Criterion_Type = 'Broad',
        First_page_bid = '',
        Top_of_page_bid = '',
        First_position_bid = '',
        Quality_score = '',
        Landing_page_experience = '',
        Expected_CTR = '',
        Ad_relevance = '',
        Final_URL =  'https://ipc2u.com/catalog/' + product.url + '/',
        Final_mobile_URL = '',
        Image_Size = '',
        Link_source = '',
        Business_name = '',
        Ad_type = draft.Ad_type,
        Headline_1 = product.vendor,
        Headline_1_position = '1',
        Headline_2 = product.name,
        Headline_2_position = '2',
        Headline_3 = product.product_type,
        Headline_3_position = '3',
        Headline_4 = 'buy ' + product.vendor,
        Headline_4_position = '1',
        Headline_5 = product.name,
        Headline_5_position = '2',
        Headline_6 = 'product.product_type GPT',
        Headline_6_position = '3',
        Headline_7 = '',
        Headline_7_position = '',
        Headline_8 = '',
        Headline_8_position = '',
        Headline_9 = '',
        Headline_9_position = '',
        Headline_10 = '',
        Headline_10_position = '',
        Headline_11 = '',
        Headline_11_position = '',
        Headline_12 = '',
        Headline_12_position = '',
        Headline_13 = '',
        Headline_13_position = '',
        Headline_14 = '',
        Headline_14_position = '',
        Headline_15 = '',
        Headline_15_position = '',
        Description_1 = checkers.check_description(product.description_en),
        Description_1_position = '',
        Description_2 = checkers.check_description(product.description_ru),
        Description_2_position = '',
        Description_3 = checkers.check_description(''),
        Description_3_position = '',
        Description_4 = checkers.check_description(''),
        Description_4_position = '',
        Path_1 = draft.Path_1,
        Path_2 = '',
        Campaign_Status = '',
        Ad_Group_Status = '',
        Status = '',
        Approval_Status = '',
        Comment = '',
    )

    return ad_object


def make_keywords(vendor, name):
    keywords = []

    keyword = name
    keywords.append(keyword)

    keyword = name.replace('-', '')
    keywords.append(keyword)

    keyword = vendor + " " + name
    keywords.append(keyword)

    keyword = vendor + " " + name
    parts = keyword.split('-')
    keyword = '-'.join(parts[:-1])
    keywords.append(keyword)

    return keywords


def generate_ads(product_list, draft):
    ads = []
    fourth_keywords = []
    not_writed_products = []

    for product in product_list:
        keywords = make_keywords(product.vendor, product.name)
        checkers.is_in_fourth_keywords(keywords, fourth_keywords)

        for keyword in keywords:
            ad = make_ad_object(product, draft, keyword)
            # EСЛИ дохуя длинно: пропускаем итерацию
            if checkers.check_headline_length(ad, not_writed_products):
                continue
            ads.append(ad)

    with open("NOT_WRITED.csv", "w") as file:
        pass


    return ads




if __name__ == "__main__":
    from get_products import get_products
    from get_draft import get_draft
    products = get_products("data.csv")
    draft = get_draft("draft.csv")
    generate_ads(products, draft)
