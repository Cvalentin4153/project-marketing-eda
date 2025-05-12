import pandera as pa
from pandera import Column, DataFrameSchema, Check
from datetime import datetime

MarketingSchema = DataFrameSchema(
    {
        "ID": Column(
            pa.Int,
            checks=[
            Check(lambda s: s.is_unique, element_wise=False)
            ],
            coerce=True,
            nullable=False
        ),
        "Year_Birth": Column(
            pa.Int,
            Check.between(1900, 2005),
            coerce=True,
            nullable=False
        ),
        "Education": Column(
            pa.String,
            checks=[
                Check.isin(["Graduation", "PhD", "Master", "Basic", "2n Cycle"])
            ],
            nullable=False
        ),
        "Income": Column(
            pa.Float,
            checks=[
                Check(lambda s: s >= 0, element_wise=True),
                Check(lambda s: s <= 200000, element_wise=True),
            ],
            nullable=True
        ),
        "Dt_Customer": Column(
            pa.DateTime,
            coerce=True,
            checks=[
                Check.between("2012-08-14", "2014-06-29")
            ],
            nullable=False
        ),
        "Recency": Column(
            pa.Int,
            checks=[
                Check(lambda s: s >= 0, element_wise=True),
                Check(lambda s: s <= 800, element_wise=True)
            ],
            nullable=False
        ),
        "Kidhome": Column(
            pa.Int,
            checks=[
                Check(lambda s: s >= 0, element_wise=True),
                Check(lambda s: s <= 10, element_wise=True),
            ],
            nullable=False
        ),
        "Teenhome": Column(
            pa.Int,
            checks=[
                Check(lambda s: s >= 0, element_wise=True),
                Check(lambda s: s <= 10, element_wise=True),
            ],
            nullable=False
        ),
        "Marital_Status": Column(
            pa.String,
            checks=[
                Check.isin(["Married", "Single", "Widow", "Divorced"])
            ],
            nullable=False
        ),
        "MntWines": Column(pa.Int, Check(lambda s: s >= 0, element_wise=True)),
        "MntFruits": Column(pa.Int, Check(lambda s: s >= 0, element_wise=True)),
        "MntMeatProducts": Column(pa.Int, Check(lambda s: s >= 0, element_wise=True)),
        "MntFishProducts": Column(pa.Int, Check(lambda s: s >= 0, element_wise=True)),
        "MntSweetProducts": Column(pa.Int, Check(lambda s: s >= 0, element_wise=True)),
        "AcceptedCmpOverall": Column(pa.Int, Check.isin([0, 1]), nullable=False),
        "Response": Column(pa.Int, Check.isin([0, 1]), nullable=False),
    },
    checks=[
        Check(
            lambda df: (df["Kidhome"] + df["Teenhome"]) <= 10,
            element_wise=False,
            error="Total children > 10"
        ),
        Check(
            lambda df: df["Dt_Customer"] <= datetime(2014, 6, 29),
            element_wise=True,
            error="Customer date beyond campaign end"
        ),
    ],
    strict=False,  
)

if __name__ == "__main__":
    import pandas as pd, pathlib, sys

    path = pathlib.Path(__file__).resolve().parents[1] / "data/processed/marketing_campaign_clean2.csv"
    df = pd.read_csv(path, sep=",")
    try:
        MarketingSchema.validate(df, lazy=True)
        print("All checks passed")
    except pa.errors.SchemaErrors as err:
        print("Schema errors:\n", err.failure_cases)
        sys.exit(1)
