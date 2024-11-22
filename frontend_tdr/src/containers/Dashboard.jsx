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
              title="Estadísticas de Mantenimiento"
              linkText="See all"
              linkTo="/stats"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
            <GraphContainer
              title="Estado de los Tractos"
              linkText="See all"
              linkTo="/tractos"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
          </div>

          {/* Second grid with 2.5fr and 1.5fr columns */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "2.5fr 1.5fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Actividades de Mantenimiento"
              linkText="See all"
              linkTo="/mantenimientos"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
            <GraphContainer
              title="Resumen de Gastos"
              linkText="See all"
              linkTo="/gastos"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
          </div>

          {/* Third grid with 1.5fr 2.5fr column */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "1.5fr 2.5fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Actividades de Mantenimiento"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
            <GraphContainer
              title="Resumen de Gastos"
              iframeSrc="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
