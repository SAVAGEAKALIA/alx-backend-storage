-- Sql task 5:  Email validation to sent
-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed

DELIMITER $$
CREATE TRIGGER reset_email_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END if;
END$$

DELIMITER ;