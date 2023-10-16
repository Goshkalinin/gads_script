"""Подхватываем шаблонные значения из шаблона Google Ads."""

import csv
from dataclasses import dataclass


@dataclass
class Draft(object):
    """Так и назовём: шаблон."""

    campaign: str
    audience_targeting: str
    flexible_reach: str
    max_cpc: str
    max_cpm: str
    target_cpm: str
    display_network_custom_bid_type: str
    optimized_targeting: str
    ad_group_type: str
    ad_type: str
    path1: str

    budget: str
    budget_type: str
    standard_conversion_goals: str
    custom_conversion_goal: str
    campaign_type: str
    networks: str
    languages: str
    bid_strategy_type: str
    target_cpa: str
    start_date: str
    end_date: str
    ad_schedule: str
    ad_rotation: str
    targeting_method: str
    exclusion_method: str

    id: str
    location: str
    reach: str
    image_size: str
    link_source: str
    business_name: str


def get_draft(draft_path):
    """
    Записываем значения из шаблона.

    Args:
        draft_path (str): путь до csv-ки с файлами.

    Returns:
        draft (object): класс с шаблонными значениями.

    """
    rows = []
    with open(draft_path, 'r', encoding='utf-8') as cvs_file:
        reader = csv.reader(cvs_file, delimiter=',')
        for row in reader:
            rows.append(row)

    campaign_header = rows[1]
    campaign_description = rows[1]
    group_draft = rows[2]
    campaign_footer1 = rows[-1]
    campaign_footer2 = rows[-2]
    campaign_footer3 = rows[-3]

    draft = Draft(
        campaign=campaign_description[0],
        audience_targeting=campaign_description[18],
        flexible_reach=group_draft[19],
        max_cpc=group_draft[21],
        max_cpm=group_draft[22],
        target_cpm=group_draft[25],
        display_network_custom_bid_type=group_draft[31],
        optimized_targeting=group_draft[32],
        ad_group_type=group_draft[33],
        ad_type=campaign_description[61],
        path1='catalog',

        budget=campaign_header[2],
        budget_type=campaign_header[3],
        standard_conversion_goals=campaign_header[4],
        custom_conversion_goal=campaign_header[5],
        campaign_type=campaign_header[6],
        networks=campaign_header[7],
        languages=campaign_header[8],
        bid_strategy_type=campaign_header[9],
        target_cpa=campaign_header[11],
        start_date=campaign_header[12],
        end_date=campaign_header[13],
        ad_schedule=campaign_header[14],
        ad_rotation=campaign_header[15],
        targeting_method=campaign_header[16],
        exclusion_method=campaign_header[17],

        id=campaign_footer3[38],
        location=campaign_footer3[39],
        reach=campaign_footer3[40],
        image_size=campaign_footer2[58],
        link_source=campaign_footer2[59],
        business_name=campaign_footer1[60],
    )
    return draft


if __name__ == '__main__':
    draft = get_draft('draft.csv')
