SELECT t.artist, t.title
FROM tracks t
GROUP BY t.artist, t.title
ORDER BY t.artist ASC;
