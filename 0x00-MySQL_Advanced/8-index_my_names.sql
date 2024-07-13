-- SQL script to create an index idx_name_first on the table names for the first letter of name

-- Drop the index if it already exists
DROP INDEX IF EXISTS index_name_first ON names;

-- Create the index
CREATE INDEX index_name_first ON names (LEFT(name, 1));
