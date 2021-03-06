from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'main_categories'

class SubCategory(models.Model):
    name     = models.CharField(max_length=50)
    main_sub = models.ManyToManyField(MainCategory, through='Story')

    class Meta:
        db_table = 'sub_categories'

class Story(models.Model):
    main_category   = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category    = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    content         = models.TextField()
    description     = models.TextField()
    related_stories = models.ManyToManyField('self', through='RelatedStory', symmetrical=False)

    class Meta:
        db_table = 'stories'

class StoryImage(models.Model):
    story     = models.ForeignKey(Story, on_delete=models.CASCADE)
    image_url = models.URLField()

    class Meta:
        db_table = 'story_images'

class RelatedStory(models.Model):
    from_story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='to_story')
    to_story   = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='from_story')

    class Meta:
        db_table = 'related_stories'