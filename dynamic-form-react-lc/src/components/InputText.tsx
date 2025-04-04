import React from 'react';
import { registerComponent } from '../registry';

interface InputTextProps {
  label?: string;
  placeholder?: string;
  value?: string;
}

const InputText: React.FC<InputTextProps> = ({ label, placeholder, value }) => (
  <div>
    {label && <label>{label}</label>}
    <input type="text" placeholder={placeholder || ''} defaultValue={value || ''} />
  </div>
);

const generateInputText = (data: any) => <InputText key={data.id} {...data} />;

registerComponent('INPUT_TEXT', generateInputText);

export default InputText;
