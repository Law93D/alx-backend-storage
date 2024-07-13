-- SQL script to create a stored procedure ComputeAverageScoreForUser
-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
    user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10,2);

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
    
END$$
DELIMITER ;
