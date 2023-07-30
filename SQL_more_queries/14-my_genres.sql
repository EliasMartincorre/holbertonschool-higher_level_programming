-- FIrst show all genres , second inner join with tv_show_genres
-- only data by the title =c dexter
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
Order BY tv_genres.name ASC