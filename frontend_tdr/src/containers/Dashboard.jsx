import React from "react";
import GraphContainer from "../components/DashboardGraphContainer";

function Dashboard() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          {/* First grid with 2.5fr and 1.5fr columns */}
          <div
            className="grid"
            style={{ gridTemplateColumns: "2.5fr 1.5fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Estadísticas Generales"
              linkTo="/stats"
              iframeSrc="https://tdr-dashboard.onrender.com/dash_monthly_repair_distribution"
            />
            <GraphContainer
              title="Estado de los Tractos"
              linkTo="/tractos"
              iframeSrc="https://tdr-dashboard.onrender.com/dash_tractos_failure_distribution"
            />
          </div>

          {/* Second grid with 2.5fr and 1.5fr columns */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "1.5fr 2.5fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Resumen de Gastos"
              linkTo="/gastos"
              iframeSrc="https://tdr-dashboard.onrender.com/dash_cost_distribution"
            />
            <GraphContainer
              title="Actividades de Mantenimiento"
              linkTo="/mantenimientos"
              iframeSrc="https://tdr-dashboard.onrender.com/dash_part_number"
            />
          </div>

          {/* Third grid with 1.5fr 2.5fr column */}
          {/* <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "1fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Análisis Predictivo"
              linkTo="/predictive"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
          </div> */}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
