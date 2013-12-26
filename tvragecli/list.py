import logging
import os

from cliff.lister import Lister
import tvrage


class EpisodeList(Lister):
    """list episodes"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(EpisodeList, self).get_parser(prog_name)
        self.app.add_default_args(parser)
        parser.add_argument('--show', help='show id', required=True)
        parser.add_argument('--season', help='season number', required=True,
                            type=int)
        return parser

    def take_action(self, parsed_args):
        client = tvrage.TVRage(api_key=parsed_args.api_key)
        r = client.get_episode_list(parsed_args.show)

        season = r.seasons[parsed_args.season - 1]

        columns = (
            'title',
            'seasonnum',
            'epnum',
            'prodnum',
            'airdate',
            'rating',
            'link',
            'screencap',
        )

        data = []
        for episode in season.episodes:
            data_point = [getattr(episode, column, None) for column in columns]
            data.append(data_point)

        return (columns, data)


class ShowSearchList(Lister):
    """search for tv shows"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(ShowSearchList, self).get_parser(prog_name)
        self.app.add_default_args(parser)
        parser.add_argument('show', help='show name')
        return parser

    def take_action(self, parsed_args):
        client = tvrage.TVRage(api_key=parsed_args.api_key)
        r = client.search(parsed_args.show)

        columns = (
            'name',
            'showid',
            'status',
            'seasons',
            'started',
            'ended',
            'country',
            'classification',
            'link',
        )

        data = []
        for show in r:
            data_point = [getattr(show, column, None) for column in columns]
            data.append(data_point)

        return (columns, data)
