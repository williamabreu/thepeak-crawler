SELECT t.artist, t.title, count(*) AS num
FROM tracks t
GROUP BY t.artist, t.title
ORDER BY num DESC;
