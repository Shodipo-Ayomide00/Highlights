import dateparser
from django.core.management.base import BaseCommand

from fb_bot.highlight_fetchers import hoofoot_fetcher, footyroom_fetcher
from fb_bot.model_managers import latest_highlight_manager


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Footyroom + Hoofoot highlights fetching
        highlights = footyroom_fetcher.fetch_highlights(num_pagelet=10, max_days_ago=1000) \
                     + hoofoot_fetcher.fetch_highlights(num_pagelet=10, max_days_ago=1000)

        # Add new highlights
        for highlight in highlights:
            # Parse the date before inserting it (date needs to be a string)
            highlight.time_since_added = str(dateparser.parse(highlight.time_since_added))

            if not latest_highlight_manager.has_highlight(highlight):
                latest_highlight_manager.add_highlight(highlight, sent=True)