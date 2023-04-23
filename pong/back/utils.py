import os

score_file_path = os.path.dirname(os.path.abspath(__file__)) + "/scores.txt"

def get_sorted_scores():
    global inf
    _inf = []
    inf = []
    with open(score_file_path, 'r') as f:
        for line in f:
            _inf.append(line)
        for x in _inf:
            w = x.split(',')
            x.strip('\n')
            inf.append(w)
        for i, item in enumerate(inf):
            inf[i][1] = item[1].strip("\n")
            inf[i][1] = int(item[1])
            # print(inf)
            if str(i) == str((len(inf)-1)):
                print(inf)
                print(sorted(inf, key = lambda x: int(x[1]), reverse=True))
                return sorted(inf, key = lambda x: int(x[1]), reverse=True)

