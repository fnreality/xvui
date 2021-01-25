import kaon
from flask import Flask, request
app = Flask(__name__)

from xv_kaon import XVCtx

@app.route('/')
def page_root():
    return ctx.render(file= 'index.kaon.html')

@app.route('/update', methods= ['POST'])
def page_root_update():
    with ctx.complete(request.form) as concept:
        concept.merge([update_params])
    return ctx.render(file= 'index.kaon.html')

ctx = kaon.Context({
    'xv': XVCtx()
})

def update_params(ctx, req):
    #TODO#

if __name__ == '__main__':
    ctx.start_reality()
    app.run(port= 8087)
