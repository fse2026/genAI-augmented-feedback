import pandas as pd
from pathlib import Path

DATA = Path('2-data/derived/ratings_tidy.csv')
OUT_DIR = Path('3-analysis/outputs')
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA)
    # Expect columns: unit_id, source_id, rater, dimension, score
    if 'score' not in df.columns or 'dimension' not in df.columns:
        raise ValueError('ratings_tidy.csv must include at least: dimension, score')
    # Basic summaries
    summary = (df.groupby('dimension')['score']
                 .agg(['count','mean','std','min','max'])
                 .reset_index())
    summary.to_csv(OUT_DIR/'summary_by_dimension.csv', index=False)

    # If rubric_dimension column exists, also summarize by that
    if 'rubric_dimension' in df.columns:
        s2=(df.groupby('rubric_dimension')['score']
              .agg(['count','mean','std','min','max'])
              .reset_index())
        s2.to_csv(OUT_DIR/'summary_by_rubric_dimension.csv', index=False)

if __name__ == '__main__':
    main()
