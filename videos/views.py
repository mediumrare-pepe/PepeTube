from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Video


@login_required
@require_POST
def upload_video(request):
    video = Video.objects.create(
        title=request.POST.get("title", ""),
        description=request.POST.get("description", ""),
        video_file=request.FILES["video_file"],
        thumbnail=request.FILES.get("thumbnail"),
        uploaded_by=request.user,
    )
    return JsonResponse({"id": video.id, "title": video.title})
