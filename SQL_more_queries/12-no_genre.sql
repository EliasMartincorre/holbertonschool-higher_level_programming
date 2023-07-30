-- All Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tg.genre_id        
FROM tv_shows 
LEFT JOIN tv_show_genres AS tg
ON tv_shows.id = tg.show_id
WHERE tg.show_id IS NULL
ORDER BY tv_shows.title, tg.genre_id ASC;