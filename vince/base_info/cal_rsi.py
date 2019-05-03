from vince import *

# A=14个数字中正数之和
# B=14个数字中负数之和乘以（-1）
# RSI（14）=A÷（A＋B）×100

#Index(['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close','change', 'pct_chg', 'vol', 'amount'],dtype='object')
df = pro.daily(ts_code='601377.SH', start_date='20190423', end_date='20190429')
# print (df.columns)
# print (df.index)
# print (df.values)
print(df)
SumA = 0
SumB = 0
for i in df.index:
     diff = df['close'][i] - df['pre_close'][i]
     if diff > 0:
        SumA = SumA + diff
     else:
        SumB = SumB + diff

SumB = SumB * -1
RSI = 100 * SumA / (SumA+SumB)
print(RSI)