def calculate_mean_time(time_str):
    if pd.isnull(time_str):
        return np.nan
    match = re.findall(r'\d+', time_str)
    if len(match) == 2:
        return (int(match[0]) + int(match[1])) / 2
    return np.nan