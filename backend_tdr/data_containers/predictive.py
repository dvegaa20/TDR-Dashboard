from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)


def predictive_model(tdr_df):
    ## Feature Engineering
    # Kilometraje acumulado
    tdr_df["OpenedDate"] = pd.to_datetime(tdr_df["OpenedDate"])
    tdr_df = tdr_df.sort_values(by=["UnitNumber", "OpenedDate"])

    tdr_df["AccumulatedKilometers"] = tdr_df.groupby("UnitNumber")[
        "Kilometers"
    ].cumsum()

    # Días desde el último mantenimiento
    tdr_df["DaysSinceLastRepair"] = (
        tdr_df.groupby("UnitNumber")["OpenedDate"].diff().dt.days
    )
    tdr_df["DaysSinceLastRepair"] = tdr_df["DaysSinceLastRepair"].fillna(0)

    # Frecuencia anual y mensual de mantenimiento
    tdr_df["Year"] = tdr_df["OpenedDate"].dt.year
    tdr_df["Month"] = tdr_df["OpenedDate"].dt.month

    tdr_df["AnualMaintenanceFrequency"] = tdr_df.groupby(["UnitNumber", "Year"])[
        "OrderID"
    ].transform("count")
    tdr_df["MonthlyMaintenanceFrequency"] = tdr_df.groupby(
        ["UnitNumber", "Year", "Month"]
    )["OrderID"].transform("count")

    # Promedio costo por componente
    tdr_df["AvgComponentCost"] = tdr_df.groupby("ComponentCode")["UnitCost"].transform(
        "mean"
    )

    ## Model
    # Objective feature
    tdr_df["ClosedDate"] = pd.to_datetime(tdr_df["ClosedDate"])

    df_sorted = tdr_df.sort_values(by=["PartNumber", "ClosedDate"]).copy()

    df_sorted["DaysBetweenChanges"] = (
        df_sorted.groupby("PartNumber")["ClosedDate"].diff().dt.days
    )

    avg_days_between_changes = (
        df_sorted.groupby("PartNumber")["DaysBetweenChanges"].mean().reset_index()
    )
    avg_days_between_changes.columns = ["PartNumber", "AvgDaysTilChange"]

    tdr_df = tdr_df.merge(avg_days_between_changes, on="PartNumber", how="left")

    tdr_df["DaysTilNextChange"] = (
        tdr_df["AvgDaysTilChange"] - tdr_df["DaysSinceLastRepair"]
    )

    # Maintenance Conditions
    conditions = [
        tdr_df["DaysTilNextChange"] < 0,
        tdr_df["DaysTilNextChange"].between(0, 10),
        tdr_df["DaysTilNextChange"] > 10,
    ]

    choices = ["Vencido", "A tiempo", "Corriente"]
    tdr_df["MaintenanceState"] = np.select(conditions, choices, default="No definido")

    tdr_df = tdr_df[tdr_df["MaintenanceState"] != "No definido"]

    # Train-test split
    X = tdr_df[
        [
            "AccumulatedKilometers",
            "DaysSinceLastRepair",
            "AnualMaintenanceFrequency",
            "MonthlyMaintenanceFrequency",
            "AvgComponentCost",
        ]
    ]
    y = tdr_df["MaintenanceState"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred_rf = rf_model.predict(X_test)

    print("\nRandom Forest:")
    print("Accuracy:", accuracy_score(y_test, y_pred_rf))
    print("Precision:", precision_score(y_test, y_pred_rf, average="weighted"))
    print("Recall:", recall_score(y_test, y_pred_rf, average="weighted"))
    print("F1 Score:", f1_score(y_test, y_pred_rf, average="weighted"))
    print(
        "ROC AUC:",
        roc_auc_score(y_test, rf_model.predict_proba(X_test), multi_class="ovr"),
    )
    print(confusion_matrix(y_test, y_pred_rf))
    print(classification_report(y_test, y_pred_rf))


# data = pd.read_csv("tdrV2.csv")
# predictive_model(data)
