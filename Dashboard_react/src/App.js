import React, { useState, useEffect } from "react";
import VulnerabilitySummary from "./components/VulnerabilitySummary";
import VulnerabilityList from "./components/VulnerabilityList";
import VulnerabilityDetails from "./components/VulnerabilityDetails";
import Notifications from "./components/Notifications";
import data from "./data/vulnerabilities.json"; // Simulate data

function App() {
  const [selectedVulnerability, setSelectedVulnerability] = useState(null);
  const [filteredVulnerabilities, setFilteredVulnerabilities] = useState([]);
  const [severityFilter, setSeverityFilter] = useState("");

  useEffect(() => {
    // Apply severity filter
    if (severityFilter === "") {
      setFilteredVulnerabilities(data);
    } else {
      setFilteredVulnerabilities(
        data.filter((vuln) => vuln.severity === severityFilter)
      );
    }
  }, [severityFilter]);

  return (
    <div className="App">
      <h1>Vulnerability Dashboard</h1>
      <Notifications data={data} />
      <VulnerabilitySummary data={data} />
      <div style={{ display: "flex" }}>
        <VulnerabilityList
          vulnerabilities={filteredVulnerabilities}
          onSelectVulnerability={setSelectedVulnerability}
          setSeverityFilter={setSeverityFilter}
        />
        {selectedVulnerability && (
          <VulnerabilityDetails vulnerability={selectedVulnerability} />
        )}
      </div>
    </div>
  );
}

export default App;
