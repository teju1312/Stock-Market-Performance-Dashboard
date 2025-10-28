CREATE TABLE if not exists company_events (
  symbol VARCHAR(255) NOT NULL,
  company VARCHAR(255) NOT NULL,
  purpose VARCHAR(255) NOT NULL,
  event_date DATE NOT NULL

);
