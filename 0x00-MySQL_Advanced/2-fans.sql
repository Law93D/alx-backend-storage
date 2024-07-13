-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT u.id, u.email, u.name, COUNT(l.id) AS like_count
FROM users u
JOIN likes l ON u.id = l.user_id
GROUP BY u.id
HAVING like_count > 10;
