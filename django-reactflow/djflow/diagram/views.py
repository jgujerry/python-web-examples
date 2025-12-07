import json
from django.shortcuts import render
from django.views import View

class DiagramView(View):
    def get(self, request):
        default_nodes = [
            {"id": "1", "data": {"label": "Node 1"}, "position": {"x": 0, "y": 0}},
            {"id": "2", "data": {"label": "Node 2"}, "position": {"x": 250, "y": 0}},
            {"id": "3", "data": {"label": "Node 3"}, "position": {"x": 500, "y": 0}},
            {"id": "4", "data": {"label": "Node 4"}, "position": {"x": 125, "y": 150}},
            {"id": "5", "data": {"label": "Node 5"}, "position": {"x": 375, "y": 150}},
        ]
        
        default_edges = [
            {"id": "e1-2", "source": "1", "target": "2"},
            {"id": "e2-3", "source": "2", "target": "3"},
            {"id": "e1-4", "source": "1", "target": "4"},
            {"id": "e2-5", "source": "2", "target": "5"},
            {"id": "e4-5", "source": "4", "target": "5"},
        ]
        
        context = {
            'nodes_json': json.dumps(default_nodes),
            'edges_json': json.dumps(default_edges),
        }
        return render(request, 'diagram.html', context)
