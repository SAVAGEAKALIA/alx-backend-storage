-- Sql task 9:  Optimize search and score
-- Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
CREATE INDEX index_name_first_score
    ON names(name(1), score);
