CREATE TABLE user (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL
);

CREATE TABLE recordTraining (
  date_skated Date,
  distance_skated INTEGER,
  time_spent Time
);