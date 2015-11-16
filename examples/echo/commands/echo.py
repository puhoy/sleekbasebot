from sleekbasebot.decorators import arguments, admin_only

import logging
logging.basicConfig(level=logging.DEBUG)

@arguments('first_argument', min=0, usage='!echo')
def command_echo(msg, **kwargs):
    logging.debug('sending echo')
    msg.reply(kwargs['first_argument']).send()


@admin_only(reply_string='you are no admin!')
@arguments('first_argument', min=1, usage='!aecho')
def command_admin_echo(msg, **kwargs):
    logging.debug('sending echo')
    msg.reply('admin ' + kwargs['first_argument']).send()
