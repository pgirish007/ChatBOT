import React from 'react';
import { registerComponent } from '../registry';

interface TextAreaProps {
  label?: string;
  rows?: number;
  value?: string;
}

const TextArea: React.FC<TextAreaProps> = ({ label, rows = 4, value }) => (
  <div>
    {label && <label>{label}</label>}
    <textarea rows={rows} defaultValue={value}></textarea>
  </div>
);

const generateTextArea = (data: any) => <TextArea key={data.id} {...data} />;

registerComponent('TEXTAREA', generateTextArea);

export default TextArea;
