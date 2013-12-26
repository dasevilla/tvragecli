import logging

from cliff.show import ShowOne


class EpisodeInfo(ShowOne):
    """episode details"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(EpisodeInfo, self).get_parser(prog_name)
        parser.add_argument('--show', help='show id', required=True)
        parser.add_argument('--season', help='season number', required=True,
                            type=int)
        parser.add_argument('--episode', help='episode number', required=True,
                            type=int)
        return parser

    def take_action(self, parsed_args):

        r = self.app.client.get_episodeinfo(
            parsed_args.show,
            parsed_args.season,
            parsed_args.episode
        )

        columns = r.episode.keys()
        data = r.episode.values()

        return (columns, data)


class ShowInfo(ShowOne):
    """tv show details"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(ShowInfo, self).get_parser(prog_name)
        parser.add_argument('show', help='show id')
        return parser

    def take_action(self, parsed_args):

        r = self.app.client.get_showinfo(parsed_args.show)

        columns = [
            'showname',
            'showid',
            'image',
            'origin_country',
            'status',
            'airtime',
            'airday',
            'timezone',

            'seasons',
            'started',
            'runtime',
            'classification',
            'showlink',

            'startdate',
            'ended',
        ]

        data = [getattr(r, column, None) for column in columns]

        return (columns, data)
