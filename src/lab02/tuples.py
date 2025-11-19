def f(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio2 = (" ".join(fio.split()).strip()).split()
    if len(fio2) < 2 or len(group.strip()) == 0 or gpa < 0:
        raise ValueError
    s = ""
    if len(fio2) == 3:
        s = f"{fio2[0].title()} {fio2[1][0].title()}.{fio2[2][0].title()}., "
    else:
        s = f"{fio2[0].title()} {fio2[1][0].title()}., "
    s += f"гр. {group}, "
    s += f"GPA {gpa:.2f}"
    return s
