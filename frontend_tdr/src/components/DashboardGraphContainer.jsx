import React from "react"
import { Link } from "react-router-dom"

const DashboardGraphContainer = ({ title, linkText, linkTo, iframeSrc }) => {
  return (
    <div className="flex flex-col">
      <div className="flex justify-between items-center mb-2">
        <h2 className="text-customBlue text-lg font-semibold">{title}</h2>
        {linkTo && (
          <Link to={linkTo}>
            <p className="text-sm text-customBlue cursor-pointer hover:text-blue-900 hover:underline hover:decoration-dashed">
              {linkText}
            </p>
          </Link>
        )}
      </div>
      <div className="flex flex-col items-center justify-center h-auto p-4 bg-gray-50 dark:bg-gray-800 rounded-lg">
        <iframe
          src={iframeSrc}
          style={{
            border: "none",
            height: "100%",
            width: "100%",
            borderRadius: "10px",
          }}
        ></iframe>
      </div>
    </div>
  )
}

export default DashboardGraphContainer
