{{config(
    materialized='table'
)}}

select * from {{ref('netflix_titles_post')}} limit 100 
