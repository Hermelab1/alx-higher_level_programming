#!/bin/bash

mysql -h localhost -u hbtn_0d_admin -pArl1784 hbtn_0d_tvshows_rate -e 
"SELECT tv_shows.title, SUM(rates.rating) AS total_rating FROM tv_shows 
LEFT JOIN rates ON tv_shows.id = rates.tv_show_id 
GROUP BY tv_shows.title 
ORDER BY total_rating DESC;"
