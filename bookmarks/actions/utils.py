import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType 
from .models import Action



def create_action(user, verb, target=None):
	# check for any similar action made in the last minute
	now = timezone.now()
	last_minute = now - datetime.timedelta(seconds=60)
	similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created__gte=last_minute)
	# don't use below line, instead you should use above line.
	# similar_actions = Action.objects.filter(user_id=user.id, verb=verb, timestamp__gte=last_minute)
	if target:
		target_ct = ContentType.objects.get_for_model(target)
		similar_actions = Action.objects.filter(target_ct=target_ct, target_id=target.id)
	if not similar_actions:
		# no existing actions found
		action = Action(user=user, verb=verb, target=target)
		action.save()
		return True
	return False