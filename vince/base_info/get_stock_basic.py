from vince import *

#查询当前所有正常上市交易的股票列表
# df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,list_date,is_hs')

#查询曾用名
# df2 = pro.namechange(ts_code='002456.SZ', fields='ts_code,name,start_date,end_date,change_reason')

#查询沪股通、深股通信息
# df3 = pro.hs_const(hs_type='SH')

#查询上市公司基础信息
# df4 = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')

#IPO新股列表
# df5 = pro.new_share(start_date='20190901', end_date='20190429')

#日线行情
#df6 = pro.daily(ts_code='000001.SZ', start_date='20190428', end_date='20190429')

#周线行情
#df7 = pro.weekly(trade_date='20181123', fields='ts_code,trade_date,open,high,low,close,vol,amount')

# for stock_i in my_stock:
#     print(pro.suspend(ts_code=stock_i, suspend_date='', resume_date='', fields=''))

df8 = pro.fina_mainbz(ts_code='000627.SZ', type='P')
print(df8)