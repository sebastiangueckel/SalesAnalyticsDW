import pandas as pd
import locale

locale.setlocale(locale.LC_TIME, "de_DE")

dates = pd.date_range(
    start="2020-01-01",
    end="2026-12-31",
    freq="D"
)

date_dim = pd.DataFrame({
    "date": dates
})

date_dim["date_key"] = (
    date_dim["date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)
date_dim["year"] = date_dim["date"].dt.year
date_dim["quarter"] = date_dim["date"].dt.quarter
date_dim["month"] = date_dim["date"].dt.month
date_dim["month_name"] = date_dim["date"].dt.month_name(locale="de_DE")
date_dim["week"] = date_dim["date"].dt.isocalendar().week
date_dim["weekday"] = date_dim["date"].dt.day_name(locale="de_DE")
date_dim["is_weekend"] = date_dim["date"].dt.weekday >= 5



