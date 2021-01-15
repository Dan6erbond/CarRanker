DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `url` VARCHAR(256) NOT NULL,
  `make` VARCHAR(64) NOT NULL,
  `model` VARCHAR(64) NOT NULL,
  `type` VARCHAR(256),
  `type_full` VARCHAR(256),
  `price` INTEGER NOT NULL,
  `horse_power` INTEGER NOT NULL,
  `transmission_type` VARCHAR(64) NOT NULL,
  `fuel_type` VARCHAR(64) NOT NULL,
  `seats` INTEGER NOT NULL,
  `doors` INTEGER NOT NULL,
  `drive_type` VARCHAR(64) NOT NULL,
  `mileage` INTEGER NOT NULL,
  `consumption_combined` REAL NOT NULL,
  `condition_type` VARCHAR(64) NOT NULL,
  `consumption_category` VARCHAR(8),
  `exterior_front_image` VARCHAR(256) NOT NULL,
  `exterior_side_image` VARCHAR(256) NOT NULL,
  `exterior_back_image` VARCHAR(256) NOT NULL,
  `interior_front_image` VARCHAR(256) NOT NULL,
  `interior_dash_image` VARCHAR(256) NOT NULL,
  `interior_back_image` VARCHAR(256) NOT NULL,
  `interior_trunk_image` VARCHAR(256) NOT NULL,
  `data` TEXT
);

DROP TABLE IF EXISTS car_scores;

CREATE TABLE car_scores (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `interior_score` INTEGER,
  `exterior_score` INTEGER,
  `equipment_score` INTEGER,
  `design_score` INTEGER,
  `run_costs_score` INTEGER,
  `maintenance_score` INTEGER
);

DROP TABLE IF EXISTS score_weights;

CREATE TABLE score_weights (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `interior_weight` INTEGER,
  `exterior_weight` INTEGER,
  `equipment_weight` INTEGER,
  `design_weight` INTEGER,
  `run_costs_weight` INTEGER,
  `maintenance_weight` INTEGER
);
