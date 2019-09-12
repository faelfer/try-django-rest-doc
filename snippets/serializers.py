from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetsSerializer(serializers.Serializer):
	id = serializers.integerField(read_only=True)
	title = serializers.CharField(required=False, max_length=100, allow_blank=True)
	code = serializers.TextField(style={'base_template': 'textarea.html'})
	linenos = serializers.BooleanField(required=False)
	language = serializers.CharField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.CharField(choices=STYLE_CHOICES, default='friendly')

	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return	Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.code = validated_data.get('code', instance.code)
		instance.linenos= validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('language', instance.style)
		instance.save()
		return instance
