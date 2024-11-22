import React from "react";
import ChartCarousel from "../components/Carousel";
import Table from "../components/Table";

function Stats() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-4 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Mantenimiento
          </h2>
          <ChartCarousel
            iframeSrc1="https://tdr-dashboard.onrender.com/failure_frequency"
            iframeSrc2="https://tdr-dashboard.onrender.com/avg_repair_frecuency"
            iframeSrc3="https://tdr-dashboard.onrender.com/monthly_repair_distribution"
            iframeSrc4="https://tdr-dashboard.onrender.com/mtbf"
          />
          <Table />
        </div>
      </div>
    </div>
  );
}

export default Stats;
