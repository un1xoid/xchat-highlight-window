import xchat

__module_name__ = "HighlightWindow"
__module_version__ = "1.1"
__module_description__ = "A simple plugin to aggregate all highlights into a single, easy to read window."

xchat.prnt('\0034%(name)s, version %(version)s has been loaded\003' % {'name': __module_name__,  'version': __module_version__})


def highlight(word, word_eol, userdata):
    context = xchat.get_context()
    context.command('query -nofocus @highlight')

    nick = word[0]
    message = word_eol[1]
    channel = context.get_info("channel")
    server = context.get_info('server')

    query = xchat.find_context(server, '@highlight')
    query.prnt('[' + channel + '] <' + nick + '> ' + message)
    query.command("GUI COLOR 3")


def highlight_private(word, word_eol, userdata, private=False):
    context = xchat.get_context()
    context.command('query -nofocus @highlight')

    nick = word[0]
    message = word_eol[1]
    server = context.get_info('server')

    query = xchat.find_context(server, '@highlight')
    query.prnt('[private msg] <' + nick + '> ' + message)
    query.command("GUI COLOR 3")


xchat.hook_print('Channel Msg Hilight', highlight)
xchat.hook_print('Channel Action Hilight', highlight)
#xchat.hook_print('Private Message', highlight)
xchat.hook_print('Private Message to Dialog', highlight_private)
