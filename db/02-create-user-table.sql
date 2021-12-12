CREATE TABLE users (
  id serial PRIMARY KEY,
  email VARCHAR ( 50 ) UNIQUE,
  password VARCHAR ( 250 ),
  first_name VARCHAR ( 50 ),
  family_name VARCHAR ( 50 ),
  city VARCHAR ( 50 )
);