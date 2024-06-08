from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
    image_serialized = ImageSerializer(data=request.data)
    if image_serialized.is_valid():
        image_serialized.save()
        return Response(image_serialized.data, status=status.HTTP_201_CREATED)
    return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
    images = Image.objects.all()
    images_serialized = ImageSerializer(images, many=True)
    return Response(images_serialized.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_image(request, pk):
    print("REQUEST: ", request)
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response({"error": "Image not found."}, status=status.HTTP_404_NOT_FOUND)

    image_serialized = ImageSerializer(image, data=request.data)
    print("IMAGE SERIALIZER: ", ImageSerializer)
    if image_serialized.is_valid():
        updated_image = image_serialized.save()
        return Response({"message": "Image updated successfully.", "data": ImageSerializer(imageId).data})
        print("IMAGE SERIALIZER IMAGEID DATA: ", ImageSerializer(imageid).data)
    return Response({"error": "Invalid data provided.", "details": image_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_image(request, pk):
#     print("REQUEST, PK: ", request, pk)
#     try:
#         image = Image.objects.get(pk=pk)
#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except Image.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_posts(request):
#     posts = Post.objects.all()
#     posts_serialized = PostSerializer(posts, many=True)
#     return Response(posts_serialized.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_post(request):
#     post_serialized = PostSerializer(data=request.data)
#     if post_serialized.is_valid():
#         post_serialized.save()
#         return Response(post_serialized.data, status=status.HTTP_201_CREATED)
#     return Response(post_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_likes(request):
#     likes = Like.objects.all()
#     likes_serialized = LikeSerializer(likes, many=True)
#     return Response(likes_serialized.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_like(request):
#     like_serialized = LikeSerializer(data=request.data)
#     if like_serialized.is_valid():
#         like_serialized.save()
#         return Response(like_serialized.data, status=status.HTTP_201_CREATED)
#     return Response(like_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_comments(request):
#     comments = Comment.objects.all()
#     comments_serialized = CommentSerializer(comments, many=True)
#     return Response(comments_serialized.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_comment(request):
#     comment_serialized = CommentSerializer(data=request.data)
#     if comment_serialized.is_valid():
#         comment_serialized.save()
#         return Response(comment_serialized.data, status=status.HTTP_201_CREATED)
#     return Response(comment_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_shares(request):
#     shares = Share.objects.all()
#     shares_serialized = ShareSerializer(shares, many=True)
#     return Response(shares_serialized.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_share(request):
#     share_serialized = ShareSerializer(data=request.data)
#     if share_serialized.is_valid():
#         share_serialized.save()
#         return Response(share_serialized.data, status=status.HTTP_201_CREATED)
#     return Response(share_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_reposts(request):
#     reposts = Repost.objects.all()
#     reposts_serialized = RepostSerializer(reposts, many=True)
#     return Response(reposts_serialized.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_repost(request):
#     repost_serialized = RepostSerializer(data=request.data)
#     if repost_serialized.is_valid():
#         repost_serialized.save()
#         return Response(repost_serialized.data, status=status.HTTP_201_CREATED)
#     return Response(repost_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    # print('CREATE USER ', request.data)
    username = request.data['username']
    user = User.objects.create(
        username = username
    )
    user.set_password(request.data['password'])
    user.save()
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    profile = Profile.objects.create(
        user = user,
        first_name = first_name,
        last_name = last_name
    )
    user_serialized = UserSerializer(user)
    # if user_serialized.is_valid():
    #     user_serialized.save()
    # print('CAllabungaaa')
    # return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response(user_serialized.data, status=status.HTTP_201_CREATED)
    return Response(user_serialized.data)

