with 

outcomes as (

   select * from {{ ref('stg_raw__outcomes') }}

)

,session_info as (
    select  
            ParticipantID
            ,SessionsAttend
            ,WeeksAttend
    from outcomes
)


select * from session_info