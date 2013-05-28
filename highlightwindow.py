__module_name__ = "HighlightWindow"
__module_version__ = "1.0"
__module_description__ = "A simple plugin to aggregate all highlights into a single, easy to read window."

print "\0034", __module_name__, __module_version__, "has been loaded\003"

import xchat


def highlight(word, word_eol, userdata):
    context = xchat.get_context()
    context.command('query -nofocus @highlight')

    nick = word[0]
    message = word_eol[1]
    channel = context.get_info("channel")
    server = context.get_info('server')

    query = xchat.find_context(server, '@highlight')
    query.prnt('[' + channel + '] <' + nick + '> ' + message[:-2])
    query.command("GUI COLOR 3")

xchat.hook_print('Channel Msg Hilight', highlight)
xchat.hook_print('Channel Action Hilight', highlight)
