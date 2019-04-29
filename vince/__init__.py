'''
输入参数
名称	类型	必选	描述
is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
list_status	str	N	上市状态： L上市 D退市 P暂停上市
exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)

输出参数
名称	类型	描述
ts_code	str	TS代码
symbol	str	股票代码
name	str	股票名称
area	str	所在地域
industry	str	所属行业
fullname	str	股票全称
enname	str	英文全称
market	str	市场类型 （主板/中小板/创业板）
exchange	str	交易所代码
curr_type	str	交易货币
list_status	str	上市状态： L上市 D退市 P暂停上市
list_date	str	上市日期
delist_date	str	退市日期
is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
'''

import pandas as pd
import tushare as ts

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api('0032c5c89307c3f05daee628ea576ceb2afc87ed5ccdcd033dbe6748')

my_stock = ['600175.SH','001896.SZ','600503.SH','002166.SZ','600122.SH','601377.SH','600636.SH']