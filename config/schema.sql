CREATE TABLE account_settings(
  user_id INTEGER NOT NULL,
  email TEXT,
  phone_number INT,
  first_name TEXT,
  last_name TEXT,
  zipcode INT,
  created_on DATETIME
);

CREATE TABLE phone_contacts(
  user_id INTEGER NOT NULL,
  ymdh DATETIME,
  phone_number INT,
  name TEXT
);

CREATE TABLE default_pref(
  user_id INT NOT NULL,
  ymdh DATETIME,
  default_minimum_budget INT NOT NULL,
  default_maximum_budget INT NOT NULL,
  default_dist FLOAT NOT NULL
);

CREATE TABLE friends(
  friend_sender INT,
  friend_receiver INT,
  status INT
);

CREATE TABLE event_proposal(
  event_id INT,
  ymdh DATETIME,
  title TEXT,
  deadline INT,
  status INT,
  final_site_name TEXT,
  final_time DATETIME,
  max_start DATETIME,
  max_end DATETIME,
  final_budget INT,
  final_avg_dist FLOAT,
  final_activity TEXT,
  promo TINYINT
);

CREATE TABLE user_preferences(
  session_id INT NOT NULL,
  user_id INT NOT NULL,
  min_budget INT,
  max_budget INT,
  promo_code TINYINT,
  activity TEXT,
  act_level INT,
  radius FLOAT,
  location TEXT,
  is_admin TINYINT
);

CREATE TABLE preferred_times(
  user_id INT,
  event_id INT,
  start_time DATETIME,
  end_time DATETIME
);

CREATE TABLE allied_businesses(
  name TEXT,
  address TEXT,
  promo TEXT,
  yelpid TEXT,
  sponsorship TINYINT
);