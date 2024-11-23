import React from "react";
import ChartCarousel from "../components/Carousel";
import Table from "../components/Table";

function Spendings() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-2 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Costos
          </h2>
          <ChartCarousel
            iframeSrcs={[
              "http://127.0.0.1:8050/maintenance_costs",
              "http://127.0.0.1:8050/cost_distribution",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Spendings;
