from localflavor.us.us_states import STATES_NORMALIZED
from blog.models import Post, Tag, Ad


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def post_tags(request):
    return {
        'post_tags': Tag.objects.all()
    }


def ad(request):
    state = request.location['region'].lower()
    location = STATES_NORMALIZED[state]
    random_ad = Ad.objects.filter(state=location).order_by('?')[0]
    return {
        'ad': random_ad
        # 'ad': Ad.objects.filter(id=3)
    }