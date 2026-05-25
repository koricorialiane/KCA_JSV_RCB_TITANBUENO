import pandas as pd

from .cellular_planning import district_capacity_table, district_coverage_table
from .config import DistrictScenario, NetworkConfig


def analyze_financial_district(
    scenario: DistrictScenario = DistrictScenario(),
    config: NetworkConfig = NetworkConfig(),
) -> dict[str, pd.DataFrame]:
    coverage = district_coverage_table(scenario, config)
    capacity = district_capacity_table(coverage, scenario, config)
    return {"coverage": coverage, "capacity": capacity}
