create or replace view vw_stock_details_cust as 

with window_cte as (
select 
    symbol,
    trade_time,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    intervals,
    trade_year,
    lag(close_price) over (partition by symbol order by trade_time) as prev_close
from stock_prices
)

select *,
round( ( ( close_price - prev_close ) / prev_close ) * 100, 2 ) as pct_change
from window_cte
-- where symbol='TCS' and trade_time='2025-01-02'
order by symbol, trade_time
;


SELECT * FROM stock_market.stock_details_cust;