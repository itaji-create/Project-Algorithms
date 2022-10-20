def study_schedule(permanence_period, target_time):
    if isinstance(target_time, int):
        qtd = 0
        for p in permanence_period:
            if isinstance(p[1], int) and isinstance(p[0], int):
                if p[0] <= target_time <= p[1]:
                    qtd += 1
            else:
                return None
        return qtd
    else:
        return None
