-- Sql task 8:  Optimize simple search
-- Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.
CREATE INDEX index_name_first
    ON names(name);
