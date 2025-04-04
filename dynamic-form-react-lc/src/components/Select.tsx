// components/Select.tsx
import React from 'react';
import { registerComponent } from '../registry';

interface SelectProps {
    businessLabel?: string;
    name: string;
    fieldId: string;
    portalProvidedDataAttribute?: string;
    options?: string[];
}

const Select: React.FC<SelectProps> = ({ businessLabel, name, fieldId, options = [] }) => (
    <div>
        {businessLabel && <label htmlFor={fieldId}>{businessLabel}</label>}
        <select id={fieldId} name={name}>
            {options.map((option, index) => (
                <option key={index} value={option}>{option}</option>
            ))}
        </select>
    </div>
);

const generateSelect = (data: any) => <Select key={data.fieldId} {...data} />;

registerComponent('SELECT', generateSelect);

export default Select;