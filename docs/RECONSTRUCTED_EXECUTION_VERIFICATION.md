# Executed-notebook verification record

Source evidence: researcher-supplied executed `Multan_UHI_Reproducibility_Audit_v2 (1).ipynb` and four exported CSVs. **The newly organized notebook committed beside this record was not itself executed end-to-end.**

## Observed in the prior executed notebook
- Earth Engine initialization succeeded using a Cloud project authorized by the researcher's account.
- Eligible Landsat scenes for 2013/2015/2017/2018/2019/2021/2023: **12/10/11/12/10/13/9**.
- Historical annual LST, NDVI, NDBI, and MNDWI means matched the original report to displayed precision.
- 2023 cluster means and areas matched historical report values to displayed precision. Semantic cluster labels are unvalidated.
- 21 executed code cells; no saved Python error outputs. Interactive map widgets were disabled; this is **not** evidence that OpenStreetMap tiles rendered.
- Four user-exported CSVs are committed under `data/reconstructed/` as evidence of the prior execution.

## Scientific boundary
The historical FYP reports Low **38.157724%**, Moderate **57.141238%**, Extreme **4.701038%**. Its source-code PDF does not define the vulnerability mask or class computation. The new percentile-based proxy gives **62.967090% / 21.716353% / 15.316558%** over valid imagery pixels. They are *different methodologies*. Do not re-label the new figures as historical findings or tune thresholds to match.

## Reproduction limitations
The original research PDFs and poster are unchanged. The notebook uses a live Earth Engine collection that may have evolved since the original work; account permissions and dataset versions matter. The newly organized code is **syntax-oriented reconstruction, not independently tested as a fully reproducible research artifact**. Further verification should use a fresh Colab run and compare output tables with committed CSVs; do not assume identical K-Means numeric IDs across runs.

Source archive: `fyp.ipynb - Colab Code.pdf`; FYP report: `FYP_Multan_UHI_Report.pdf`.
