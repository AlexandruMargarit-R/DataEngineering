{{config(
    materialized='table',
)}}

select * from {{ ref('netflix_titles2') }}
limit 100
