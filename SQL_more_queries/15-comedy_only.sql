-- only comedy.
-- primero selecciona todos los elementos 
-- se hace coincidir los id se pide el dato es[ecifico]
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
