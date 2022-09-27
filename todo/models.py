from django.db import models

# blank == required on forms
# null == cannot be empty programatically


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # This is how to override the str method from the inherited Model class.
    # This is a great example of the benefits of class based inheritence at play.
    def __str__(self):
        return self.name
