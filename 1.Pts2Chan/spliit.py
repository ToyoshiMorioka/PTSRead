import pandas as pd

df = pd.read_csv('ShibuyaUnderground.pts', header=None, sep=' ')
df.to_csv('shibuya_x.chan', header=False, index=False, columns=[0], sep = ' ')
df.to_csv('shibuya_y.chan', header=False, index=False, columns=[1], sep = ' ')
df.to_csv('shibuya_z.chan', header=False, index=False, columns=[2], sep = ' ')
df.to_csv('shibuya_r.chan', header=False, index=False, columns=[4], sep = ' ')
df.to_csv('shibuya_g.chan', header=False, index=False, columns=[5], sep = ' ')
df.to_csv('shibuya_b.chan', header=False, index=False, columns=[6], sep = ' ')
