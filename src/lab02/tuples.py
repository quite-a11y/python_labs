def f(fio,group,gpa):
    fio2 = ''.join(fio)
    fio2 = fio2.split()
    if len(fio2) < 2 or len(group) == 0 or gpa < 0 or type(gpa) not in (float, int):
        raise ValueError
    s = ''
    if len(fio2) == 3:
        s = f'{fio2[0].title()} {fio2[1][0].title()}.{fio2[2][0].title()}., '
    else:
        s = f'{fio2[0].title()} {fio2[1][0].title()}., '
    s += f'гр. {group}, '
    s += f'GPA {gpa:.2f}'
    return s








