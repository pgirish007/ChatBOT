import React from 'react';
import { registerComponent } from '../registry';

interface InputNumberProps {
  label?: string;
  min?: number;
  max?: number;
  value?: number;
}

const InputNumber: React.FC<InputNumberProps> = ({ label, min, max, value }) => (
  <div>
    {label && <label>{label}</label>}
    <input type="number" min={min} max={max} defaultValue={value} />
  </div>
);

const generateInputNumber = (data: any) => <InputNumber key={data.id} {...data} />;

registerComponent('INPUT_NUMBER', generateInputNumber);

export default InputNumber;
