x=range(1,9)

for i in range(1,10):
    print('y=β_0+'+'+'.join(['β_{}*x_{}'.format(j,j)for j in range(1,i)])+'+ε')
