# R2 Scored

def r2_score(yTrue,yPred):
    mean_yTrue = sum(yTrue)/len(yTrue)
    ss_tot = sum([(x - mean_yTrue)**2 for x in yTrue])
    ss_res = sum([(x - y)**2 for x,y in zip(yTrue,yPred)])
    r2 = 1 - (ss_res / ss_tot)
    return r2

x = [1,2,3,4,5]
y = [1.2,2.2,2.8,3.7,4.5]

print(r2_score(x,y))
