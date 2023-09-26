import csv

def write_ads(ads_list):
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

        for ad in ads_list:
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
