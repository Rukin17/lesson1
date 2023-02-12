def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'
    

perem = get_summ('Learn'.upper(), 'python'.upper())
print(perem)

