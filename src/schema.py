import pandera as pa
from pandera import Column, DataFrameSchema, Check

MarketingSchema = DataFrameSchema(
    {
        "ID": Column(int, Check.greater_than_or_equal_to(0)),
        "Year_Birth": Column(int, Check.between(1900, 2005)),
        "Education": Column(
            pa.String,
            Check.isin(
                ["Graduation", "PhD", "Master", "Basic", "2n Cycle"]
            ),
        ),
        "Income": Column(float, nullable=True),
        # ... add the rest incrementally
    },
    strict=False,  # allow extra columns until we define them all
)

if __name__ == "__main__":
    import pandas as pd, pathlib, sys

    path = pathlib.Path(__file__).resolve().parents[1] / "data/raw/marketing_campaign.csv"
    df = pd.read_csv(path, sep=";")
    try:
        MarketingSchema.validate(df, lazy=True)
        print("✅  All checks passed")
    except pa.errors.SchemaErrors as err:
        print("❌  Schema errors:\n", err.failure_cases.head())
        sys.exit(1)
