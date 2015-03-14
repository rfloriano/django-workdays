#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import ujson as json
except ImportError:
    import json

from django.views.generic import View
from django.http import HttpResponse

from .models import Quarter


class JSONResponseView(View):
    def render_to_response(self, data, **kwargs):
        return HttpResponse(
            json.dumps(data), content_type="application/json", **kwargs
        )


class QuarterGoalsView(JSONResponseView):
    def get(self, *args, **kwargs):
        data = {'quarters': []}
        for quarter in Quarter.get_current_quarters():
            data['quarters'].append(quarter.to_dict())
        return self.render_to_response(data, status=200)
