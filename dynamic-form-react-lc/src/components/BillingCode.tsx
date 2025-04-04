// components/BillingCode.tsx
import React from 'react';
import { registerComponent } from '../registry';

interface BillingCodeProps {
    businessLabel?: string;
    name: string;
    fieldId: string;
    dependson?: string[];
}

const BillingCode: React.FC<BillingCodeProps> = ({ businessLabel, name, fieldId }) => (
    <div>
        {businessLabel && <label htmlFor={fieldId}>{businessLabel}</label>}
        <input type="text" id={fieldId} name={name} placeholder="Enter billing code" />
    </div>
);

const generateBillingCode = (data: any) => <BillingCode key={data.fieldId} {...data} />;

registerComponent('BILLING_CODE', generateBillingCode);

export default BillingCode;
