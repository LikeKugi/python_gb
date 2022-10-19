# Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.


with open('polynomes.txt', 'r') as inf:
    polynomes = [el.replace('-', '+ -').split(" + ") for el in map(str.rstrip, inf.readlines())]

max_power = 0
for i in range(len(polynomes)):
    if '^' in polynomes[i][0] and int(polynomes[i][0][polynomes[i][0].find('^') + 1:]) > max_power:
        max_power = int(polynomes[i][0][polynomes[i][0].find('^') + 1:])
    elif 'x' in polynomes[i][0] and max_power == 0:
        max_power = 1

result_polynome = [0] * (max_power + 1)

for i in range(len(result_polynome)):
    for j in range(len(polynomes)):
        if not polynomes[j]:
            continue
        current_power = i
        if current_power == 0:
            if polynomes[j][-1].isdigit():
                result_polynome[i] += int(polynomes[j].pop())
        elif current_power == 1:
            if polynomes[j][-1].endswith('x'):
                element = polynomes[j].pop().replace(' ','')
                if element.find('x') == 0:
                    result_polynome[i] += 1
                else:
                    result_polynome[i] += int(element[:element.find('x')])
        else:
            if polynomes[j][-1].endswith(str(current_power)):
                element = polynomes[j].pop().replace(' ','')
                if element.find('x') == 0:
                    result_polynome[i] += 1
                else:
                    result_polynome[i] += int(element[:element.find('x')])

for i in range(len(result_polynome)):
    if result_polynome[i] == 0:
        continue
    if i == 0:
        result_polynome[i] = str(result_polynome[i])
    elif i == 1:
        result_polynome[i] = str(result_polynome[i]) + str(f'x')
    else:
        result_polynome[i] = str(result_polynome[i]) + str(f'x^{i}')

res_str = ''
while len(result_polynome) != 0:
    element = result_polynome.pop()
    if element == 0:
        continue
    if element[0] == '-':
        if len(res_str) == 0:
            res_str += element
        else:
            res_str += f' - {element[1:]}'
    else:
        if len(res_str) == 0:
            res_str += element
        else:
            res_str += f' + {element}'

print(res_str)
