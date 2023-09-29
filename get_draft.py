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



def get_draft(draft_path):
    with open(draft_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        point_row = next(reader)

        draft = Draft(
            Campaign = point_row[0],
            Audience_targeting = point_row[18],
            Flexible_Reach = point_row[19],
            Max_CPC = point_row[21],
            Max_CPM = point_row[22],
            Target_CPM = point_row[25],
            Display_Network_Custom_Bid_Type = point_row[31],
            Optimized_targeting = point_row[32],
            Ad_Group_Type = point_row[33],
            Ad_type = point_row[61],
            Path_1 = point_row[100],
        )
    return draft
