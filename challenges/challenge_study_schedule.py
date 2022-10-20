def study_schedule(permanence_period, target_time):
    qtd = 0
    try:
        for p in permanence_period:
            if int(target_time) in range(p[0], p[1]+1):
                qtd += 1
        return qtd
    except TypeError:
        return None
