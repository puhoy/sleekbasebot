from sleekbasebot import SleekBaseBot
from sleekbasebot.commands import muc
from sleekbasebot.decorators import arguments

import logging
logging.basicConfig(level=logging.DEBUG)


@arguments('first_argument', min=1, usage='')
def command_echo(msg, **kwargs):
    logging.debug('sending echo')
    msg.reply(kwargs['first_argument']).send()


commands = {
    # !help is generated from commands in this dict and their usage
    '!echo': command_echo,
    '!join': muc.command_join_room
}

settings = {
    'admins': ['me@server.tld', 'alsome@server.tld'],
    'autojoin': [['room@conference.server.tld', 'p4ssw0rd'], ['anotherroom@conference.server.tld', 'p@sswOrd']],
    'muc_logging': 'log/path/' # or False
}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--jid", help="the bots jabber id")
    parser.add_argument("--password", help="the bots password (you will be asked if not given)")
    parser.add_argument("--admin", help="admin account (bare, eg. me@server.tld")
    args = parser.parse_args()

    if not args.password:
        import getpass
        args.password = getpass.getpass()

    if not args.admin in settings['admins']:
        settings['admins'].append(args.admin)

    bot = SleekBaseBot(jid=args.jid, password=args.password, commands=commands, settings=settings)
