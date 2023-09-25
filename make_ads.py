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
        Final_URL = product.url,
        Final_mobile_URL = '',
        Image_Size = '',
        Link_source = '',
        Business_name = '',
        Ad_type = draft.Ad_type,
        Headline_1 = checkers.check_headline(product.vendor),
        Headline_1_position = '1',
        Headline_2 = checkers.check_headline(product.name),
        Headline_2_position = '2',
        Headline_3 = checkers.check_headline(product.product_type),
        Headline_3_position = '3',
        Headline_4 = checkers.check_headline('buy ' + product.vendor),
        Headline_4_position = '1',
        Headline_5 = checkers.check_headline(product.name),
        Headline_5_position = '2',
        Headline_6 = checkers.check_headline('product.product_type REWRITED BY GPT'),
        Headline_6_position = '3',
        Headline_7 = checkers.check_headline(''),
        Headline_7_position = '',
        Headline_8 = checkers.check_headline(''),
        Headline_8_position = '',
        Headline_9 = checkers.check_headline(''),
        Headline_9_position = '',
        Headline_10 = checkers.check_headline(''),
        Headline_10_position = '',
        Headline_11 = checkers.check_headline(''),
        Headline_11_position = '',
        Headline_12 = checkers.check_headline(''),
        Headline_12_position = '',
        Headline_13 = checkers.check_headline(''),
        Headline_13_position = '',
        Headline_14 = checkers.check_headline(''),
        Headline_14_position = '',
        Headline_15 = checkers.check_headline(''),
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

    keyword = vendor + name
    keywords.append(keyword)

    keyword = (vendor + name).split('-')[-1]
    keywords.append(keyword)

    return keywords


