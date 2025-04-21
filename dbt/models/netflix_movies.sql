{{config (
    materialized='table',
)}}

select * from {{ ref('netflix_titles') }}
where type = 'Movie'
limit 100
