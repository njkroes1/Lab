with 

outcomes as (

   select * from {{ ref('stg_raw__outcomes') }}

)


,depression_scores as (
    select  
             ParticipantID
            ,PrePHQScore
            ,PrePHQ1
            ,PrePHQ2
            ,PrePHQ3
            ,PrePHQ4
            ,PrePHQ5
            ,PrePHQ6
            ,PrePHQ7
            ,PrePHQ8
            ,PrePHQ9
            ,PostPHQ1 + PostPHQ2 + PostPHQ3 + PostPHQ4 + PostPHQ5 + PostPHQ6 + PostPHQ7 + PostPHQ8 + PostPHQ9 as PostPHQScore
            ,PostPHQ1
            ,PostPHQ2
            ,PostPHQ3
            ,PostPHQ4
            ,PostPHQ5
            ,PostPHQ6
            ,PostPHQ7
            ,PostPHQ8
            ,PostPHQ9
    from outcomes
)

,categorized as (
    select  
            ParticipantID
            ,PrePHQScore
            ,CASE 
                WHEN PrePHQScore BETWEEN 0 AND 4 THEN 'No/minimal depression'
                WHEN PrePHQScore BETWEEN 5 AND 9 THEN 'Mild depression'
                WHEN PrePHQScore BETWEEN 10 and 14 THEN 'Moderate depression'
                WHEN PrePHQScore BETWEEN 15 and 19 THEN 'Moderately severe depression'
                WHEN PRePHQScore >= 20 THEN 'Severe depression'
            END as PrePHQScoreCategory
            ,PostPHQScore
            ,CASE 
                WHEN PostPHQScore BETWEEN 0 AND 4 THEN 'No/minimal depression'
                WHEN PostPHQScore BETWEEN 5 AND 9 THEN 'Mild depression'
                WHEN PostPHQScore BETWEEN 10 and 14 THEN 'Moderate depression'
                WHEN PostPHQScore BETWEEN 15 and 19 THEN 'Moderately severe depression'
                WHEN PostPHQScore >= 20 THEN 'Severe depression'
            END as PostPHQScoreCategory
            ,PrePHQScore - PostPHQScore AS PHQTrend
            ,PrePHQ1
            ,PrePHQ2
            ,PrePHQ3
            ,PrePHQ4
            ,PrePHQ5
            ,PrePHQ6
            ,PrePHQ7
            ,PrePHQ8
            ,PrePHQ9
            ,PostPHQ1
            ,PostPHQ2
            ,PostPHQ3
            ,PostPHQ4
            ,PostPHQ5
            ,PostPHQ6
            ,PostPHQ7
            ,PostPHQ8
            ,PostPHQ9
    from depression_scores
)


select * from categorized