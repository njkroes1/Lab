with 

outcomes as (

   select * from {{ ref('stg_raw__outcomes') }}

)

,demographics as (
    select  
            ParticipantID
            ,Age
            ,CASE AgeGroup
                WHEN 1 THEN 'Adolescent'
                WHEN 0 THEN 'Young Adult'
             END as AgeGroup
            ,CASE Gender
                WHEN 1 THEN 'Male'
                WHEN 2 THEN 'Female'
                WHEN 3 THEN 'Gender-Fluid'
                WHEN 4 THEN 'Gender-Neutral'
                WHEN 5 THEN 'Gender-Questioning'
                WHEN 6 THEN 'Genderqueer'
                WHEN 7 THEN 'Non-Conforming'
                WHEN 8 THEN 'Non-Binary'
            END as Gender
            ,Transgender
            ,CASE SexOrient
                WHEN 1 THEN 'Asexual or Gray-Sexuality'
                WHEN 2 THEN 'Bisexual'
                WHEN 3 THEN 'Pansexual'
                WHEN 4 THEN 'Gay'
                WHEN 5 THEN 'Heterosexual or Straight'
                WHEN 6 THEN 'Lesbian'
                WHEN 7 THEN 'Queer'
                WHEN 8 THEN 'Questioning'
            END as SexOrient
            ,SexOrientBinary
            ,Therapist
    from outcomes
)


select * from demographics