import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import React from "react";
import Notifications from "../components/Notifications";
import VulnerabilitySummary from "../components/VulnerabilitySummary";
import VulnerabilityList from "../components/VulnerabilityList";
import VulnerabilityDetails from "../components/VulnerabilityDetails";
import VulnerabilityChart from "../components/VulnerabilityChart";
import CustomDataGrid from "../components/datagrid";

// Define the types for our loader data
interface Vulnerability {
  id: string;
  severity: string;
  description: string;
}

type LoaderData = {
  vulnerabilities: Vulnerability[];
};

// Loader function to fetch data
export const loader = async () => {
  const res = await fetch("http://localhost:5001/vulnerabilities");
  const vulnerabilities = await res.json();
  return json<LoaderData>({ vulnerabilities });
};

export default function Index() {
  // Use the LoaderData type with useLoaderData
  const { vulnerabilities } = useLoaderData<LoaderData>();
  const [selectedVulnerability, setSelectedVulnerability] = React.useState<Vulnerability | null>(null);
  const [severityFilter, setSeverityFilter] = React.useState<string>("");

  const filteredVulnerabilities = severityFilter
    ? vulnerabilities.filter((vuln) => vuln.severity === severityFilter)
    : vulnerabilities;

  return (
    <div className="dashboard">
      <Notifications data={vulnerabilities} />
      <CustomDataGrid/>
      <VulnerabilitySummary data={vulnerabilities} />
      <VulnerabilityChart data={vulnerabilities} />

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
