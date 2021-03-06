'''
__target__ = 提取FRB 数据
frbname	W	Speak	Fobs	DM	DMGalaxy	DMExcess	l(°)	b(°)  |
'''
data = '''
FRB180311	12	0.2	2.4	1575.6	45.2	1530.4	337.3	-43.7  |
FRB180309	0.576	20.8	11.981	263.47	44.69	218.78	10.9	-45.4  |
FRB180301	3	0.5	1.5	520	155	365	204.4	-6.4  |
FRB171209	2.5	0.92	2.3	1458	13	1445	332.2	6.24  |
FRB170922	26	2.3	59.8	1111	45	1066	45.1	-38.7  |
FRB170827	0.4	50.3	20.12	176.4±0	37	139.4	303.2	-51.7  |
FRB170107	2.6	22.3	57.98	609.5±0.5	35	574.5	266	51.4  |
FRB160608	9	4.3	38.7	682±7	238.3	443.7	254.11	-9.54  |
FRB160410	4	7	28	278±3	57.7	220.3	220.36	27.19  |
FRB160317	21	3	63	1165±11	319.6	845.4	246.05	-0.99  |
FRB160102	3.4	0.5	1.7	2596.1±0.3	13	2583.1	18.9	-60.8  |
FRB151230	4.4	0.42	1.848	960.4±0.5	38	922.4	239	34.8  |
FRB151206	3	0.3	0.9	1909.8±0.6	160	1749.8	32.6	-8.5  |
FRB150807	0.35	128	44.8	266.5±0.1	36.9	229.6	333.89	-53.5959  |
FRB150610	2	0.7	1.4	1593.9±0.6	122	1471.9	278	16.5  |
FRB150418	0.8	2.2	1.76	776.2±0.5	188.5	587.7	232.67	-3.2348  |
FRB150215	2.88	0.7	2.016	1105.6±0.8	427.2	678.4	24.663	5.28092  |
FRB140514	2.8	0.471	1.3188	562.7±0.6	34.9	527.8	50.841	-54.612  |
FRB131104	2.08	1.12	2.3296	779±1	71.1	707.9	260.55	-21.9253  |
FRB130729	15.61	0.22	3.4342	861±2	31	830	324.79	54.7446  |
FRB130628	0.64	1.91	1.2224	469.88±0.01	52.58	417.3	225.96	30.6556  |
FRB130626	1.98	0.74	1.4652	952.4±0.1	66.87	885.53	7.45	27.4203  |
FRB121102	3	0.4	1.2	557±2	188	369	174.95	-0.22514  |
FRB121002	5.44	0.43	2.3392	1629.18±0.02	74.27	1554.91	308.22	-26.2647  |
FRB120127	1.1	0.5	0.55	553.3±0.3	31.82	521.48	49.287	-66.2037  |
FRB110703	4.3	0.5	2.15	1103.6±0.7	32.33	1071.27	80.998	-59.0191  |
FRB110626	1.4	0.4	0.56	723±0.3	47.46	675.54	355.86	-41.7522  |
FRB110523	1.73	0.6	1.038	623.3±0.06	43.52	579.78	56.12	-37.82  |
FRB110220	5.6	1.3	7.28	944.38±0.05	34.77	909.61	50.829	-54.7663  |
FRB090625	1.92	1.14	2.1888	899.55±0.01	31.69	867.86	226.44	-60.0303  |
FRB010724	5	30	150	375	44.58	330.42	300.65	-41.8051  |
FRB010621	7	0.41	2.87	745±10	523	222	25.434	-4.00381  |
FRB010125	9.4	0.3	2.82	790±3	110	680	356.64	-20.0206  |
'''
data.replace("\t"," ")
data.replace("\\t"," ")
data.replace('\n'," ")
data.replace("\r" ," ")
data.replace("\r\n" ,'  ')
data.replace("\\n" ,'  ')
lines = data.split('|')

lines_info = []
for line in lines:
    x = line.split("\t")
    try:
        print(x[7])
        value = float(x[7])+360 if(float(x[7])<180) else float(x[7])-360
        lines_info.append([x[0],value,x[8]])
    except:
        print(x)

color = 1000
import os,random
os.remove('GCs-FASTsky_fbr.txt')
file = open('GCs-FASTsky_fbr.txt','w')

for l in lines_info:

    line = "%s 6171 	%s  %s  0	1	1	%s"%(l[0],l[2],l[1],color)

    print(line,len(line),end=' ')
    if line != '' and len(line) > 10:
        file.write(line)
    color = 100
    # color = random.randint(1, 1000)
file.close()