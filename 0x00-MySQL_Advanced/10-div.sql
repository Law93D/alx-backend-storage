-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Delimiter change to handle function creation
DELIMITER $$

-- Create the function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 4)
BEGIN
    DECLARE result DECIMAL(10, 4);

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = CAST(a AS DECIMAL(10, 4)) / CAST(b AS DECIMAL(10, 4));
    END IF;

    RETURN result;
END$$

-- Reset the delimiter to default
DELIMITER ;
