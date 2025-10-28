CREATE TABLE stock_master (
  symbol VARCHAR(20) NOT NULL,
  token INT NOT NULL,
  intraday_margin DECIMAL(5, 2) DEFAULT NULL,
  name VARCHAR(255) NOT NULL,
  date_of_listing DATE NOT NULL,
  lot DECIMAL(10, 2) NOT NULL,
  paid_up_value DECIMAL(10, 2) NOT NULL,
  isin VARCHAR(20) NOT NULL,
  face_value DECIMAL(10, 2) NOT NULL,
  bse_group CHAR(1) NOT NULL,
  sector VARCHAR(100) NOT NULL,
  industry VARCHAR(100) NOT NULL,
  industry_new VARCHAR(100) NOT NULL,
  igroup VARCHAR(100) NOT NULL,
  isubgroup VARCHAR(100) NOT NULL,
  load_date DATE NOT NULL,
  PRIMARY KEY (symbol, token)
);
ALTER TABLE stock_master 
  MODIFY bse_group CHAR(1) DEFAULT NULL,
  MODIFY sector VARCHAR(100) DEFAULT NULL,
  MODIFY industry VARCHAR(100) DEFAULT NULL,
  MODIFY industry_new VARCHAR(100) DEFAULT NULL,
  MODIFY igroup VARCHAR(100) DEFAULT NULL,
  MODIFY isubgroup VARCHAR(100) DEFAULT NULL;