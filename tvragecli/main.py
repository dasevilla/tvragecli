import logging
import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager


class TVRageApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(TVRageApp, self).__init__(
            description='Command line client for TV Rage',
            version='0.1.0',
            command_manager=CommandManager('tvragecli'),
        )

    def add_default_args(self, parser):
        parser.add_argument(
            '--api-key',
            help='TVRage api key',
            required=False,
            default=os.getenv('TV_RAGE_API_KEY')
        )

def main(argv=sys.argv[1:]):
    myapp = TVRageApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
