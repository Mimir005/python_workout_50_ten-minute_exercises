

def run_timing():
    rec = []
    while True:
        times = input('Enter 10 km run time: ')
        if not times:
            break
        else:
            rec.append(float(times))
    print(f'Average of {sum(rec) / len(rec):.1f}, over {len(rec)} runs')

run_timing()