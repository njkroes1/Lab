with 

depression_scores as (
   
   select * from {{ ref('int_depression_scores') }}
)

,sessions_attended as (

    select * from {{ ref('int_sessions')}}
)

,outcomes as (
    SELECT  
             S.PARTICIPANTID
            ,S.SESSIONSATTEND
            ,S.WEEKSATTEND
            ,D.PREPHQSCORE
            ,D.POSTPHQSCORE
            ,D.PHQTREND
    FROM    sessions_attended AS S
    INNER JOIN  depression_scores   AS D
        ON  S.PARTICIPANTID = D.PARTICIPANTID
)

select * from outcomes