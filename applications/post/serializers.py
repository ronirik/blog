from Blog.applications.post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'image', 'post')


    def create(self, validated_data):
        requests = self.context.get('requests')
        validated_data['author_id'] = request.user.id
        post = Post.objects.create(**validated_data)
        return post

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.email
        rep['comment'] = PostSerializer(Post.objects.filter(post=instance.id),
                                                                  many=True).data
        return rep