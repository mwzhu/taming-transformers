lines = []
start = 0
stop = 499

for i in range(start, stop + 1):
    lines.append('/content/taming-transformers/data/BAYC/' + str(i) + '.png')

with open('data/BAYC_train.txt', 'w') as f:
    f.write('\n'.join(lines))
