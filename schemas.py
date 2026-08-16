from pydantic import BaseModel, Field
from typing import List


class Evidence(BaseModel):
    title: str
    source: str
    url: str
    claim_supported: str
    confidence: float = Field(ge=0, le=1)


class AIOpportunity(BaseModel):
    name: str

    ai_capabilities: List[str]

    benefits: List[str]

    risks: List[str]

    business_impact: float = Field(ge=0, le=100)
    ai_feasibility: float = Field(ge=0, le=100)
    data_availability: float = Field(ge=0, le=100)
    roi_potential: float = Field(ge=0, le=100)
    implementation_ease: float = Field(ge=0, le=100)

    priority_score: float = 0

    evidence: List[Evidence] = []


class Process(BaseModel):
    name: str

    business_problems: List[str]

    ai_opportunities: List[AIOpportunity]


class ValueChainStage(BaseModel):
    name: str

    description: str

    processes: List[Process]


class ValueChainAnalysis(BaseModel):
    industry: str

    stages: List[ValueChainStage]