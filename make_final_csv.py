import csv

def make_final_csv():
    with open('final.csv', 'w', newline='') as csvfile:
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


        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    make_final_csv()
