def ft_tqdm(lst: range) -> None:
    ''' Reproduces the tqdm python function
    '''

    tot = len(lst)
    for val in lst:
        yield val
        progress = val / tot
        perc = round(progress * 100)
        tot_hash = round(253 * progress)
        print("\033[K", end='', flush=True)
        bar = f"\r{perc}%|[{'#'*tot_hash}>]|{val+1}/{tot}"
        print(bar, end='', flush=True)
