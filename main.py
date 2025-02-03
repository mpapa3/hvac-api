from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HVACLeadCostInput(BaseModel):
    totalMarketingSpend: float
    numberOfLeads: int
    conversionRate: float
    averageRevenuePerSale: float

@app.post("/calculate-hvac-lead-cost")
def calculate_hvac_lead_cost(data: HVACLeadCostInput):
    cost_per_lead = data.totalMarketingSpend / data.numberOfLeads
    total_revenue = (data.numberOfLeads * (data.conversionRate / 100)) * data.averageRevenuePerSale
    roi_percentage = ((total_revenue - data.totalMarketingSpend) / data.totalMarketingSpend) * 100
    break_even_leads = data.totalMarketingSpend / ((data.conversionRate / 100) * data.averageRevenuePerSale)

    return {
        "costPerLead": cost_per_lead,
        "totalRevenue": total_revenue,
        "roiPercentage": roi_percentage,
        "breakEvenLeads": break_even_leads
    }
