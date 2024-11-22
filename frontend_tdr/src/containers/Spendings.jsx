import React from "react"
import ChartCarousel from "../components/Carousel"
import Table from "../components/Table"

function Spendings() {
  return (
    <div>
      <div className="p-4 sm:ml-64">
        <div className="p-2 rounded-lg dark:border-gray-700">
          <h2 className="text-customBlue text-lg font-semibold mb-4">
            Estadísticas de Costos
          </h2>
          <ChartCarousel iframeSrc1="http://localhost:8050/calculate_maintenance_costs" />
          <Table />
        </div>
      </div>
    </div>
  )
}

export default Spendings
