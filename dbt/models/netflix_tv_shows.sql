{{config (
    materialized='table',
)}}

select * from {{ ref('netflix_titles') }}
where type = 'TV Show'
limit 100
