CREATE TABLE stock_market.stock_prices (
  symbol VARCHAR(10) NOT NULL,
  trade_time DATE NOT NULL,
  open_price DECIMAL(10, 2) NOT NULL,
  high_price DECIMAL(10, 2) NOT NULL,
  low_price DECIMAL(10, 2) NOT NULL,
  close_price DECIMAL(10, 2) NOT NULL,
  volume BIGINT NOT NULL,
  intervals VARCHAR(20) NOT NULL,
  trade_year INT NOT NULL,
  PRIMARY KEY (symbol, trade_time)
);