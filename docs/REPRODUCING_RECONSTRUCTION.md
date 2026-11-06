# Reproducing the reconstructed UHI analysis

1. Open [the reconstructed Python notebook](../notebooks/Multan_UHI_Portfolio_Reconstructed.ipynb) in **Google Colab**.
2. Sign in to an account authorized to use Google Earth Engine. Set `PROJECT_ID` in the first Python cell to a Cloud project your account may use. The original study's ID is `fyp-multan-spatiotemp-analysis`; it is **not a secret**.
3. Run the install and initialization cells; complete Earth Engine authorization if prompted.
4. Leave `SHOW_INTERACTIVE_MAPS = False` unless browser tile access works. Maps are optional; data calculations do not require OpenStreetMap.
5. Execute sequentially. The notebook writes CSVs into `/content/multan_uhi_reconstructed_outputs`. **Download them** because Colab runtime files are temporary.
6. Compare the annual summaries with [published derived CSV](../data/reconstructed/annual_index_summary.csv) and the cluster summaries with [2023 cluster CSV](../data/reconstructed/kmeans_2023_cluster_summary.csv). Note that Earth Engine data availability and unsupervised cluster ID ordering may vary.
7. Treat [the new vulnerability proxy](../data/reconstructed/new_vulnerability_2023_areas.csv) and [historical comparison](../data/reconstructed/historical_vs_new_comparison.csv) strictly as a **new method**, not a reproduction of missing original code.

**Warnings:** Data source: Landsat 8 C2 L2; yearly source filters use a **September 30 exclusive end date**, cloud metadata <10%, QA band masking, reflectance/temperature scaling. The clustering features are *not standardized* and original cluster semantic labels have no independently validated ground truth. The annual results were verified from a *prior* executed notebook; this reorganized notebook has **not yet passed a fresh end-to-end execution**.
