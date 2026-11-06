# Multan Urban Heat Island & Surface-Temperature Analysis (2013–2023)

**Landsat 8 · Google Earth Engine · Remote sensing · Spatial statistics · Exploratory clustering**

Undergraduate environmental-science research examining surface-temperature differences across Multan and surrounding peri-urban land cover.

**Researcher:** Musab Shahid  
**Institution:** Bahauddin Zakariya University, Multan, Pakistan  
**Study area:** 25-km radius around Multan  
**Time frame:** Selected warm-season observations from 2013, 2015, 2017, 2018, 2019, 2021 and 2023

> **Interpretation:** Satellite land-surface temperature (LST) is **not** air temperature or direct human heat exposure. Historical land-cover labels and the newer vulnerability proxy are not independently validated.

## Explore the project

| Start here | What it contains |
| --- | --- |
| [Original FYP research report](FYP_Multan_UHI_Report.pdf) | Historical research narrative, methodology and results |
| [Research poster](fyp-canva-poster.png) | One-page visual introduction |
| [Reconstructed executable Colab notebook](notebooks/Multan_UHI_Portfolio_Reconstructed.ipynb) | Landsat processing, index summaries, regressions and 2023 clustering |
| [How to run the notebook](docs/REPRODUCING_RECONSTRUCTION.md) | GEE project access, dependencies and run order |
| [Derived numerical outputs](data/reconstructed/) | Annual statistics, cluster summaries and **new** vulnerability-proxy tables |
| [Execution verification and caveats](docs/RECONSTRUCTED_EXECUTION_VERIFICATION.md) | Evidence from a previous notebook run, with interpretation limits |
| [Historical code export (PDF)](fyp.ipynb%20-%20Colab%20Code.pdf) | Original archival source used in reconstruction; not executable |

![Original Multan surface-temperature research poster](fyp-canva-poster.png)

## Research questions

How do satellite-observed land-surface temperatures differ among built-up, vegetated, barren and water-related surfaces? How do LST and spectral indices vary across the selected warm-season years, and what relationships emerge between vegetation and surface temperature?

## Data and analytical approach

1. **Acquire and preprocess** Landsat 8 Collection 2 Level 2 imagery in Google Earth Engine, applying quality masks and published surface-temperature/reflectance scaling.
2. **Measure surface characteristics** with LST, NDVI (vegetation), NDBI (built-up signal) and MNDWI (water-related signal).
3. **Compare years and associations** through regional summaries and descriptive NDVI–LST regression.
4. **Explore 2023 spatial groupings** using four-cluster K-Means on LST and spectral-index features.

**Selected historical annual mean LST values:** 2013 **40.06°C**, 2015 **41.79°C**, 2017 **41.73°C**, 2018 **41.28°C**, 2019 **41.28°C**, 2021 **39.60°C**, and 2023 **40.67°C**. These are means of the selected seasonal satellite composites, **not** continuous annual air-temperature measurements.

## Reproduction status and boundaries

- A preceding Colab reconstruction ran successfully and generated the four [published CSV outputs](data/reconstructed/); the organized repository notebook was subsequently reported to run in Colab. A separate, documented independent rerun is not claimed.
- The archival code PDF does **not** contain the original vulnerability-classification formula, thresholds or complete variables. The 2026 percentile-based **relative surface vulnerability proxy** is a **new model**, not a reproduction of the historical FYP's low/moderate/extreme area percentages.
- K-Means clusters are **unsupervised** and the historical labels (water, vegetation, barren, urban) were not validated against independent reference observations. Original features were not standardized.
- Seasonal compositing, cloud masking, mixed pixels and observation timing limit comparisons. External background-map tiles can fail without affecting Earth Engine calculations.
- The original report and poster are preserved unchanged.

**Tools:** Earth Engine, Python, Google Colab, geemap, pandas, NumPy, SciPy and Matplotlib.

## Research portfolio

| Project | Focus | Research context |
| --- | --- | --- |
| **This project — Urban heat** | Landsat LST, spectral indices, exploratory spatial grouping | Undergraduate final-year research |
| [ERA5 Monsoon Analysis](https://github.com/musab-shahid/multan-era5-monsoon-analysis) | Atmospheric reanalysis, seasonal rainfall, trend inference | **Collaborative**, four contributors |
| [South Punjab Drought Analysis](https://github.com/musab-shahid/south-punjab-drought-analysis) | Multi-sensor drought events and environmental responses | **Independent** research-application report |

## Attribution and license

Researcher: **Musab Shahid**. See [LICENSE](LICENSE) for repository licensing; source publications, graphics and external imagery/data may have different usage rights. A [draft profile README](docs/GITHUB_PROFILE_README_DRAFT.md) is retained separately for potential GitHub profile publication.
