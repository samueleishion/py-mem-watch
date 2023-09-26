import subprocess
import time

from dependencies.logr import * 

def parse(lines):
    d = {} 

    head = list(filter(lambda x : len(x) > 0, lines[0].split(' ')))
    body = [list(filter(lambda y : len(y) > 0, x.split(' '))) for x in lines[1:]]

    # logr.data(str(head))
    # logr.data(str(body))

    for b in body:
        if (len(b) == 0):
            continue 

        mem = b[0]
        row = b[1:] 
        d[mem] = {}

        for h in head:
            d[mem][h] = None 

        for i in range(len(row)):
            b = row[i] 
            h = head[i] 
            d[mem][h] = int(b)

    # logr.data(str(d))
    return d 

def chart(percentage=0, size=10):
    block_done = '█'
    block_todo = '░' 

    chart_done = block_done * round(percentage * size) 
    chart_todo = block_todo * round((1 - percentage) * size) 

    return f'[{chart_done}{chart_todo}]' 

def get_memory():
    output = subprocess.run(['free', '-m'], stdout=subprocess.PIPE)
    # logr.test(str(output.stdout.decode('utf-8')))
    lines = str(output.stdout.decode('utf-8')).split('\n')
    # for line in lines:
    #    logr.test(line)

    values = parse(lines)

    stats = ''
    for mem in values:
        used = values[mem]["used"]
        total = values[mem]["total"]
        percent = used/total
        bar = chart(percent)
        p = "{:.2f}".format(percent * 100)
        stats += f'{mem} {used}/{total} {bar} {p}%   '

    return stats 

def main():
    logr.info("Mamory watch")

    while True: 
        render = get_memory() 
        logr.live(render)
        time.sleep(1) 

    logr.pause()

if __name__ == '__main__': 
    main()
