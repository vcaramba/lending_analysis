import pandas as pd

def clean_dataset(df):
    res = df.copy()
    cols_to_drop = ['loan_paid', 'loan_paid_on', 'loan_is_matured']
    if set(cols_to_drop).issubset(res.columns):
        res = res.drop(cols_to_drop, axis=1)
    res['age'] = round((pd.to_datetime(res['loan_created_on']) - pd.to_datetime(res['client_birth_date'])).dt.days / 365, 1)
    res = res[res['age'] >= 18]
    res.drop(['loan_created_on', 'client_birth_date', 'client_id', 'loan_issued'], axis=1, inplace=True)
    res.set_index('loan_id', inplace=True)
    return res
