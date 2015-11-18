# sleekbasebot

### sleekxmpp bot mini framework

just add settings and implement commands.

    from sleekbasebot.decorators import arguments, admin_only
    from sleekbasebot.commands import help
    from sleekbasebot import SleekBaseBot
    import logging
    
    @admin_only(reply_string='you are no admin!')
    @arguments('first_argument', min=1, usage='!echo <argument_to_echo>\necho the first argument')
    def command_echo(msg, **kwargs):
        logging.debug('sending echo')
        msg.reply(kwargs['first_argument']).send()
    
    commands = {
        #'command-trigger_in_chat': executed_command,
        '!echo': command_echo,
        '!help': help.command_help # help generates a dynamic help from usage in commands
        }
    
    settings = {
        'admins': ['me@server.tld', 'alsome@server.tld'],
        'autojoin': [['room@conference.server.tld', 'p4ssw0rd'], ['anotherroom@conference.server.tld', 'p@sswOrd']],
        'muc_logging': 'log/path/' # or False
        }
    
    
    if __name__ == '__main__':
        bot = SleekBaseBot(jid='me@server.tld', password='p4ssw0rd', commands=commands, settings=settings)

        if bot.connect():
            bot.process(blocking=False)
        else:
            print("Unable to connect.")


see examples for a better echobot :)
