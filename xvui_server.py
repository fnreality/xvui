import kaon
from xvkaon import XVEntity
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def page_root():
    return ctx.render(file= 'index.kaon.html')

@app.route('/update', methods= ['POST'])
def page_root_update():
    with ctx.complete(request.form) as concept:
        concept.merge(map(
            lambda x: ParamUpdate(x).instant,
            [ 'erosion', 'dilation' ]
        ))
    return ctx.render(file= 'index.kaon.html')

default_params = {
    'erosion': 0,
    'dilation': 0
}

ctx = kaon.Context({
    'xv': XVEntity(default_params)
})

class ParamUpdate(object):
    def __init__(self, param):
        super(ParamUpdate, self).__init__()
        self.param = param
        
    def instant(self, ctx, data):
        param = self.param
        return 'xv', {
            **ctx['xv'],
            **{ param: int(req[f'xv-{param}']) }
        }

if __name__ == '__main__':
    ctx.start_reality()
    app.run(port= 2422)
