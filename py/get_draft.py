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

    cell_a = 0
    cell_c = 2
    cell_d = 3
    cell_e = 4
    cell_f = 5
    cell_g = 6
    cell_h = 7
    cell_i = 8
    cell_j = 9
    cell_l = 11
    cell_m = 12
    cell_n = 13
    cell_o = 14
    cell_p = 15
    cell_q = 16
    cell_r = 17

    cell_s = 18
    cell_t = 19
    cell_v = 21
    cell_w = 22
    cell_z = 25
    cell_af = 31
    cell_ag = 32
    cell_ah = 33

    cell_am = 38
    cell_an = 39
    cell_ao = 40

    cell_bg = 58
    cell_bh = 59
    cell_bi = 60

    cell_bj = 61

    draft = Draft(
        campaign=campaign_description[cell_a],
        audience_targeting=campaign_description[cell_s],
        flexible_reach=group_draft[cell_t],
        max_cpc=group_draft[cell_v],
        max_cpm=group_draft[cell_w],
        target_cpm=group_draft[cell_z],
        display_network_custom_bid_type=group_draft[cell_af],
        optimized_targeting=group_draft[cell_ag],
        ad_group_type=group_draft[cell_ah],
        ad_type=campaign_description[cell_bj],
        path1='catalog',

        budget=campaign_header[cell_c],
        budget_type=campaign_header[cell_d],
        standard_conversion_goals=campaign_header[cell_e],
        custom_conversion_goal=campaign_header[cell_f],
        campaign_type=campaign_header[cell_g],
        networks=campaign_header[cell_h],
        languages=campaign_header[cell_i],
        bid_strategy_type=campaign_header[cell_j],
        target_cpa=campaign_header[cell_l],
        start_date=campaign_header[cell_m],
        end_date=campaign_header[cell_n],
        ad_schedule=campaign_header[cell_o],
        ad_rotation=campaign_header[cell_p],
        targeting_method=campaign_header[cell_q],
        exclusion_method=campaign_header[cell_r],

        id=campaign_footer3[cell_am],
        location=campaign_footer3[cell_an],
        reach=campaign_footer3[cell_ao],
        image_size=campaign_footer2[cell_bg],
        link_source=campaign_footer2[cell_bh],
        business_name=campaign_footer1[cell_bi],
    )
    return draft


if __name__ == '__main__':
    draft = get_draft('draft.csv')
