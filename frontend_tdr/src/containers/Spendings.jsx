import React from "react";
import ChartCarousel from "../components/Carousel";
import Table from "../components/Table";

function Spendings() {
  return (
    <div>
      <div className="p-2 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Resumen de Costos
          </h2>
          <ChartCarousel
            iframeSrcs={[
              "https://tdr-dashboard.onrender.com/maintenance_costs",
              "https://tdr-dashboard.onrender.com/cost_distribution",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Spendings;
