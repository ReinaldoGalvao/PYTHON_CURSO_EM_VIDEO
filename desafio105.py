
def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['ninime'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >7:
            r['sutuação'] = 'BOA'
        elif r['maior'] >= 5:
            r['sutuação'] = 'RAZOÁVEL'
        elif r['media'] < 5:
            r['sutuação'] = 'RUIM'
    return r

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)