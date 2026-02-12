```
Files inside: ['cybersecurity_intrusion_data.csv']
  session_id  network_packet_size protocol_type  login_attempts  ...  failed_logins browser_type  unusual_time_access  attack_detected
0  SID_00001                  599           TCP               4  ...              1         Edge                    0                1
1  SID_00002                  472           TCP               3  ...              0      Firefox                    0                0
2  SID_00003                  629           TCP               3  ...              2       Chrome                    0                1
3  SID_00004                  804           UDP               4  ...              0      Unknown                    0                1
4  SID_00005                  453           TCP               5  ...              1      Firefox                    0                0

[5 rows x 11 columns]
(9537, 11)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9537 entries, 0 to 9536
Data columns (total 11 columns):
 #   Column               Non-Null Count  Dtype
---  ------               --------------  -----
 0   session_id           9537 non-null   object
 1   network_packet_size  9537 non-null   int64
 2   protocol_type        9537 non-null   object
 3   login_attempts       9537 non-null   int64
 4   session_duration     9537 non-null   float64
 5   encryption_used      7571 non-null   object
 6   ip_reputation_score  9537 non-null   float64
 7   failed_logins        9537 non-null   int64
 8   browser_type         9537 non-null   object
 9   unusual_time_access  9537 non-null   int64
 10  attack_detected      9537 non-null   int64
dtypes: float64(2), int64(5), object(4)
memory usage: 819.7+ KB
None
attack_detected
0    5273
1    4264
Name: count, dtype: int64

Confusion Matrix:
[[840 215]
 [301 552]]

Classification Report:
              precision    recall  f1-score   support

           0       0.74      0.80      0.77      1055
           1       0.72      0.65      0.68       853

    accuracy                           0.73      1908
   macro avg       0.73      0.72      0.72      1908
weighted avg       0.73      0.73      0.73      1908


Random Forest Confusion Matrix:
[[1051    4]
 [ 216  637]]

Random Forest Classification Report:
              precision    recall  f1-score   support

           0       0.83      1.00      0.91      1055
           1       0.99      0.75      0.85       853

    accuracy                           0.88      1908
   macro avg       0.91      0.87      0.88      1908
weighted avg       0.90      0.88      0.88      1908

```
