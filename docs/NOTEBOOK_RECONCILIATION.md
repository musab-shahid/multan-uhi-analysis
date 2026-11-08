# Notebook reconciliation and verification

8 November 2026. The two repository notebooks have the same 20-cell structure. Their only code-cell source difference is zero-based cell 15, which computes the later percentile proxy. The clean source contains an unmatched closing parenthesis. The archived execution snapshot uses valid parenthesized chaining. Its saved outputs are retained; no claim of a new Earth Engine execution is made.

The canonical source now uses three explicit boolean terms and adds them to form the same score. All code cells pass Python parsing after excluding the installation magic. No saved outputs were copied into edited cells. The researcher-supplied original 34-cell notebook was inspected locally; its hash and syntax results are recorded without publishing local paths.

Additional changes remove fixed Water/Vegetation/Barren/Urban names from arbitrary K-Means IDs. Groups are ordered by their observed mean temperature and retain spectral statistics. A permutation test confirms the reporting function is invariant to relabeling IDs. Future Earth Engine runs also export package versions, scene counts, configuration, proxy thresholds and regression samples. These new exports have not been produced by a fresh Earth Engine run.

The offline results notebook executed successfully from all four supplied CSVs. Checks cover finite annual values, unique classes, positive areas, area proportions, percentage sums and historical/new comparison arithmetic. Four focused tests passed. Numerical outputs, input hashes and the actual local package environment are in results/release/. These are table-level and source checks, not an independent Landsat extraction or land-cover validation.

Machine-readable cell-by-cell results: [notebook_reconciliation.json](../results/release/notebook_reconciliation.json). Source scaling and masking references: [Landsat collection documentation](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2) and [normalizedDifference](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference). The historical normalizedDifference masking behavior is retained.
