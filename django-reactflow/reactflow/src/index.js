import React from 'react';
import ReactDOM from 'react-dom/client';
import DiagramFlow from './components/DiagramFlow';

// Function to mount the React app
export function mountApp(containerId, initialData = {}) {
  const container = document.getElementById(containerId);
  if (container) {
    const root = ReactDOM.createRoot(container);
    root.render(<DiagramFlow initialData={initialData} />);
  }
}
