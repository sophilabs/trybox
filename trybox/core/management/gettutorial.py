from trybox.core import Context, serialize
import json

def handle(args):
    try:
        module = __import__(args.tutorial)
        print json.dumps({'success': True, 'response': serialize(module.tutorial) })
    except Exception as e:
        print json.dumps({'success': False, 'response': e.message })


def gettutorial(sp_base):
    p_hint = sp_base.add_parser('gettutorial', help='Get Tutorial')
    p_hint.set_defaults(handle=handle)