 ```
Dataset Shape: (1048575, 80)
   dst port  protocol            timestamp  flow duration  tot fwd pkts  \
0         0         0  14/02/2018 08:31:01      112641719             3   
1         0         0  14/02/2018 08:33:50      112641466             3   
2         0         0  14/02/2018 08:36:39      112638623             3   
3        22         6  14/02/2018 08:40:13        6453966            15   
4        22         6  14/02/2018 08:40:23        8804066            14   
```
```
   tot bwd pkts  totlen fwd pkts  totlen bwd pkts  fwd pkt len max  \
0             0                0                0                0   
1             0                0                0                0   
2             0                0                0                0   
3            10             1239             2273              744   
4            11             1143             2209              744   
```
```
   fwd pkt len min  ...  fwd seg size min  active mean  active std  \
0                0  ...                 0          0.0         0.0   
1                0  ...                 0          0.0         0.0   
2                0  ...                 0          0.0         0.0   
3                0  ...                32          0.0         0.0   
4                0  ...                32          0.0         0.0   
```
```
   active max  active min   idle mean    idle std  idle max  idle min   label  
0           0           0  56320859.5  139.300036  56320958  56320761  Benign  
1           0           0  56320733.0  114.551299  56320814  56320652  Benign  
2           0           0  56319311.5  301.934596  56319525  56319098  Benign  
3           0           0         0.0    0.000000         0         0  Benign  
4           0           0         0.0    0.000000         0         0  Benign  

[5 rows x 80 columns]
```
---
##  --- Random Forest Results ---
```
Accuracy: 0.999971389743223
              precision    recall  f1-score   support

           0       1.00      1.00      1.00    133397
           1       1.00      1.00      1.00     38689
           2       1.00      1.00      1.00     37629

    accuracy                           1.00    209715
   macro avg       1.00      1.00      1.00    209715
weighted avg       1.00      1.00      1.00    209715
```
---

##  --- SVM Results ---
```
Accuracy: 0.9999380111103163
              precision    recall  f1-score   support

           0       1.00      1.00      1.00    133397
           1       1.00      1.00      1.00     38689
           2       1.00      1.00      1.00     37629

    accuracy                           1.00    209715
   macro avg       1.00      1.00      1.00    209715
weighted avg       1.00      1.00      1.00    209715

```
---
##  --- K-Means Results (Unsupervised) ---
Confusion Matrix:
[[84027 49370     0]
---
 [    0 38689     0]
 [18686 18943     0]]
```
