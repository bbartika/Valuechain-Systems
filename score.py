def calculate_priority(
    business_impact,
    ai_feasibility,
    data_availability,
    roi_potential,
    implementation_ease,
    evidence_strength
):

    score = (

        business_impact * 0.30

        + ai_feasibility * 0.20

        + data_availability * 0.15

        + roi_potential * 0.15

        + implementation_ease * 0.10

        + evidence_strength * 0.10
    )

    return round(score, 2)