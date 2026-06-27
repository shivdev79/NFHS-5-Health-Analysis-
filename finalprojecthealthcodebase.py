Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
df = pd.read_csv("NFHS5_State_Indicators.csv")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df = pd.read_csv("NFHS5_State_Indicators.csv")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'NFHS5_State_Indicators.csv'
df = pd.read_csv(""C:\Users\Lenovo\Downloads\NFHS-5-States.csv"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
df = pd.read_csv("C:\Users\Lenovo\Downloads\NFHS-5-States.csv")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape



df = pd.read_csv(
    r"C:\Users\Lenovo\Downloads\National Family Health Survey (NFHS-5) 2019-20.csv"
)






df.head()
   S.No.  indicator code  ... NFHS-4 2015-16                   STATE/UT
0    NaN             NaN  ...          Total                        NaN
1    1.0             1.0  ...           84.7  Andaman & Nicobar Islands
2    2.0             2.0  ...           23.9  Andaman & Nicobar Islands
3    3.0             3.0  ...            977  Andaman & Nicobar Islands
4    4.0             4.0  ...            859  Andaman & Nicobar Islands

[5 rows x 9 columns]
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 4819 entries, 0 to 4818
Data columns (total 9 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   S.No.             4818 non-null   float64
 1   indicator code    4818 non-null   float64
 2   Indicators        4818 non-null   str    
 3    sub indicators   4818 non-null   str    
 4   NFHS-5 (2019-20)  4819 non-null   str    
 5   Unnamed: 5        4685 non-null   str    
 6   Unnamed: 6        4819 non-null   str    
 7   NFHS-4 2015-16    4819 non-null   str    
 8   STATE/UT          4818 non-null   str    
dtypes: float64(2), str(7)
memory usage: 339.0 KB
print("Rows :", df.shape[0])
Rows : 4819
print("Columns :", df.shape[1])
Columns : 9
print(df.columns)
Index(['S.No.', 'indicator code', 'Indicators', ' sub indicators',
       'NFHS-5 (2019-20)', 'Unnamed: 5', 'Unnamed: 6', 'NFHS-4 2015-16',
       'STATE/UT'],
      dtype='str')
df.columns = [
    "SNo",
    "Indicator_Code",
    "Indicator",
    "Sub_Indicator",
    "NFHS5",
    "Urban",
    "Rural",
    "NFHS4",
    "State"
]
df.head()
   SNo  Indicator_Code  ...  NFHS4                      State
0  NaN             NaN  ...  Total                        NaN
1  1.0             1.0  ...   84.7  Andaman & Nicobar Islands
2  2.0             2.0  ...   23.9  Andaman & Nicobar Islands
3  3.0             3.0  ...    977  Andaman & Nicobar Islands
4  4.0             4.0  ...    859  Andaman & Nicobar Islands

[5 rows x 9 columns]
df.isnull().sum()
SNo                 1
Indicator_Code      1
Indicator           1
Sub_Indicator       1
NFHS5               0
Urban             134
Rural               0
NFHS4               0
State               1
dtype: int64
df = df.dropna(subset=["State"])
df = df.reset_index(drop=True)
df.head(10)
    SNo  Indicator_Code  ... NFHS4                      State
0   1.0             1.0  ...  84.7  Andaman & Nicobar Islands
1   2.0             2.0  ...  23.9  Andaman & Nicobar Islands
2   3.0             3.0  ...   977  Andaman & Nicobar Islands
3   4.0             4.0  ...   859  Andaman & Nicobar Islands
4   5.0             5.0  ...  97.9  Andaman & Nicobar Islands
5   6.0             6.0  ...    na  Andaman & Nicobar Islands
6   7.0             7.0  ...  97.2  Andaman & Nicobar Islands
7   8.0             8.0  ...  95.0  Andaman & Nicobar Islands
8   9.0             9.0  ...  75.4  Andaman & Nicobar Islands
9  10.0            10.0  ...  63.5  Andaman & Nicobar Islands

[10 rows x 9 columns]
df.dtypes
SNo               float64
Indicator_Code    float64
Indicator             str
Sub_Indicator         str
NFHS5                 str
Urban                 str
Rural                 str
NFHS4                 str
State                 str
dtype: object
df["NFHS5"] = pd.to_numeric(df["NFHS5"], errors="coerce")
df["NFHS4"] = pd.to_numeric(df["NFHS4"], errors="coerce")
df.isnull().sum()
SNo                  0
Indicator_Code       0
Indicator            0
Sub_Indicator        0
NFHS5              351
Urban              134
Rural                0
NFHS4             1196
State                0
dtype: int64
df["NFHS5"] = df["NFHS5"].fillna(df["NFHS5"].mean())
df["NFHS4"] = df["NFHS4"].fillna(df["NFHS4"].mean())
KeyboardInterrupt
print(df["Indicator"].unique())

print(df["Sub_Indicator"].unique())
<StringArray>
[                                          'Female population age 6 years and above who ever attended school (%)',
                                                                              'Population below age 15 years (%)',
                                                    'Sex ratio of the total population (females per 1,000 males)',
                          'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                             'Children under age 5 years whose birth was registered with the civil authority (%)',
                                             'Deaths in the last 3 years registered with the civil authority (%)',
                                                           'Population living in households with electricity (%)',
                                     'Population living in households with an improved drinking-water source (%)',
                                   'Population living in households that use an improved sanitation facility (%)',
                                                                    'Households using clean fuel for cooking (%)',
 ...
          'Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)',
                                  'Children age 6-8 months receiving solid or semi-solid food and breastmilk (%)',
                                      'Non-breastfeeding children age 6-23 months receiving an adequate diet (%)',
                'Children age 12-23 months fully vaccinated based on information from vaccination card only (%) ',
 'Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%) ',
                                                       'Women who have comprehensive knowledge24 of HIV/AIDS (%)',
                                                         'Men who have comprehensive knowledge24 of HIV/AIDS (%)',
                          'Children age 12-23 months who received most of their vaccinations in a private health',
                               'Children age 12-23 months who have received the first dose of measles-containing',
            'Children age 12-23 months who received most of their vaccinations in a private health facility (%) ']
Length: 138, dtype: str
print(df["Indicator"].unique())

print(df["Sub_Indicator"].unique())
<StringArray>
[                                          'Female population age 6 years and above who ever attended school (%)',
                                                                              'Population below age 15 years (%)',
                                                    'Sex ratio of the total population (females per 1,000 males)',
                          'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                             'Children under age 5 years whose birth was registered with the civil authority (%)',
                                             'Deaths in the last 3 years registered with the civil authority (%)',
                                                           'Population living in households with electricity (%)',
                                     'Population living in households with an improved drinking-water source (%)',
                                   'Population living in households that use an improved sanitation facility (%)',
                                                                    'Households using clean fuel for cooking (%)',
 ...
          'Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)',
                                  'Children age 6-8 months receiving solid or semi-solid food and breastmilk (%)',
                                      'Non-breastfeeding children age 6-23 months receiving an adequate diet (%)',
                'Children age 12-23 months fully vaccinated based on information from vaccination card only (%) ',
 'Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%) ',
                                                       'Women who have comprehensive knowledge24 of HIV/AIDS (%)',
                                                         'Men who have comprehensive knowledge24 of HIV/AIDS (%)',
                          'Children age 12-23 months who received most of their vaccinations in a private health',
                               'Children age 12-23 months who have received the first dose of measles-containing',
            'Children age 12-23 months who received most of their vaccinations in a private health facility (%) ']
Length: 138, dtype: str
print(df["Sub_Indicator"].unique())
<StringArray>
[                                          'Female population age 6 years and above who ever attended school (%)',
                                                                              'Population below age 15 years (%)',
                                                    'Sex ratio of the total population (females per 1,000 males)',
                          'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                             'Children under age 5 years whose birth was registered with the civil authority (%)',
                                             'Deaths in the last 3 years registered with the civil authority (%)',
                                                           'Population living in households with electricity (%)',
                                     'Population living in households with an improved drinking-water source (%)',
                                   'Population living in households that use an improved sanitation facility (%)',
                                                                    'Households using clean fuel for cooking (%)',
 ...
          'Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)',
                                  'Children age 6-8 months receiving solid or semi-solid food and breastmilk (%)',
                                      'Non-breastfeeding children age 6-23 months receiving an adequate diet (%)',
                'Children age 12-23 months fully vaccinated based on information from vaccination card only (%) ',
 'Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%) ',
                                                       'Women who have comprehensive knowledge24 of HIV/AIDS (%)',
                                                         'Men who have comprehensive knowledge24 of HIV/AIDS (%)',
                          'Children age 12-23 months who received most of their vaccinations in a private health',
                               'Children age 12-23 months who have received the first dose of measles-containing',
            'Children age 12-23 months who received most of their vaccinations in a private health facility (%) ']
Length: 138, dtype: str
print(df["Sub_Indicator"].unique())
<StringArray>
[                                          'Female population age 6 years and above who ever attended school (%)',
                                                                              'Population below age 15 years (%)',
                                                    'Sex ratio of the total population (females per 1,000 males)',
                          'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                             'Children under age 5 years whose birth was registered with the civil authority (%)',
                                             'Deaths in the last 3 years registered with the civil authority (%)',
                                                           'Population living in households with electricity (%)',
                                     'Population living in households with an improved drinking-water source (%)',
                                   'Population living in households that use an improved sanitation facility (%)',
                                                                    'Households using clean fuel for cooking (%)',
 ...
          'Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)',
                                  'Children age 6-8 months receiving solid or semi-solid food and breastmilk (%)',
                                      'Non-breastfeeding children age 6-23 months receiving an adequate diet (%)',
                'Children age 12-23 months fully vaccinated based on information from vaccination card only (%) ',
 'Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%) ',
                                                       'Women who have comprehensive knowledge24 of HIV/AIDS (%)',
                                                         'Men who have comprehensive knowledge24 of HIV/AIDS (%)',
                          'Children age 12-23 months who received most of their vaccinations in a private health',
                               'Children age 12-23 months who have received the first dose of measles-containing',
            'Children age 12-23 months who received most of their vaccinations in a private health facility (%) ']
Length: 138, dtype: str
print(df["Sub_Indicator"].unique())
<StringArray>
[                                          'Female population age 6 years and above who ever attended school (%)',
                                                                              'Population below age 15 years (%)',
                                                    'Sex ratio of the total population (females per 1,000 males)',
                          'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
                             'Children under age 5 years whose birth was registered with the civil authority (%)',
                                             'Deaths in the last 3 years registered with the civil authority (%)',
                                                           'Population living in households with electricity (%)',
                                     'Population living in households with an improved drinking-water source (%)',
                                   'Population living in households that use an improved sanitation facility (%)',
                                                                    'Households using clean fuel for cooking (%)',
 ...
          'Children born at home who were taken to a health facility for a check-up within 24 hours of birth (%)',
                                  'Children age 6-8 months receiving solid or semi-solid food and breastmilk (%)',
                                      'Non-breastfeeding children age 6-23 months receiving an adequate diet (%)',
                'Children age 12-23 months fully vaccinated based on information from vaccination card only (%) ',
 'Children with diarrhoea in the 2 weeks preceding the survey taken to a health facility or health provider (%) ',
                                                       'Women who have comprehensive knowledge24 of HIV/AIDS (%)',
                                                         'Men who have comprehensive knowledge24 of HIV/AIDS (%)',
                          'Children age 12-23 months who received most of their vaccinations in a private health',
                               'Children age 12-23 months who have received the first dose of measles-containing',
            'Children age 12-23 months who received most of their vaccinations in a private health facility (%) ']
Length: 138, dtype: str
# Search for obesity indicators
df[df["Indicator"].str.contains("obese|overweight", case=False, na=False)][["Indicator"]].drop_duplicates()
Empty DataFrame
Columns: [Indicator]
Index: []
# Search for anaemia indicators
df[df["Indicator"].str.contains("anaemia|anemia", case=False, na=False)][["Indicator"]].drop_duplicates()
                            Indicator
88  Anaemia among Children and Adults
# Search for hypertension indicators
df[df["Indicator"].str.contains("hypertension|blood pressure", case=False, na=False)][["Indicator"]].drop_duplicates()
                                             Indicator
101  Hypertension among Adults (age 15 years and ab...
104  Hypertension among Adults (age 15 years and ab...
# Search for high blood sugar indicators
df[df["Indicator"].str.contains("blood sugar|glucose|diabetes", case=False, na=False)][["Indicator"]].drop_duplicates()
                                
                                            Indicator
95  Blood Sugar Level among Adults (age 15 years a...
98  Blood Sugar Level among Adults (age 15 years a...
# Search for high blood sugar indicators
df[df["Indicator"].str.contains("blood sugar|glucose|diabetes", case=False, na=False)][["Indicator"]].drop_duplicates()
                                    
                                            Indicator
95  Blood Sugar Level among Adults (age 15 years a...
98  Blood Sugar Level among Adults (age 15 years a...
keywords = [
    "obese",
    "overweight",
    "anaemia",
    "anemia",
    "blood pressure",
    "hypertension",
    "blood sugar",
    "glucose",
    "diabetes"
]

pattern = "|".join(keywords)

health_df = df[
    df["Indicator"].str.contains(pattern, case=False, na=False)
].copy()

health_df.head()
                                    
SyntaxError: multiple statements found while compiling a single statement
keywords = [
    "obese",
    "overweight",
    "anaemia",
    "anemia",
    "blood pressure",
    "hypertension",
    "blood sugar",
    "glucose",
    "diabetes"
]

pattern = "|".join(keywords)
                                    
health_df = df[
    df["Indicator"].str.contains(pattern, case=False, na=False)
].copy()


health_df.head()
                                    
     SNo  Indicator_Code  ... NFHS4                      State
88  92.0            92.0  ...  49.0  Andaman & Nicobar Islands
89  93.0            93.0  ...  65.8  Andaman & Nicobar Islands
90  94.0            94.0  ...  61.4  Andaman & Nicobar Islands
91  95.0            95.0  ...  65.7  Andaman & Nicobar Islands
92  96.0            96.0  ...  68.1  Andaman & Nicobar Islands

[5 rows x 9 columns]
print("Rows:", health_df.shape[0])
                                    
Rows: 702
print("Columns:", health_df.shape[1])
                                    
Columns: 9
health_df["Indicator"].unique()
                                    
<StringArray>
[                              'Anaemia among Children and Adults',
 'Blood Sugar Level among Adults (age 15 years and above) - Women',
   'Blood Sugar Level among Adults (age 15 years and above) - Men',
      'Hypertension among Adults (age 15 years and above) - Women',
        'Hypertension among Adults (age 15 years and above) - Men']
Length: 5, dtype: str
health_df["NFHS5"] = pd.to_numeric(
    health_df["NFHS5"],
    errors="coerce"
)

health_df["NFHS5"] = health_df["NFHS5"].fillna(
    health_df["NFHS5"].mean()
)
                                    

health_df.isnull().sum()
                                    
SNo               0
Indicator_Code    0
Indicator         0
Sub_Indicator     0
NFHS5             0
Urban             0
Rural             0
NFHS4             0
State             0
dtype: int64
obesity = health_df[
    health_df["Indicator"].str.contains("obese|overweight", case=False)
]

obesity.head()
                                    
Empty DataFrame
Columns: [SNo, Indicator_Code, Indicator, Sub_Indicator, NFHS5, Urban, Rural, NFHS4, State]
Index: []
print(obesity["Indicator"].unique())
                                    
<StringArray>
[]
Length: 0, dtype: str
health["Gender_Obesity_Gap"] = (
    health["Women_Obesity"] -
    health["Men_Obesity"]
)
                                    
Traceback (most recent call last):
  File "<pyshell#62>", line 2, in <module>
    health["Women_Obesity"] -
NameError: name 'health' is not defined. Did you mean: 'health_df'?
print(
    df[df["Indicator"].str.contains("obese|overweight", case=False, na=False)]["Indicator"].unique()
)
                                    
<StringArray>
[]
Length: 0, dtype: str
plt.style.use("ggplot")
                                    
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\NFHS-5-States.csv")
                                    
df.head()
                                    
   state state_code  ... nfhs5_total  nfhs4_total
0  India        NaN  ...        71.8         68.8
1  India        NaN  ...        26.5         28.6
2  India        NaN  ...      1020.0        991.0
3  India        NaN  ...       929.0        919.0
4  India        NaN  ...        89.1         79.7

[5 rows x 7 columns]
df.info()
                                    
<class 'pandas.DataFrame'>
RangeIndex: 4847 entries, 0 to 4846
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   state        4847 non-null   str    
 1   state_code   4716 non-null   str    
 2   indicator    4847 non-null   str    
 3   nfhs5_urban  4693 non-null   float64
 4   nfhs5_rural  4635 non-null   float64
 5   nfhs5_total  4799 non-null   float64
 6   nfhs4_total  3660 non-null   float64
dtypes: float64(4), str(3)
memory usage: 265.2 KB
print(df.columns)
KeyboardInterrupt
print(df.columns)
                                    
Index(['state', 'state_code', 'indicator', 'nfhs5_urban', 'nfhs5_rural',
       'nfhs5_total', 'nfhs4_total'],
      dtype='str')
health = df[
    [
        "State",
        "Obesity_Women",
        "Obesity_Men",
        "Anaemia_Women",
        "Anaemia_Children",
        "High_Blood_Sugar_Women",
        "High_Blood_Sugar_Men",
        "Hypertension_Women",
        "Hypertension_Men"
    ]
]
                                    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    health = df[
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4384, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 6302, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 6352, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['State', 'Obesity_Women', 'Obesity_Men', 'Anaemia_Women',\n       'Anaemia_Children', 'High_Blood_Sugar_Women', 'High_Blood_Sugar_Men',\n       'Hypertension_Women', 'Hypertension_Men'],\n      dtype='str')] are in the [columns]"

df = pd.read_csv(r"C:\Users\Lenovo\Downloads\datafile.csv")
df.head()
                  States/UTs  ... Unnamed: 136
0                      India  ...          NaN
1                      India  ...          NaN
2                      India  ...          NaN
3  Andaman & Nicobar Islands  ...          NaN
4  Andaman & Nicobar Islands  ...          NaN

[5 rows x 137 columns]
health = df[[
    "States/UTs",

    "Women (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)",

    "Men (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2) (%)",

    "Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)",

    "All women age 15-49 years who are anaemic22 (%)",

    "Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)",

    "Men age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level  or taking medicine to control blood sugar level23 (%)",

    "Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)",

    "Men age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)"
]]
health.columns = [

    "State",

    "Obesity_Women",

    "Obesity_Men",

    "Anaemia_Children",

    "Anaemia_Women",

    "BloodSugar_Women",

    "BloodSugar_Men",

    "Hypertension_Women",

    "Hypertension_Men"
]

health = health[
    ~health["State"].isin(["India"])
]

for col in health.columns[1:]:

    health[col] = pd.to_numeric(
        health[col],
        errors="coerce"
    )
health = health.fillna(
    health.mean(numeric_only=True)
)
SyntaxError: invalid syntax
health = health.fillna(
    health.mean(numeric_only=True)
)
health = health.fillna(
    health.mean(numeric_only=True)
)

health["Gender_Obesity_Gap"] = (

    health["Obesity_Women"]

    -

    health["Obesity_Men"]

)
Traceback (most recent call last):
  File "<pyshell#82>", line 3, in <module>
    health["Obesity_Women"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\series.py", line 6751, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\base.py", line 1644, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
health["Gender_Obesity_Gap"] = (

    health["Obesity_Women"]

    -

    health["Obesity_Men"]

)
Traceback (most recent call last):
  File "<pyshell#83>", line 3, in <module>
    health["Obesity_Women"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\series.py", line 6751, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\base.py", line 1644, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'

health["Gender_Obesity_Gap"] = (

    health["Obesity_Women"]

    -

    health["Obesity_Men"]

)
Traceback (most recent call last):
  File "<pyshell#84>", line 3, in <module>
    health["Obesity_Women"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\series.py", line 6751, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\base.py", line 1644, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'

print(health.dtypes)
State                 str
Obesity_Women         str
Obesity_Men           str
Anaemia_Children      str
Anaemia_Women         str
BloodSugar_Women      str
BloodSugar_Men        str
Hypertension_Women    str
Hypertension_Men      str
dtype: object
print(health["Obesity_Women"].head(10))
3     41.7 
4     35.7 
5     38.1 
6     44.4 
7     32.6 
8      36.3
9     28.9 
10    22.9 
11    23.9 
12    23.8 
Name: Obesity_Women, dtype: str
print(health["Obesity_Men"].head(10))
3     37.0 
4     50.6 
5     45.3 
6     37.7 
7     28.0 
8      31.1
9     32.4 
10    26.6 
11    27.6 
12    25.4 
Name: Obesity_Men, dtype: str
health["Obesity_Women"] = pd.to_numeric(
    health["Obesity_Women"],
    errors="coerce"
)
health["Obesity_Men"] = pd.to_numeric(
    health["Obesity_Men"],
    errors="coerce"
)
health["Obesity_Women"] = health["Obesity_Women"].replace("-", np.nan)
health["Obesity_Men"] = health["Obesity_Men"].replace("-", np.nan)
health["Obesity_Women"] = pd.to_numeric(health["Obesity_Women"], errors="coerce")
health["Obesity_Men"] = pd.to_numeric(health["Obesity_Men"], errors="coerce")
health["Obesity_Women"] = health["Obesity_Women"].fillna(
    health["Obesity_Women"].mean()
)

health["Obesity_Men"] = health["Obesity_Men"].fillna(
    health["Obesity_Men"].mean()
)

health["Gender_Obesity_Gap"] = (
    health["Obesity_Women"] - health["Obesity_Men"]
)
numeric_cols = [
    "Obesity_Women",
    "Obesity_Men",
    "Anaemia_Children",
    "Anaemia_Women",
    "BloodSugar_Women",
    "BloodSugar_Men",
    "Hypertension_Women",
    "Hypertension_Men"
]



for col in numeric_cols:
    health[col] = (
        health[col]
        .astype(str)
        .str.strip()          # remove extra spaces
        .replace("-", np.nan) # replace hyphens with NaN
    )
    health[col] = pd.to_numeric(health[col], errors="coerce")

 health[col] = health[col].fillna(health[col].mean())
 
SyntaxError: unexpected indent
for col in numeric_cols:
    health[col] = (
        health[col]
        .astype(str)
        .str.strip()          # remove extra spaces
        .replace("-", np.nan) # replace hyphens with NaN
    )
    health[col] = pd.to_numeric(health[col], errors="coerce")
    health[col] = health[col].fillna(health[col].mean())

    

print(health.dtypes)
State                     str
Obesity_Women         float64
Obesity_Men           float64
Anaemia_Children      float64
Anaemia_Women         float64
BloodSugar_Women      float64
BloodSugar_Men        float64
Hypertension_Women    float64
Hypertension_Men      float64
Gender_Obesity_Gap    float64
dtype: object
correlation = health["Anaemia_Children"].corr(health["Obesity_Women"])

print("Pearson Correlation:", correlation)
Pearson Correlation: -0.16364932754854142
corr = health.corr(numeric_only=True)

plt.figure(figsize=(10,8))
<Figure size 1000x800 with 0 Axes>
plt.imshow(corr, cmap="coolwarm")
<matplotlib.image.AxesImage object at 0x00000208FBEE02F0>
plt.colorbar()

<matplotlib.colorbar.Colorbar object at 0x00000208FBEE16A0>
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
([<matplotlib.axis.XTick object at 0x00000208FBEBECF0>, <matplotlib.axis.XTick object at 0x00000208FBEF6E90>, <matplotlib.axis.XTick object at 0x00000208FBEF7250>, <matplotlib.axis.XTick object at 0x00000208FBEF7610>, <matplotlib.axis.XTick object at 0x00000208FBEF79D0>, <matplotlib.axis.XTick object at 0x00000208FBEF7D90>, <matplotlib.axis.XTick object at 0x00000208FBF34190>, <matplotlib.axis.XTick object at 0x00000208FBF34550>, <matplotlib.axis.XTick object at 0x00000208FBF34910>], [Text(0, 0, 'Obesity_Women'), Text(1, 0, 'Obesity_Men'), Text(2, 0, 'Anaemia_Children'), Text(3, 0, 'Anaemia_Women'), Text(4, 0, 'BloodSugar_Women'), Text(5, 0, 'BloodSugar_Men'), Text(6, 0, 'Hypertension_Women'), Text(7, 0, 'Hypertension_Men'), Text(8, 0, 'Gender_Obesity_Gap')])
plt.yticks(range(len(corr.columns)), corr.columns)

([<matplotlib.axis.YTick object at 0x00000208FBEBF4D0>, <matplotlib.axis.YTick object at 0x00000208FBECD590>, <matplotlib.axis.YTick object at 0x00000208FBF34F50>, <matplotlib.axis.YTick object at 0x00000208FBF35310>, <matplotlib.axis.YTick object at 0x00000208FBF356D0>, <matplotlib.axis.YTick object at 0x00000208FBF35A90>, <matplotlib.axis.YTick object at 0x00000208FBF35E50>, <matplotlib.axis.YTick object at 0x00000208FBF36210>, <matplotlib.axis.YTick object at 0x00000208FBF365D0>], [Text(0, 0, 'Obesity_Women'), Text(0, 1, 'Obesity_Men'), Text(0, 2, 'Anaemia_Children'), Text(0, 3, 'Anaemia_Women'), Text(0, 4, 'BloodSugar_Women'), Text(0, 5, 'BloodSugar_Men'), Text(0, 6, 'Hypertension_Women'), Text(0, 7, 'Hypertension_Men'), Text(0, 8, 'Gender_Obesity_Gap')])
plt.title("Correlation Matrix")
Text(0.5, 1.0, 'Correlation Matrix')
plt.show()
top10 = health.sort_values(
    "Hypertension_Women",
    ascending=False
).head(10)

x = np.arange(len(top10))
width = 0.35
plt.figure(figsize=(12,6))
<Figure size 1200x600 with 0 Axes>
plt.bar(x-width/2, top10["Hypertension_Men"], width, label="Men")
<BarContainer object of 10 artists>
plt.bar(x+width/2, top10["Hypertension_Women"], width, label="Women")

<BarContainer object of 10 artists>
plt.xticks(x, top10["State"], rotation=45, ha="right")
([<matplotlib.axis.XTick object at 0x00000208FBF8ED50>, <matplotlib.axis.XTick object at 0x00000208FC55DA90>, <matplotlib.axis.XTick object at 0x00000208FC55DE50>, <matplotlib.axis.XTick object at 0x00000208FC55E210>, <matplotlib.axis.XTick object at 0x00000208FC55E5D0>, <matplotlib.axis.XTick object at 0x00000208FC55E990>, <matplotlib.axis.XTick object at 0x00000208FC55ED50>, <matplotlib.axis.XTick object at 0x00000208FC55F110>, <matplotlib.axis.XTick object at 0x00000208FC55F4D0>, <matplotlib.axis.XTick object at 0x00000208FC55F890>], [Text(0, 0, 'Sikkim'), Text(1, 0, 'Sikkim'), Text(2, 0, 'Sikkim'), Text(3, 0, 'Punjab'), Text(4, 0, 'Punjab'), Text(5, 0, 'Kerala'), Text(6, 0, 'Kerala'), Text(7, 0, 'Punjab'), Text(8, 0, 'Kerala'), Text(9, 0, 'Telangana')])
plt.ylabel("Percentage (%)")
Text(0, 0.5, 'Percentage (%)')
plt.xlabel("States")
Text(0.5, 0, 'States')
plt.title("Top 10 States with Highest Hypertension")
Text(0.5, 1.0, 'Top 10 States with Highest Hypertension')
plt.legend()
<matplotlib.legend.Legend object at 0x00000208FC4EF4D0>
plt.tight_layout()
plt.show()
plt.figure(figsize=(10,8))
<Figure size 1000x800 with 0 Axes>
plt.scatter(
    health["Anaemia_Women"],
    health["Obesity_Women"]
)

<matplotlib.collections.PathCollection object at 0x00000208FC5CA3C0>

for _, row in health.iterrows():
    plt.text(
        row["Anaemia_Women"],
        row["Obesity_Women"],
        row["State"][:3],
        fontsize=8
    )

    
Text(57.2, 41.7, 'And')
Text(57.6, 35.7, 'And')
Text(57.5, 38.1, 'And')
Text(57.8, 44.4, 'And')
Text(59.3, 32.6, 'And')
Text(58.8, 36.3, 'And')
Text(36.5, 28.9, 'Aru')
Text(41.0, 22.9, 'Aru')
Text(40.3, 23.9, 'Aru')
Text(65.2, 23.8, 'Ass')
Text(66.0, 13.6, 'Ass')
Text(65.9, 15.2, 'Ass')
Text(65.6, 25.2, 'Bih')
Text(63.1, 14.2, 'Bih')
Text(63.5, 15.9, 'Bih')
Text(60.3, 43.9, 'Cha')
Text(53.566981132075476, 28.63867924528302, 'Cha')
Text(60.3, 44.0, 'Cha')
Text(56.5, 23.1, 'Chh')
Text(62.2, 11.3, 'Chh')
Text(60.8, 14.1, 'Chh')
Text(60.5, 34.0, 'Dad')
Text(64.4, 20.3, 'Dad')
Text(62.5, 26.8, 'Dad')
Text(40.0, 38.1, 'Goa')
Text(37.4, 33.1, 'Goa')
Text(39.0, 36.1, 'Goa')
Text(61.3, 30.4, 'Guj')
Text(67.6, 17.0, 'Guj')
Text(65.0, 22.6, 'Guj')
Text(57.4, 37.5, 'Har')
Text(61.9, 30.9, 'Har')
Text(60.4, 33.1, 'Har')
Text(51.0, 38.3, 'Him')
Text(53.3, 29.2, 'Him')
Text(53.0, 30.4, 'Him')
Text(61.4, 33.4, 'Jam')
Text(67.5, 27.9, 'Jam')
Text(65.9, 29.3, 'Jam')
Text(61.1, 21.6, 'Jha')
Text(66.7, 8.6, 'Jha')
Text(65.3, 11.9, 'Jha')
Text(43.9, 37.1, 'Kar')
Text(50.3, 25.6, 'Kar')
Text(47.8, 30.1, 'Kar')
Text(37.0, 40.4, 'Ker')
Text(35.8, 36.0, 'Ker')
Text(36.3, 38.1, 'Ker')
Text(89.5, 28.5, 'Lad')
Text(93.5, 28.2, 'Lad')
Text(92.8, 28.3, 'Lad')
Text(26.4, 34.2, 'Lak')
Text(23.7, 31.0, 'Lak')
Text(25.8, 33.5, 'Lak')
Text(51.5, 26.0, 'Mad')
Text(55.8, 13.0, 'Mad')
Text(54.7, 16.6, 'Mad')
Text(52.0, 29.6, 'Mah')
Text(56.1, 18.3, 'Mah')
Text(54.2, 23.4, 'Mah')
Text(30.5, 39.0, 'Man')
Text(28.8, 31.0, 'Man')
Text(29.4, 34.1, 'Man')
Text(51.8, 17.9, 'Meg')
Text(54.3, 9.7, 'Meg')
Text(53.8, 11.5, 'Meg')
Text(30.8, 29.7, 'Miz')
Text(39.9, 16.9, 'Miz')
Text(34.8, 24.2, 'Miz')
Text(27.3, 17.1, 'Nag')
Text(29.8, 13.0, 'Nag')
Text(28.9, 14.4, 'Nag')
Text(49.7, 41.2, 'NCT')
Text(58.6, 44.6, 'NCT')
Text(49.9, 41.3, 'NCT')
Text(61.5, 40.1, 'Odi')
Text(64.9, 19.2, 'Odi')
Text(64.3, 23.0, 'Odi')
Text(52.3, 47.6, 'Pud')
Text(61.4, 43.2, 'Pud')
Text(55.1, 46.2, 'Pud')
Text(59.0, 44.3, 'Pun')
Text(58.5, 38.8, 'Pun')
Text(58.7, 40.8, 'Pun')
Text(49.9, 20.6, 'Raj')
Text(55.7, 10.5, 'Raj')
Text(54.4, 12.9, 'Raj')
Text(42.4, 41.0, 'Sik')
Text(41.9, 30.8, 'Sik')
Text(42.1, 34.7, 'Sik')
Text(51.3, 46.1, 'Tam')
Text(55.3, 35.4, 'Tam')
Text(53.4, 40.4, 'Tam')
Text(55.2, 41.7, 'Tel')
Text(58.9, 23.8, 'Tel')
Text(57.6, 30.1, 'Tel')
Text(66.1, 29.2, 'Tri')
Text(67.6, 18.4, 'Tri')
Text(67.2, 21.5, 'Tri')
Text(50.1, 30.6, 'Utt')
Text(50.5, 18.3, 'Utt')
Text(50.4, 21.3, 'Utt')
Text(45.8, 39.1, 'Utt')
Text(41.1, 25.4, 'Utt')
Text(42.6, 29.7, 'Utt')
Text(65.1, 27.9, 'Wes')
Text(74.4, 20.3, 'Wes')
plt.xlabel("Anaemia among Women (%)")
Text(0.5, 0, 'Anaemia among Women (%)')
KeyboardInterrupt
plt.ylabel("Obesity among Women (%)")
plt.ylabel("Obesity among Women (%)")
Text(0, 0.5, 'Obesity among Women (%)')
plt.title("Anaemia vs Obesity")
Text(0.5, 1.0, 'Anaemia vs Obesity')
plt.grid(True)
plt.show()
print(health.dtypes)
State                     str
Obesity_Women         float64
Obesity_Men           float64
Anaemia_Children      float64
Anaemia_Women         float64
BloodSugar_Women      float64
BloodSugar_Men        float64
Hypertension_Women    float64
Hypertension_Men      float64
Gender_Obesity_Gap    float64
dtype: object
print(health.head())
                       State  ...  Gender_Obesity_Gap
3  Andaman & Nicobar Islands  ...                 4.7
4  Andaman & Nicobar Islands  ...               -14.9
5  Andaman & Nicobar Islands  ...                -7.2
6             Andhra Pradesh  ...                 6.7
7             Andhra Pradesh  ...                 4.6

[5 rows x 10 columns]
plt.show()


df.columns
Index(['States/UTs', 'Area', 'Number of Households surveyed',
       'Number of Women age 15-49 years interviewed',
       'Number of Men age 15-54 years interviewed',
       'Female population age 6 years and above who ever attended school (%)',
       'Population below age 15 years (%)',
       ' Sex ratio of the total population (females per 1,000 males)',
       'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
       'Children under age 5 years whose birth was registered with the civil authority (%)',
       ...
       'Women (age 15-49 years) having a mobile phone that they themselves use (%)',
       'Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)',
       'Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)',
       'Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)',
       'Young women age 18-29 years who experienced sexual violence by age 18 (%)',
       'Women age 15 years and above who use any kind of tobacco (%)',
       'Men age 15 years and above who use any kind of tobacco (%)',
       'Women age 15 years and above who consume alcohol (%)',
       'Men age 15 years and above who consume alcohol (%)', 'Unnamed: 136'],
      dtype='str', length=137)
print(df.head())
                  States/UTs  ... Unnamed: 136
0                      India  ...          NaN
1                      India  ...          NaN
2                      India  ...          NaN
3  Andaman & Nicobar Islands  ...          NaN
4  Andaman & Nicobar Islands  ...          NaN

[5 rows x 137 columns]
print(df.iloc[:10])
                  States/UTs  ... Unnamed: 136
0                      India  ...          NaN
1                      India  ...          NaN
2                      India  ...          NaN
3  Andaman & Nicobar Islands  ...          NaN
4  Andaman & Nicobar Islands  ...          NaN
5  Andaman & Nicobar Islands  ...          NaN
6             Andhra Pradesh  ...          NaN
7             Andhra Pradesh  ...          NaN
8             Andhra Pradesh  ...          NaN
9          Arunachal Pradesh  ...          NaN

[10 rows x 137 columns]
health = health[health["Residence"] == "Total"]
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Residence'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    health = health[health["Residence"] == "Total"]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Residence'
health["Gender_Obesity_Gap"] = (
    health["Obesity_Women"] -
    health["Obesity_Men"]
)

correlation = health["Anaemia_Children"].corr(
    health["Obesity_Women"]
)

print(correlation)
-0.16364932754854142
top10 = health.sort_values(
    "Hypertension_Women",
    ascending=False
).head(10)
top10 = health.sort_values(
    "Hypertension_Women",
    ascending=False
).head(10)
import folium
india_map = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)
india_map
<folium.folium.Map object at 0x0000020883462BA0>


import os

print(os.path.exists(r"C:\Users\Lenovo\Downloads\india_states.geojson"))
False
print(os.path.exists(r"C:\Users\Lenovo\Downloads\india_states.geojson"))
False

import json
with open(r"C:\Users\Lenovo\Downloads\india_state.geojson.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

    
print("Loaded successfully!")
Loaded successfully!
print(data["features"][0]["properties"])
{'ID_0': 105, 'ISO': 'IND', 'NAME_0': 'India', 'ID_1': 1, 'NAME_1': 'Andaman and Nicobar', 'NL_NAME_1': None, 'VARNAME_1': 'Andaman & Nicobar Islands|Andaman et Nicobar|Iihas de Andama e Nicobar|Inseln Andamanen und Nikobare', 'TYPE_1': 'Union Territor', 'ENGTYPE_1': 'Union Territory'}
import folium
india_map = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)
print(health["State"].unique())
<StringArray>
[             'Andaman & Nicobar Islands',
                         'Andhra Pradesh',
                      'Arunachal Pradesh',
                                  'Assam',
                                  'Bihar',
                             'Chandigarh',
                           'Chhattisgarh',
 'Dadra and Nagar Haveli & Daman and Diu',
                                    'Goa',
                                'Gujarat',
                                'Haryana',
                       'Himachal Pradesh',
                        'Jammu & Kashmir',
                              'Jharkhand',
                              'Karnataka',
                                 'Kerala',
                                 'Ladakh',
                            'Lakshadweep',
                         'Madhya Pradesh',
                             'Maharastra',
                                'Manipur',
                              'Meghalaya',
                                'Mizoram',
                               'Nagaland',
                           'NCT of Delhi',
                                 'Odisha',
                             'Puducherry',
                                 'Punjab',
                              'Rajasthan',
                                 'Sikkim',
                             'Tamil Nadu',
                              'Telangana',
                                'Tripura',
                          'Uttar Pradesh',
                            'Uttarakhand',
                            'West Bengal']
Length: 36, dtype: str
health["State"] = health["State"].replace({
    "Andaman & Nicobar Islands": "Andaman and Nicobar",
    "NCT of Delhi": "Delhi",
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Odisha": "Odisha",
    "Dadra & Nagar Haveli and Daman & Diu":
        "Dadra and Nagar Haveli and Daman and Diu"
})
folium.Choropleth(
    geo_data=r"C:\Users\Lenovo\Downloads\india_state.geojson.txt",
    data=health,
    columns=["State", "Obesity_Women"],
    key_on="feature.properties.NAME_1",
    fill_color="YlOrRd",
    fill_opacity=0.8,
    line_opacity=0.3,
    legend_name="Women Obesity (%)"
).add_to(india_map)
<folium.features.Choropleth object at 0x00000208837A5160>
state_capitals = {
    "Andhra Pradesh": [15.9129,79.7400],
    "Arunachal Pradesh":[28.2180,94.7278],
    "Assam":[26.2006,92.9376],
    "Bihar":[25.0961,85.3131],
    "Chhattisgarh":[21.2514,81.6296],
    "Goa":[15.2993,74.1240],
    "Gujarat":[22.2587,71.1924],
    "Haryana":[29.0588,76.0856],
    "Himachal Pradesh":[31.1048,77.1734],
    "Jharkhand":[23.6102,85.2799],
    "Karnataka":[15.3173,75.7139],
    "Kerala":[10.8505,76.2711],
    "Madhya Pradesh":[22.9734,78.6569],
    "Maharashtra":[19.7515,75.7139],
    "Manipur":[24.6637,93.9063],
    "Meghalaya":[25.4670,91.3662],
    "Mizoram":[23.1645,92.9376],
    "Nagaland":[26.1584,94.5624],
    "Odisha":[20.9517,85.0985],
    "Punjab":[31.1471,75.3412],
    "Rajasthan":[27.0238,74.2179],
    "Sikkim":[27.5330,88.5122],
    "Tamil Nadu":[11.1271,78.6569],
    "Telangana":[18.1124,79.0193],
    "Tripura":[23.9408,91.9882],
    "Uttar Pradesh":[26.8467,80.9462],
    "Uttarakhand":[30.0668,79.0193],
    "West Bengal":[22.9868,87.8550],
    "Delhi":[28.6139,77.2090],
    "Puducherry":[11.9416,79.8083],
    "Lakshadweep":[10.5667,72.6417],
    "Andaman and Nicobar":[11.7401,92.6586],
    "Ladakh":[34.1526,77.5771]
}
for _, row in health.iterrows():

    if row["State"] in state_capitals:

        folium.CircleMarker(
            location=state_capitals[row["State"]],
            radius=6,
            color="blue",
            fill=True,
            fill_color="red",
            popup=f"""
            <b>{row['State']}</b><br>
            Women Obesity: {row['Obesity_Women']}%<br>
            Blood Sugar: {row['BloodSugar_Women']}%<br>
            Anaemia: {row['Anaemia_Women']}%
            """
        ).add_to(india_map)

        
<folium.vector_layers.CircleMarker object at 0x00000208837A5400>
<folium.vector_layers.CircleMarker object at 0x000002088C5F2850>
<folium.vector_layers.CircleMarker object at 0x000002088C5F2C10>
<folium.vector_layers.CircleMarker object at 0x0000020883472780>
<folium.vector_layers.CircleMarker object at 0x0000020883472B10>
<folium.vector_layers.CircleMarker object at 0x0000020882D315B0>
<folium.vector_layers.CircleMarker object at 0x0000020883675D00>
<folium.vector_layers.CircleMarker object at 0x0000020883676030>
<folium.vector_layers.CircleMarker object at 0x0000020891790350>
<folium.vector_layers.CircleMarker object at 0x0000020891790750>
<folium.vector_layers.CircleMarker object at 0x0000020883797A70>
<folium.vector_layers.CircleMarker object at 0x0000020883797D40>
<folium.vector_layers.CircleMarker object at 0x0000020891FEC3D0>
<folium.vector_layers.CircleMarker object at 0x0000020891FEC670>
<folium.vector_layers.CircleMarker object at 0x000002088365C050>
<folium.vector_layers.CircleMarker object at 0x000002088B86F1D0>
<folium.vector_layers.CircleMarker object at 0x000002088B86F4D0>
<folium.vector_layers.CircleMarker object at 0x00000208836E85D0>
<folium.vector_layers.CircleMarker object at 0x00000208836E87E0>
<folium.vector_layers.CircleMarker object at 0x00000208838151D0>
<folium.vector_layers.CircleMarker object at 0x00000208838153B0>
<folium.vector_layers.CircleMarker object at 0x00000208FC5911D0>
<folium.vector_layers.CircleMarker object at 0x0000020883815630>
<folium.vector_layers.CircleMarker object at 0x000002088346FA70>
<folium.vector_layers.CircleMarker object at 0x00000208838158B0>
<folium.vector_layers.CircleMarker object at 0x00000208838159F0>
<folium.vector_layers.CircleMarker object at 0x00000208838154F0>
<folium.vector_layers.CircleMarker object at 0x0000020883815C70>
<folium.vector_layers.CircleMarker object at 0x0000020883815770>
<folium.vector_layers.CircleMarker object at 0x0000020883815EF0>
<folium.vector_layers.CircleMarker object at 0x0000020883816030>
<folium.vector_layers.CircleMarker object at 0x0000020883815B30>
<folium.vector_layers.CircleMarker object at 0x00000208838162B0>
<folium.vector_layers.CircleMarker object at 0x0000020883815DB0>
<folium.vector_layers.CircleMarker object at 0x0000020883816530>
<folium.vector_layers.CircleMarker object at 0x0000020883816670>
<folium.vector_layers.CircleMarker object at 0x0000020883816170>
<folium.vector_layers.CircleMarker object at 0x00000208838168F0>
<folium.vector_layers.CircleMarker object at 0x00000208838163F0>
<folium.vector_layers.CircleMarker object at 0x0000020883816B70>
<folium.vector_layers.CircleMarker object at 0x0000020883816CB0>
<folium.vector_layers.CircleMarker object at 0x00000208838167B0>
<folium.vector_layers.CircleMarker object at 0x0000020883816F30>
<folium.vector_layers.CircleMarker object at 0x0000020883816A30>
<folium.vector_layers.CircleMarker object at 0x00000208838171B0>
<folium.vector_layers.CircleMarker object at 0x00000208838172F0>
<folium.vector_layers.CircleMarker object at 0x0000020883816DF0>
<folium.vector_layers.CircleMarker object at 0x0000020883817570>
<folium.vector_layers.CircleMarker object at 0x0000020883817070>
<folium.vector_layers.CircleMarker object at 0x00000208838177F0>
<folium.vector_layers.CircleMarker object at 0x0000020883817930>
<folium.vector_layers.CircleMarker object at 0x0000020883817430>
<folium.vector_layers.CircleMarker object at 0x0000020883817BB0>
<folium.vector_layers.CircleMarker object at 0x00000208838176B0>
<folium.vector_layers.CircleMarker object at 0x0000020883817E30>
<folium.vector_layers.CircleMarker object at 0x0000020883817F70>
<folium.vector_layers.CircleMarker object at 0x0000020883817A70>
<folium.vector_layers.CircleMarker object at 0x000002088D030230>
<folium.vector_layers.CircleMarker object at 0x0000020883817CF0>
<folium.vector_layers.CircleMarker object at 0x000002088D0304B0>
<folium.vector_layers.CircleMarker object at 0x000002088D0305F0>
<folium.vector_layers.CircleMarker object at 0x000002088D0300F0>
<folium.vector_layers.CircleMarker object at 0x000002088D030870>
<folium.vector_layers.CircleMarker object at 0x000002088D030370>
<folium.vector_layers.CircleMarker object at 0x000002088D030AF0>
<folium.vector_layers.CircleMarker object at 0x000002088D030C30>
<folium.vector_layers.CircleMarker object at 0x000002088D030730>
<folium.vector_layers.CircleMarker object at 0x000002088D030EB0>
<folium.vector_layers.CircleMarker object at 0x000002088D0309B0>
<folium.vector_layers.CircleMarker object at 0x000002088D031130>
<folium.vector_layers.CircleMarker object at 0x000002088D031270>
<folium.vector_layers.CircleMarker object at 0x000002088D030D70>
<folium.vector_layers.CircleMarker object at 0x000002088D0314F0>
<folium.vector_layers.CircleMarker object at 0x000002088D030FF0>
<folium.vector_layers.CircleMarker object at 0x000002088D031770>
<folium.vector_layers.CircleMarker object at 0x000002088D0318B0>
<folium.vector_layers.CircleMarker object at 0x000002088D0313B0>
<folium.vector_layers.CircleMarker object at 0x000002088D031B30>
<folium.vector_layers.CircleMarker object at 0x000002088D031630>
<folium.vector_layers.CircleMarker object at 0x000002088D031DB0>
<folium.vector_layers.CircleMarker object at 0x000002088D031EF0>
<folium.vector_layers.CircleMarker object at 0x000002088D0319F0>
<folium.vector_layers.CircleMarker object at 0x000002088D032170>
<folium.vector_layers.CircleMarker object at 0x000002088D031C70>
<folium.vector_layers.CircleMarker object at 0x000002088D0323F0>
<folium.vector_layers.CircleMarker object at 0x000002088D032530>
<folium.vector_layers.CircleMarker object at 0x000002088D032030>
<folium.vector_layers.CircleMarker object at 0x000002088D0327B0>
<folium.vector_layers.CircleMarker object at 0x000002088D0322B0>
<folium.vector_layers.CircleMarker object at 0x000002088D032A30>
<folium.vector_layers.CircleMarker object at 0x000002088D032B70>
<folium.vector_layers.CircleMarker object at 0x000002088D032670>
<folium.vector_layers.CircleMarker object at 0x000002088D032DF0>
<folium.vector_layers.CircleMarker object at 0x000002088D0328F0>
<folium.vector_layers.CircleMarker object at 0x000002088D033070>
>>> india_map.save("NFHS_Health_Dashboard.html")
