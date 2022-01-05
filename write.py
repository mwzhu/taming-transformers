lines = []
start = 500
stop = 635

for i in range(start, stop + 1):
    lines.append('/content/taming-transformers/data/BAYC_test/' + str(i) + '.png')

with open('data/BAYC_test.txt', 'w') as f:
    f.write('\n'.join(lines))
