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
              iframeSrc="http://localhost:8050/iris"
            />
            <GraphContainer
              title="Estado de Refacciones"
              linkText="See all"
              linkTo="/tractos"
              iframeSrc="http://localhost:8050/tractos_age"
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
              iframeSrc="http://localhost:8050/iris"
            />
            <GraphContainer
              title="Resumen de Gastos"
              linkText="See all"
              linkTo="/gastos"
              iframeSrc="http://localhost:8050/cost_distribution"
            />
          </div>

          {/* Third grid with 1.5fr 2.5fr column */}
          <div
            className="grid mt-8"
            style={{ gridTemplateColumns: "1.5fr 2.5fr", gap: "1rem" }}
          >
            <GraphContainer
              title="Actividades de Mantenimiento"
              iframeSrc="http://localhost:8050/iris"
            />
            <GraphContainer
              title="Resumen de Gastos"
              iframeSrc="http://localhost:8050/gapminder"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
