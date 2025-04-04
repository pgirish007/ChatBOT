import { JSX } from "react";

const componentRegistry = new Map<string, (data: any) => JSX.Element>();

export const registerComponent = (type: string, generateFn: (data: any) => JSX.Element) => {
    componentRegistry.set(type, generateFn);
};

export const generateComponent = (type: string, data: any) => {
    const generateFn = componentRegistry.get(type);
    if (!generateFn) {
        console.warn(`No component registered for type: ${type}`);
        return null;
    }
    return generateFn(data);
};