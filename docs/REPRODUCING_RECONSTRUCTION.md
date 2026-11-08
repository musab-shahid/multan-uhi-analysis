# Running the UHI project

## Rebuild the published results without an account

From the repository root, use Python 3.12:

```sh
pip install -r requirements-results.txt
python src/prepare_results.py
python -m unittest discover -s tests -v
```

Or open [the executed offline notebook](../notebooks/UHI_Results_From_Saved_Tables.ipynb) in a local Jupyter environment. It reads the four preserved tables in data/reconstructed, checks them, and generates results/release and docs/RESEARCH_RESULTS.md. This path does not download or recompute Landsat imagery.

## Re-extract from Earth Engine

Open [the canonical Earth Engine notebook](../notebooks/Multan_UHI_Portfolio_Reconstructed.ipynb) in Colab. Install its listed packages, set PROJECT_ID to an authorized Earth Engine Cloud project, authenticate and run sequentially. Maps are disabled by default. Download the generated CSVs, regression samples and run_metadata.json before the temporary runtime resets. Source now passes parsing, but this edited version has not been freshly executed on Earth Engine.

The exact source period is May 1 to September 30 exclusive. The scene cloud metadata threshold is below 10%; QA masking and historical normalizedDifference behavior are preserved. No feature standardization was added. Cluster groups are descriptive, not land-cover classes. The later percentile proxy remains separate from the original FYP vulnerability method.

See [the reconciliation record](NOTEBOOK_RECONCILIATION.md) for the repaired source difference and exact verification scope. The archived snapshot and original FYP documents remain unchanged.