def make_ads(product_list, draft):
    with open('final.csv', 'w') as file:
        header = (
            "Campaign", "Labels", "Budget", "Budget type", "Standard conversion goals",
            "Custom conversion goal", "Campaign Type", "Networks", "Languages",
            "Bid Strategy Type", "Bid Strategy Name", "Target CPA", "Start Date",
            "End Date", "Ad Schedule", "Ad rotation", "Targeting method",
            "Exclusion method", "Audience targeting", "Flexible Reach", "Ad Group",
            "Max CPC", "Max CPM", "Max CPV", "Percent CPC", "Target CPM",
            "Target ROAS", "Desktop Bid Modifier", "Mobile Bid Modifier",
            "Tablet Bid Modifier", "TV Screen Bid Modifier",
            "Display Network Custom Bid Type", "Optimized targeting",
            "Ad Group Type", "Audience name", "Tracking template",
            "Final URL suffix", "Custom parameters", "ID", "Location", "Reach",
            "Location groups", "Location groups legacy", "Feed", "Radius", "Unit",
            "Bid Modifier", "Keyword", "Criterion Type", "First page bid",
            "Top of page bid", "First position bid", "Quality score",
            "Landing page experience", "Expected CTR", "Ad relevance",
            "Final URL", "Final mobile URL", "Image Size", "Link source",
            "Business name", "Ad type", "Headline 1", "Headline 1 position",
            "Headline 2", "Headline 2 position", "Headline 3",
            "Headline 3 position", "Headline 4", "Headline 4 position",
            "Headline 5", "Headline 5 position", "Headline 6",
            "Headline 6 position", "Headline 7", "Headline 7 position",
            "Headline 8", "Headline 8 position", "Headline 9",
            "Headline 9 position", "Headline 10", "Headline 10 position",
            "Headline 11", "Headline 11 position", "Headline 12",
            "Headline 12 position", "Headline 13", "Headline 13 position",
            "Headline 14", "Headline 14 position", "Headline 15",
            "Headline 15 position", "Description 1", "Description 1 position",
            "Description 2", "Description 2 position", "Description 3",
            "Description 3 position", "Description 4", "Description 4 position",
            "Path 1", "Path 2", "Campaign Status", "Ad Group Status",
            "Status", "Approval Status", "Comment"
        )

        writer = csv.writer(file)
        writer.writerow(header)

        for product in product_list:
            keywords = make_keywords(product.vendor, product.name)
            for keyword in keywords:

                ad = make_ad_object(product, draft, keyword)
                #тут нихера не просто так кортеж, держу в курсе
                #сто, блин, колонок, они там нормальлные ваще?!
                row = (
                    ad.Campaign,
                    ad.Labels,
                    ad.Budget,
                    ad.Budget_type,
                    ad.Standard_conversion_goals,
                    ad.Custom_conversion_goal,
                    ad.Campaign_Type,
                    ad.Networks,
                    ad.Languages,
                    ad.Bid_Strategy_Type,
                    ad.Bid_Strategy_Name,
                    ad.Target_CPA,
                    ad.Start_Date,
                    ad.End_Date,
                    ad.Ad_Schedule,
                    ad.Ad_Rotation,
                    ad.Targeting_method,
                    ad.Exclusion_method,
                    ad.Audience_targeting,
                    ad.Flexible_Reach,
                    ad.Ad_Group,
                    ad.Max_CPC,
                    ad.Max_CPM,
                    ad.Max_CPV,
                    ad.Percent_CPC,
                    ad.Target_CPM,
                    ad.Target_ROAS,
                    ad.Desktop_Bid_Modifier,
                    ad.Mobile_Bid_Modifier,
                    ad.Tablet_Bid_Modifier,
                    ad.TV_Screen_Bid_Modifier,
                    ad.Display_Network_Custom_Bid_Type,
                    ad.Optimized_targeting,
                    ad.Ad_Group_Type,
                    ad.Audience_name,
                    ad.Tracking_template,
                    ad.Final_URL_suffix,
                    ad.Custom_parameters,
                    ad.ID,
                    ad.Location,
                    ad.Reach,
                    ad.Location_groups,
                    ad.Location_groups_legacy,
                    ad.Feed,
                    ad.Radius,
                    ad.Unit,
                    ad.Bid_Modifier,
                    ad.Keyword,
                    ad.Criterion_Type,
                    ad.First_page_bid,
                    ad.Top_of_page_bid,
                    ad.First_position_bid,
                    ad.Quality_score,
                    ad.Landing_page_experience,
                    ad.Expected_CTR,
                    ad.Ad_relevance,
                    ad.Final_URL,
                    ad.Final_mobile_URL,
                    ad.Image_Size,
                    ad.Link_source,
                    ad.Business_name,
                    ad.Ad_type,
                    ad.Headline_1,
                    ad.Headline_1_position,
                    ad.Headline_2,
                    ad.Headline_2_position,
                    ad.Headline_3,
                    ad.Headline_3_position,
                    ad.Headline_4,
                    ad.Headline_4_position,
                    ad.Headline_5,
                    ad.Headline_5_position,
                    ad.Headline_6,
                    ad.Headline_6_position,
                    ad.Headline_7,
                    ad.Headline_7_position,
                    ad.Headline_8,
                    ad.Headline_8_position,
                    ad.Headline_9,
                    ad.Headline_9_position,
                    ad.Headline_10,
                    ad.Headline_10_position,
                    ad.Headline_11,
                    ad.Headline_11_position,
                    ad.Headline_12,
                    ad.Headline_12_position,
                    ad.Headline_13,
                    ad.Headline_13_position,
                    ad.Headline_14,
                    ad.Headline_14_position,
                    ad.Headline_15,
                    ad.Headline_15_position,
                    ad.Description_1,
                    ad.Description_1_position,
                    ad.Description_2,
                    ad.Description_2_position,
                    ad.Description_3,
                    ad.Description_3_position,
                    ad.Description_4,
                    ad.Description_4_position,
                    ad.Path_1,
                    ad.Path_2,
                    ad.Campaign_Status,
                    ad.Ad_Group_Status,
                    ad.Status,
                    ad.Approval_Status,
                    ad.Comment,
                )
                writer.writerow(row)







if __name__ == "__main__":
    from get_products import get_products
    products = get_products()
    draft = get_draft()
    make_ads_(products, draft)
