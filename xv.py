import time

def xv_main(params, stopping_backreference):
    while not stopping_backreference():
        time.sleep(10)
        print(f"Erosion: {params['erosion']}")
        print(f"Dilation: {params['dilation']}")
