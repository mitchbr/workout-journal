from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from workouts.models import Workout, WorkoutType

@require_http_methods(["GET"])
def dump_db(request):
  workouts = Workout.objects.all()
  workouts_json_data = json.loads(serializers.serialize("json", workouts))
  workout_types = WorkoutType.objects.all()
  workout_types_json_data = json.loads(serializers.serialize("json", workout_types))
  json_data = {'workouts': workouts_json_data, 'workout_types': workout_types_json_data}
  data = {'message': 'Request successful', 'status': 'ok', 'data': json_data}

  return JsonResponse(data)
