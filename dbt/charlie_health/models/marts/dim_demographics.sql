with 

patient_demographics as (
   
   select * from {{ ref('int_patient_demographics') }}
)

,demographics as (

    select  
             PARTICIPANTID
            ,Age
            ,AgeGroup
            ,Gender
            ,Transgender
            ,SexOrient          AS SexualOrientation
            ,SexOrientBinary    AS SexualOrientationFlag
            ,Therapist
    from patient_demographics
)


select * from demographics