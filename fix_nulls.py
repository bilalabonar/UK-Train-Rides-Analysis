import pandas as pd
import os

# Load Fact_Tickets
path = r'PowerBI_Model\Fact_Tickets.csv'
df = pd.read_csv(path)

print('=== BEFORE FIX ===')
print('ActualArrivalTime nulls:', df['ActualArrivalTime'].isna().sum())
print('ReasonForDelay nulls:', df['ReasonForDelay'].isna().sum())
print('DelayMinutes nulls:', df['DelayMinutes'].isna().sum())
print()

# Fix 1: ReasonForDelay - fill empty with 'No Delay'
df['ReasonForDelay'] = df['ReasonForDelay'].fillna('No Delay')

# Fix 2: DelayMinutes - fill empty with 0
df['DelayMinutes'] = df['DelayMinutes'].fillna(0)

# Fix 3: ActualArrivalTime - fill cancelled with 'Cancelled'
df['ActualArrivalTime'] = df['ActualArrivalTime'].fillna('Cancelled')

print('=== AFTER FIX ===')
print('ActualArrivalTime nulls:', df['ActualArrivalTime'].isna().sum())
print('ReasonForDelay nulls:', df['ReasonForDelay'].isna().sum())
print('DelayMinutes nulls:', df['DelayMinutes'].isna().sum())
print()

# Full data type review of ALL columns
print('=== FULL DATA TYPE REVIEW (Fact_Tickets) ===')
print(f'Total Rows: {len(df)}')
print(f'Total Cols: {len(df.columns)}')
print()
for col in df.columns:
    nulls = df[col].isna().sum()
    dtype = df[col].dtype
    uniq = df[col].nunique()
    sample = str(df[col].dropna().iloc[0]) if not df[col].dropna().empty else 'N/A'
    print(f'  {col:25s} | {str(dtype):10s} | Unique: {uniq:6d} | Nulls: {nulls} | Sample: {sample[:30]}')

# Verify key columns (all IDs should have no nulls and be integers)
print()
print('=== KEY COLUMNS CHECK (FK/PK) ===')
key_cols = ['JourneyDateKey','PurchaseDateKey','DepartureStationID','ArrivalStationID',
            'TicketID','PaymentID','RailcardID','DepartureHour']
for col in key_cols:
    nulls = df[col].isna().sum()
    is_int = df[col].dtype in ['int64','int32']
    print(f'  {col:25s} | Nulls: {nulls} | IsInteger: {is_int} | {"PASS" if nulls==0 and is_int else "FAIL"}')

# Verify revenue
print()
rev = df['Price'].sum()
print(f'Revenue Check: {rev} (expected 741921) {"PASS" if rev == 741921 else "FAIL"}')

# Save fixed Fact_Tickets
df.to_csv(path, index=False, encoding='utf-8-sig')
print(f'\nSaved fixed Fact_Tickets.csv!')

# Now review ALL Dim tables too
print('\n' + '='*60)
print('=== DIMENSION TABLES REVIEW ===')
print('='*60)

dim_files = ['Dim_Date.csv', 'Dim_Station.csv', 'Dim_Ticket.csv', 
             'Dim_Payment.csv', 'Dim_Railcard.csv', 'Dim_Time.csv']

for f in dim_files:
    fpath = os.path.join('PowerBI_Model', f)
    d = pd.read_csv(fpath)
    total_nulls = d.isna().sum().sum()
    print(f'\n--- {f} ({len(d)} rows, {len(d.columns)} cols) ---')
    for col in d.columns:
        nulls = d[col].isna().sum()
        dtype = d[col].dtype
        print(f'  {col:20s} | {str(dtype):10s} | Nulls: {nulls} | {"PASS" if nulls==0 else "FAIL"}')
    print(f'  Total Nulls: {total_nulls} {"PASS" if total_nulls==0 else "NEEDS FIX"}')

print('\n\nDone! All checks complete.')
