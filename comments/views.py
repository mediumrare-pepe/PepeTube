import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Comment
from videos.models import Video


@require_http_methods(["POST"])
def post_comment(request):
    try:
        data = json.loads(request.body)
        video_id = data["video"]
        content = data["content"]
    except (KeyError, json.JSONDecodeError):
        return HttpResponseBadRequest("Invalid data")
    video = get_object_or_404(Video, id=video_id)
    user = request.user if request.user.is_authenticated else None
    comment = Comment.objects.create(video=video, user=user, content=content)
    return JsonResponse({"id": comment.id, "video": comment.video.id, "user": comment.user.id if comment.user else None, "content": comment.content})


@require_http_methods(["GET"])
def list_comments(request):
    video_id = request.GET.get("video")
    if not video_id:
        return HttpResponseBadRequest("Video parameter required")
    comments = Comment.objects.filter(video_id=video_id).select_related("user").order_by("created_at")
    data = [
        {
            "id": c.id,
            "user": c.user.id if c.user else None,
            "content": c.content,
            "created_at": c.created_at.isoformat(),
        }
        for c in comments
    ]
    return JsonResponse(data, safe=False)


@require_http_methods(["DELETE"])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({"status": "deleted"})
