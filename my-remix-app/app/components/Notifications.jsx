import React from "react";

function Notifications({ data }) {
  const criticalAlerts = data.filter((vuln) => vuln.severity === "Critical");

  return (
    <div className="notifications">
      <h2>Notifications</h2>
      {criticalAlerts.length > 0 ? (
        <p><strong>Alert:</strong> {criticalAlerts.length} Critical Vulnerabilities Found!</p>
      ) : (
        <p>No critical vulnerabilities.</p>
      )}
    </div>
  );
}

export default Notifications;
