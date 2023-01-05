with source as (
    select * from {{ source('charlie_health', 'outcomes')}}
)

,renamed as (
    SELECT 
        -- ID's
        TRY_CAST(ParticipantID as INT)    as ParticipantID

        -- Patient Demographics
       ,Age
      ,AgeGroup
      ,Gender
      ,Transgender
      ,SexOrient
      ,SexOrientBinary
      ,Therapist

       -- Type of discharge

       -- Depression scores (PHQ)
       
      ,PreHLCRefYN         
      ,POSTHLCRefYN        
      ,NewPreHLCAdmYN      
      ,POST_HLCAdmYN       
      ,PreER
      ,POST_ER
      ,DischargeMonth
      ,DischargeCode
      ,IntakeMonth
      ,IntakeDate
      ,DateDischarge
      ,SessionsAttend
      ,WeeksAttend
      ,SessionsAttend2
      ,PrePHQScore
      ,NewPreABASI_Think
      ,NewPreABASI_Solution
      ,NewPostABASI_Think
      ,NewPostABASI_Solution
      ,PreERWhy
      ,POST_ERWhy
      ,PreSelfHarmBinary
      ,PostSelfHarmBinary
      ,PreASQ1Wished
      ,PreASQ2FamBetter
      ,PreASQ3ThoughtsWk
      ,PreASQ5ThoughtsNow
      ,PostASQ1Wished
      ,PostASQ2FamBetter
      ,PostASQ3ThoughtsWk
      ,PostASQ5ThoughtsNow
      ,HLCAdm_PreCH
      ,PreERNum
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
      ,PreCRAFFTQ1DaysDrink
      ,PreCRAFFTQ2DaysMarij
      ,PreCRAFFTQ3DaysOther
      ,PreCRAFFTQ4DaysRelax
      ,PreCRAFFTQ5DaysAlone
      ,PreCRAFFTQ6DaysForget
      ,PreCRAFFTQ7DaysTrouble
      ,PreCRAFFTQ8ToldStop
      ,PreCRAFFTQ9Car
      ,PostCRAFFTQ1DaysDrink
      ,PostCRAFFTQ2DaysMarij
      ,PostCRAFFTQ3DaysOther
      ,PostCRAFFTQ4DaysRelax
      ,PostCRAFFTQ5DaysAlone
      ,PostCRAFFTQ6DaysForget
      ,PostCRAFFTQ7DaysTrouble
      ,PostCRAFFTQ8ToldStop
      ,PostCRAFFTQ9Car
    from source
)


select * from renamed