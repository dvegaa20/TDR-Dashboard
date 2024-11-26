import React from "react";
import ChartCarousel from "../components/Carousel";
import Table from "../components/Table";

function Stats() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas Generales
          </h2>
          <ChartCarousel
            iframeSrcs={[
              "http://127.0.0.1:8050/monthly_repair_distribution",
              "http://127.0.0.1:8050/failure_frequency",
              "http://127.0.0.1:8050/avg_repair_frecuency",
            ]}
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Stats;
