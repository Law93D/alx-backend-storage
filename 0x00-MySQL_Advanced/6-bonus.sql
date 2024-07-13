-- SQL script to create a stored procedure AddBonus
-- Drop the procedure if it already exists
-- Delimiter change to handle procedure creation
-- Create the procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
	DECLARE v_project_id INT;

	SELECT id INTO v_project_id FROM projects WHERE name = p_project_name;
	IF v_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (p_user_id, v_project_id, p_score);	
    UPDATE users u
    SET u.average_score = (
        SELECT AVG(c.score)
        FROM corrections c
        WHERE c.user_id = p_user_id
    )
    WHERE u.id = p_user_id;
    
END$$
DELIMITER ;
