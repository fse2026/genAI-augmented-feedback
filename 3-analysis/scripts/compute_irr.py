import pandas as pd
from pathlib import Path
from sklearn.metrics import cohen_kappa_score

DATA = Path('2-data/derived/ratings_tidy.csv')
OUT_DIR = Path('3-analysis/outputs')
OUT_DIR.mkdir(parents=True, exist_ok=True)

def exact_and_within_one(a, b):
    a = a.astype(int)
    b = b.astype(int)
    exact = (a == b).mean()
    within_one = (abs(a - b) <= 1).mean()
    return exact, within_one

def main():
    df = pd.read_csv(DATA)

    needed = {'unit_id','dimension','rater','score'}
    if not needed.issubset(df.columns):
        raise ValueError(f'ratings_tidy.csv must include columns: {sorted(needed)}')

    # Pairwise agreement per dimension across raters
    raters = sorted(df['rater'].unique())
    if len(raters) < 2:
        raise ValueError('Need at least two raters to compute IRR.')

    out_rows=[]
    for dim, g in df.groupby('dimension'):
        pivot = g.pivot_table(index='unit_id', columns='rater', values='score', aggfunc='first')
        # consider only units rated by all raters
        pivot = pivot.dropna()
        for i in range(len(raters)):
            for j in range(i+1, len(raters)):
                r1, r2 = raters[i], raters[j]
                if r1 not in pivot.columns or r2 not in pivot.columns:
                    continue
                a = pivot[r1].astype(int)
                b = pivot[r2].astype(int)
                kappa_w = cohen_kappa_score(a, b, weights='quadratic')
                exact, within_one = exact_and_within_one(a, b)
                out_rows.append({
                    'dimension': dim,
                    'rater_a': r1,
                    'rater_b': r2,
                    'n_units': len(pivot),
                    'weighted_kappa_quadratic': kappa_w,
                    'exact_agreement': exact,
                    'within_one_agreement': within_one
                })

    out = pd.DataFrame(out_rows)
    out.to_csv(OUT_DIR/'irr_pairwise.csv', index=False)

if __name__ == '__main__':
    main()
