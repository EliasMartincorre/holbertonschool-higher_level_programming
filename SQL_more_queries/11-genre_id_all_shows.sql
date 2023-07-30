-- all element of the tv_show list, left join, 
-- muestra el titulo tenga o no un valor de genre_id.
SELECT tv_shows.title, tg.genre_id        
FROM tv_shows 
LEFT JOIN tv_show_genres AS tg
ON tv_shows.id = tg.show_id
ORDER BY tv_shows.title, tg.genre_id ASC;