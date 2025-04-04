import React, { useState } from 'react';
import DynamicFormGenerator from './DynamicFormGenerator';

// Import component definitions to register them into the registry
import './components/InputText';
import './components/InputNumber';
import './components/TextArea';
import './components/Select';
import './components/BillingCode';

const initialJson = {
  moduleName: "NG-LINUX-VIRTUAL-D-V1.4",
  moduleDescription: "Linux",
  name: "Linux",
  jsonVersion: "1.0.0",
  lowcodeVersion: "2.0",
  apiName: "itid-pa-hic-os",
  apiSignature: "/buildLinuxServers",
  apiMethodType: "POST",
  roleName: "itid-hic_build_os_role,itid-hic_demise_os_role",
  collection: {
    "how To": [
      {
        titleName: "How To Setup Entitlements",
        link: "https://alm-confluence.systems.uk.hsbc/confluence/pages/viewpage.action?pageId=1011665782"
      }
    ],
    type: "TABBED",
    elements: {
      "Business Information": [
        {
          businessLabel: "Service",
          fieldRequired: true,
          readonly: true,
          inputType: "SELECT",
          name: "service",
          fieldId: "service",
          portalProvidedDataAttribute: "services",
          onChangeAction: "retrieve DataMapping",
          onChangeActionInputs: ["environmentClass", "UnicornSearch"]
        },
        {
          businessLabel: "Region",
          fieldRequired: true,
          inputType: "SELECT",
          name: "region",
          fieldId: "region",
          patternProvidedDataAttribute: "region"
        },
        {
          businessLabel: "Billing Code",
          fieldRequired: true,
          inputType: "BILLING_CODE",
          name: "billingCode",
          fieldId: "billingCode",
          dependson: ["region"]
        }
      ]
    }
  }
};

const App: React.FC = () => {
  const [jsonInput, setJsonInput] = useState<string>(JSON.stringify(initialJson, null, 2));
  const [formConfig, setFormConfig] = useState<any>(initialJson.collection.elements);
  const [error, setError] = useState<string | null>(null);

  const handleJsonChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const text = e.target.value;
    setJsonInput(text);
    try {
      const parsed = JSON.parse(text);
      if (parsed.collection?.elements) {
        setFormConfig(parsed.collection.elements);
        setError(null);
      } else {
        setError("Missing 'collection.elements' in JSON.");
      }
    } catch (err) {
      setError("Invalid JSON format.");
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Dynamic Form Generator</h1>
      <p>Paste your JSON below to dynamically generate a form.</p>
      <textarea
        rows={12}
        style={{ width: '100%', fontFamily: 'monospace' }}
        value={jsonInput}
        onChange={handleJsonChange}
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <DynamicFormGenerator formConfig={formConfig} />
    </div>
  );
};

export default App;
