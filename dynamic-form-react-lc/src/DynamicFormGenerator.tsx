import React from 'react';
import { generateComponent } from './registry';

interface DynamicFormGeneratorProps {
    formConfig: Record<string, any[]>;
}

const DynamicFormGenerator: React.FC<DynamicFormGeneratorProps> = ({ formConfig }) => {
    return (
        <div>
            {Object.entries(formConfig).map(([section, fields]) => (
                <fieldset key={section} style={{ marginBottom: '20px' }}>
                    <legend>{section}</legend>
                    {fields.map((field) => generateComponent(field.inputType, field))}
                </fieldset>
            ))}
        </div>
    );
};

export default DynamicFormGenerator;