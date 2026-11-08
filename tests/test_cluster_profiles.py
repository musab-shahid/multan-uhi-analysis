import unittest,sys
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from prepare_results import cluster_profiles
class ClusterTests(unittest.TestCase):
 def setUp(self):
  self.z=pd.DataFrame({'cluster_id':[0,1,2,3],'LST':[40.,30.,45.,35.],'NDVI':[.2,.5,.1,.3],'NDBI':[-.1,-.3,0.,-.2],'MNDWI':[-.2,.1,-.1,-.3],'area_m2':[100.,200.,300.,400.]})
 def test_id_permutation_preserves_profiles(self):
  a=cluster_profiles(self.z);z=self.z.sample(frac=1,random_state=8);z['cluster_id']=[13,14,11,12];b=cluster_profiles(z)
  pd.testing.assert_frame_equal(a.drop(columns='cluster_id'),b.drop(columns='cluster_id'))
 def test_area_denominator_uses_classified_area(self):
  z=cluster_profiles(self.z);self.assertAlmostEqual(z.percent_of_classified_area.sum(),100);self.assertEqual(z.iloc[0].percent_of_classified_area,20)
 def test_invalid_statistics_rejected(self):
  for value in [-1.,float('nan')]:
   z=self.z.copy();z.loc[0,'area_m2']=value
   with self.assertRaises(ValueError):cluster_profiles(z)
 def test_duplicate_ids_rejected(self):
  z=self.z.copy();z.loc[0,'cluster_id']=1
  with self.assertRaises(ValueError):cluster_profiles(z)
if __name__=='__main__':unittest.main()
