import React, { useCallback } from 'react';
import {
  ReactFlow,
  addEdge,
  Background,
  Controls,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

const defaultNodes = [
  {
    id: '1',
    data: { label: 'Node 1' },
    position: { x: 0, y: 0 },
  },
  {
    id: '2',
    data: { label: 'Node 2' },
    position: { x: 250, y: 0 },
  },
];

const defaultEdges = [
  { id: 'e1-2', source: '1', target: '2' },
];

export default function DiagramFlow({ initialData = {} }) {
  const [nodes, setNodes, onNodesChange] = useNodesState(
    initialData.nodes || defaultNodes
  );
  const [edges, setEdges, onEdgesChange] = useEdgesState(
    initialData.edges || defaultEdges
  );

  const onConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100%', height: '100%' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
      >
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}
