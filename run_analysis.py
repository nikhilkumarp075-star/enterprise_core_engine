from pathlib import Path
import csv, math, random, statistics
ROOT=Path(__file__).resolve().parents[1]
random.seed(42)
rows=[]
for i in range(10000):
    x=random.uniform(-10,10)
    y=2*x*x-3*x+5+random.gauss(0,2)
    rows.append((i,round(x,6),round(y,6)))
with (ROOT/'data'/'synthetic_quadratic_10000.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','x','y']);w.writerows(rows)
xs=[r[1] for r in rows];ys=[r[2] for r in rows]
summary=f'''# Reproducible analysis results\n\nGenerated with Python standard library (seed 42).\n\n- Rows: {len(rows):,}\n- Mean x: {statistics.mean(xs):.5f}\n- Mean y: {statistics.mean(ys):.5f}\n- Standard deviation y: {statistics.stdev(ys):.5f}\n- Generating function: y = 2x² - 3x + 5 + Gaussian noise (σ=2)\n\nAll data is **synthetic**, not real research or personal records.\n'''
(ROOT/'RESULTS.md').write_text(summary)
print(summary)
