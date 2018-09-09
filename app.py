from aiohttp import web
import json
import logging
import os


log = logging.getLogger(__name__)
level = logging.INFO
if json.load(open('config.json')).get('debug', False):
    level = logging.DEBUG
logging.basicConfig(format='%(asctime)s %(message)s', level=level)


async def file_handle(request):
    try:
        data = await request.post()
        config = json.load(open('config.json'))
        return web.FileResponse(os.path.join('content', config.get('keys', {})[data['key']]))
    except KeyError as e:
        log.debug(e)
        return web.Response(status=403)


app = web.Application()
app.add_routes([web.post('/', file_handle)])
web.run_app(app)
