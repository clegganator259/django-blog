from django.db import models
from django.utils import timezone
import markdown2
from pyquery import PyQuery as pq
from django.core.validators import RegexValidator
from django_extensions.db.fields import AutoSlugField
import re

valid_title_chars = r'^[a-zA-Z ,!?]+$'
title_validator = RegexValidator(valid_title_chars)

# The length of the summary -3 represents the space for the elipses
CONST_SUMMARY_LENGTH = 200 - 3 

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(
            unique=True,
            max_length=200
        )
    text = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True,
            null=True)
    slug = AutoSlugField( max_length=50,null=False,unique=True, populate_from=('title','author'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Creates a summary of CONST_SUMMARY_LENGTH and no more
    # TODO box filling with words so words aren't broken
    def summary(self):
        html_text = markdown2.markdown(self.text) 
        ## Gets the paragraphs for 
        body_text = pq(html_text)('p').text()
        if len(body_text) < CONST_SUMMARY_LENGTH:
            return body_text
        else:
            #Returns the first CONST_SUMMARY_LENGTH
            #characters of the body + elipses
            return body_text[:CONST_SUMMARY_LENGTH]+'...'


    def __str__(self):
        return self.title
