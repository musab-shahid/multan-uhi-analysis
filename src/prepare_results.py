"""Validate and present saved UHI outputs; no new Earth Engine extraction is claimed."""
from pathlib import Path
import hashlib,json,platform,importlib.metadata
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]

def cluster_profiles(frame):
    required=['cluster_id','LST','NDVI','NDBI','MNDWI','area_m2']
    if not set(required)<=set(frame):raise ValueError('Required cluster fields missing')
    z=frame[required].copy()
    if z.cluster_id.duplicated().any():raise ValueError('Duplicate cluster IDs')
    if not np.isfinite(z.drop(columns='cluster_id')).all().all():raise ValueError('Nonfinite cluster statistics')
    if (z.area_m2<=0).any():raise ValueError('Cluster area must be positive')
    z=z.sort_values(['LST','NDVI','NDBI','MNDWI']).reset_index(drop=True)
    z['temperature_rank']=np.arange(1,len(z)+1)
    z['profile']=['Temperature group '+str(i) for i in z.temperature_rank]
    z['area_km2']=z.area_m2/1e6;z['percent_of_classified_area']=100*z.area_m2/z.area_m2.sum()
    return z

def run():
    src=ROOT/'data/reconstructed';out=ROOT/'results/release';out.mkdir(parents=True,exist_ok=True)
    a=pd.read_csv(src/'annual_index_summary.csv');raw=pd.read_csv(src/'kmeans_2023_cluster_summary.csv');v=pd.read_csv(src/'new_vulnerability_2023_areas.csv');c=pd.read_csv(src/'historical_vs_new_comparison.csv')
    assert a.Year.tolist()==[2013,2015,2017,2018,2019,2021,2023]
    assert np.isfinite(a).all().all() and (a.filter(like='stdDev')>=0).all().all()
    z=cluster_profiles(raw)
    assert np.allclose(raw.area_proportion,raw.area_m2/raw.area_m2.sum(),rtol=1e-8)
    assert set(v.class_code)=={0,1,2} and v.class_code.is_unique and (v.area_km2>0).all()
    assert np.allclose(v.percent_of_valid_area,100*v.area_km2/v.area_km2.sum(),atol=1e-8)
    assert np.isclose(v.percent_of_valid_area.sum(),100)
    joined=c.merge(v,on='vulnerability',validate='one_to_one',suffixes=('_comparison','_source'))
    assert np.allclose(joined.percent_of_valid_area_comparison,joined.percent_of_valid_area_source)
    assert np.allclose(joined.difference_percentage_points,joined.percent_of_valid_area_source-joined.historical_report_percent)
    a.to_csv(out/'seasonal_surface_summary.csv',index=False);z.to_csv(out/'neutral_cluster_profiles.csv',index=False)
    # This is a difference between two region-wide means, not paired-pixel change or UHI intensity.
    delta=float(a.loc[a.Year==2023,'LST_mean'].iloc[0]-a.loc[a.Year==2013,'LST_mean'].iloc[0])
    metrics=dict(mean_lst_2013_c=float(a.iloc[0].LST_mean),mean_lst_2023_c=float(a.iloc[-1].LST_mean),difference_of_regional_means_c=delta,coolest_selected_year=int(a.loc[a.LST_mean.idxmin(),'Year']),warmest_selected_year=int(a.loc[a.LST_mean.idxmax(),'Year']),cluster_mean_range_c=float(z.LST.max()-z.LST.min()),classified_area_km2=float(z.area_km2.sum()),proxy_valid_area_km2=float(v.area_km2.sum()))
    (out/'summary_metrics.json').write_text(json.dumps(metrics,indent=2))
    manifest=[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in sorted(src.glob('*.csv'))]
    (out/'input_manifest.json').write_text(json.dumps(manifest,indent=2))
    (out/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),packages={n:importlib.metadata.version(n) for n in ['numpy','pandas','matplotlib']}),indent=2))
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(figsize=(10,4.6));ax.errorbar(a.Year,a.LST_mean,yerr=a.LST_stdDev,fmt='o',color='#b76c45',capsize=5,markersize=7)
    for row in a.itertuples():ax.text(row.Year,row.LST_mean+.35,f'{row.LST_mean:.2f}',ha='center',fontsize=9)
    ax.set(xticks=a.Year,ylabel='Land-surface temperature (C)',title='Selected warm-season surface temperatures',ylim=(34,48));ax.text(.01,.02,'Bars: spatial standard deviation, not confidence intervals',transform=ax.transAxes,fontsize=9);fig.tight_layout();fig.savefig(out/'seasonal_surface_temperature.png',dpi=180);plt.close(fig)
    fig,axs=plt.subplots(1,2,figsize=(11,4.5));labels=['G'+str(i) for i in z.temperature_rank]
    axs[0].bar(labels,z.LST,color=['#517fa1','#5d9e8a','#c2a16c','#b66f51']);axs[0].set(ylabel='Mean LST (C)',title='Exploratory temperature groups',ylim=(0,52))
    for i,row in z.iterrows():axs[0].text(i,row.LST+.8,f'{row.LST:.2f} C\n{row.percent_of_classified_area:.1f}% area',ha='center',fontsize=9)
    xx=np.arange(len(z));width=.25
    for j,(key,color) in enumerate(zip(['NDVI','NDBI','MNDWI'],['#287c70','#b28a64','#527fa1'])):axs[1].bar(xx+(j-1)*width,z[key],width,label=key,color=color)
    axs[1].set(xticks=xx,xticklabels=labels,ylabel='Mean spectral index',title='Group spectral characteristics');axs[1].axhline(0,color='grey',lw=.8);axs[1].legend(frameon=False,fontsize=9);fig.tight_layout();fig.savefig(out/'cluster_profiles.png',dpi=180);plt.close(fig)
    lines=['# Spatiotemporal Analysis of Urban Heat Island Effect in Multan, Pakistan (2013–2023)','Research results brief | November 2026','## Study and contribution','Musab Shahid’s undergraduate environmental-science project at Bahauddin Zakariya University examines Landsat surface-temperature patterns within 25 km of central Multan. This brief presents the supplied reconstructed numerical results, with neutral descriptions of exploratory clusters. The original FYP report remains the full historical research document.','## Findings',f'The selected warm-season mean LST ranged from {a.LST_mean.min():.2f} C in 2021 to {a.LST_mean.max():.2f} C in 2015. The 2013 and 2023 means were {a.iloc[0].LST_mean:.2f} C and {a.iloc[-1].LST_mean:.2f} C. Their difference, {delta:.2f} C, is descriptive: it is not a warming rate, a paired-pixel change estimate, or an urban-rural heat-island intensity.','![Seasonal surface temperatures](../results/release/seasonal_surface_temperature.png)','## Methods','Landsat 8 Collection 2 Tier 1 Level 2 imagery was filtered to the 25-km circle centered at 71.4753 E, 30.1575 N. Selected years are 2013, 2015, 2017, 2018, 2019, 2021 and 2023. The source filter runs from May 1 to September 30 exclusive (through September 29), with scene cloud cover below 10%. Quality masks exclude flagged pixels; surface reflectance and surface temperature are scaled before calculating NDVI, NDBI and MNDWI. Each selected year uses a median composite. Mean and spatial standard deviation summarize the available pixels; standard deviation is spatial variability, not uncertainty in the mean.','## Exploratory groups',f'Four-cluster K-Means uses LST, NDVI, NDBI and MNDWI on the 2023 composite. The input features were not standardized. The retained cluster summaries cover {z.area_km2.sum():.2f} km2 of classified pixels. Group means range from {z.LST.min():.2f} to {z.LST.max():.2f} C, a {z.LST.max()-z.LST.min():.2f} C contrast. Groups G1-G4 are ordered by mean LST only; they are not validated land-cover classes. This contrast is also not an independently estimated urban heat-island intensity.','![Neutral cluster profiles](../results/release/cluster_profiles.png)','The coolest group has positive mean MNDWI and low NDVI. Group G2 has the highest NDVI. Group G4 is hottest and has the least-negative NDBI. These spectral patterns support exploratory interpretation, but cannot by themselves establish water, vegetation, barren or urban class accuracy. The old names remain in historical tables; the current figures avoid assigning land-cover names from numeric cluster IDs.','## The later surface proxy','A separate 2026 extension uses high LST (75th percentile), low NDVI (25th percentile) and high NDBI (75th percentile). Its saved shares are 62.97%, 21.72% and 15.32% for scores 0, 1-2 and 3, respectively. The source called these Low, Moderate and Extreme. They describe a relative surface-index rule, not population vulnerability or health risk. The original FYP vulnerability formula is not recoverable from the archived code, so these later percentages must not be presented as a reconstruction of that formula.','## Scope and reproducibility','The published four CSVs pass schema, finite-value, area-denominator and comparison-arithmetic checks. The offline results notebook executes without Earth Engine or account access. These checks reproduce the presentation from saved tables, not a fresh extraction from Landsat. The canonical Earth Engine notebook has been reconciled and syntax checked; the saved execution snapshot remains an archive. Input hashes, execution details and source differences are supporting methods in the repository.','LST measures surface temperature rather than air temperature. Cloud selection, per-band masks, uneven acquisition dates, mixed pixels and unstandardized clustering limit interpretation. No land-cover accuracy, health-risk, long-term trend or urban-rural UHI-intensity claim is made from these summaries.','## Materials and credits','Original study: Musab Shahid, Bahauddin Zakariya University. Data: USGS Landsat 8 Collection 2 Level 2, processed in Google Earth Engine. November 2026 code review, offline verification and presentation preparation used AI assistance. See the original report for its research narrative; use these current figures with the scope above.']
    (ROOT/'docs').mkdir(exist_ok=True);(ROOT/'docs/RESEARCH_RESULTS.md').write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
    print('PASS: 7 yearly records; 4 neutral clusters; 3 proxy classes; all area and comparison checks.')
    print(json.dumps(metrics,indent=2));return metrics
if __name__=='__main__':run()
