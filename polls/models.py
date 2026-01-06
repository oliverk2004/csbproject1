from django.db import models

# A Question has a question and a publication date.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


# A Choice has two fields: the text of the choice and a vote tally.
# Each Choice is associated with a Question.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey tells Django each Choice is related to a single Question.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)