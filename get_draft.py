import csv
from dataclasses import dataclass


@dataclass
class Draft:
    Campaign: str
    Audience_targeting: str
    Flexible_Reach: str
    Max_CPC: str
    Max_CPM: str
    Target_CPM: str
    Display_Network_Custom_Bid_Type: str
    Optimized_targeting: str
    Ad_Group_Type: str
    Ad_type: str
    Path_1: str

    Budget: str
    Budget_type: str
    Standard_conversion_goals: str
    Custom_conversion_goal: str
    Campaign_Type: str
    Networks: str
    Languages: str
    Bid_Strategy_Type: str
    Target_CPA: str
    Start_Date: str
    End_Date: str
    Ad_Schedule: str
    Ad_rotation: str
    Targeting_method: str
    Exclusion_method: str

    ID: str
    Location: str
    Reach: str
    Image_Size: str
    Link_source: str
    Business_name: str



def get_draft(draft_path):
    rows = []
    with open(draft_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            rows.append(row)

    campaign_header = rows[0]
    campaign_description = rows[1]
    campaign_footer_1 = rows[-1]
    campaign_footer_2 = rows[-2]
    campaign_footer_3 = rows[-3]

    #print(campaign_header)
    #print(campaign_description)
    #print(campaign_footer_1)
    #print(campaign_footer_2)
    #print(campaign_footer_3)

    draft = Draft(
        Campaign = campaign_description[0],
        Audience_targeting = campaign_description[18],
        Flexible_Reach = campaign_description[19],
        Max_CPC = campaign_description[21],
        Max_CPM = campaign_description[22],
        Target_CPM = campaign_description[25],
        Display_Network_Custom_Bid_Type = campaign_description[31],
        Optimized_targeting = campaign_description[32],
        Ad_Group_Type = campaign_description[33],
        Ad_type = campaign_description[61],
        Path_1 = campaign_description[100],

        Budget = campaign_header[2],
        Budget_type = campaign_header[3],
        Standard_conversion_goals = campaign_header[4],
        Custom_conversion_goal = campaign_header[5],
        Campaign_Type = campaign_header[6],
        Networks = campaign_header[7],
        Languages = campaign_header[8],
        Bid_Strategy_Type = campaign_header[9],
        Target_CPA = campaign_header[11],
        Start_Date = campaign_header[12],
        End_Date = campaign_header[13],
        Ad_Schedule = campaign_header[14],
        Ad_rotation = campaign_header[15],
        Targeting_method = campaign_header[16],
        Exclusion_method = campaign_header[17],
        ID = campaign_footer_3[38],
        Location = campaign_footer_3[39],
        Reach = campaign_footer_3[40],
        Image_Size = campaign_footer_2[58],
        Link_source = campaign_footer_2[59],
        Business_name = campaign_footer_1[60],

    )
    return draft


if __name__ == '__main__':
    get_draft('draft.csv')
