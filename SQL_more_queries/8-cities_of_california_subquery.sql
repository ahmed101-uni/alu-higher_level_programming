-- List cities in the state of california
SELECT id, name FROM cities WHERE state_id IN (
    SELECT id FROM states WHERE name = 'California'
);