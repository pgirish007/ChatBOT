import React, { useState, useEffect } from "react";
import VulnerabilitySummary from "./components/VulnerabilitySummary";
import VulnerabilityList from "./components/VulnerabilityList";
import VulnerabilityDetails from "./components/VulnerabilityDetails";
import Notifications from "./components/Notifications";
import VulnerabilityChart from "./components/VulnerabilityChart";

function App() {
  const [vulnerabilities, setVulnerabilities] = useState([]);
  const [selectedVulnerability, setSelectedVulnerability] = useState(null);
  const [filteredVulnerabilities, setFilteredVulnerabilities] = useState([]);
  const [severityFilter, setSeverityFilter] = useState("");

  useEffect(() => {
    // Fetch the vulnerability data from the REST API
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5000/vulnerabilities");
        const data = await response.json();
        setVulnerabilities(data);
        setFilteredVulnerabilities(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    // Apply severity filter
    if (severityFilter === "") {
      setFilteredVulnerabilities(vulnerabilities);
    } else {
      setFilteredVulnerabilities(
        vulnerabilities.filter((vuln) => vuln.severity === severityFilter)
      );
    }
  }, [severityFilter, vulnerabilities]);

  return (
    <div className="App">
      <Notifications data={vulnerabilities} />
      <VulnerabilitySummary data={vulnerabilities} />

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
        <VulnerabilityChart data={vulnerabilities} />
      </div>

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
