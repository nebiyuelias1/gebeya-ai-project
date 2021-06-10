import requests
from django.conf import settings

from views.models import View, ViewReview, Term


def review_view(view: View):
    api_url = settings.AZ_CONTENT_MODERATOR_URL
    headers = {'Ocp-Apim-Subscription-Key': settings.AZ_SUBSCRIPTION_KEY,
               'Content-Type': 'text/plain'}

    response = requests.post(
        api_url,
        'Is this a crap email abcdef@abcd.com, phone: 6657789887, IP: 255.255.255.255, 1 Microsoft Way, Redmond, WA 98052',
        headers=headers
    )

    # If the request is successful.
    if response.status_code == requests.status_codes.codes.OK:
        json_response = response.json()
        if json_response['Classification']['ReviewRecommended']:
            view.flagged = True
            view.save()

            view_review = ViewReview.objects.create(view=view,
                                                    category_one_score=json_response['Classification']['Category1'][
                                                        'Score'],
                                                    category_two_score=json_response['Classification']['Category2'][
                                                        'Score'],
                                                    category_three_score=json_response['Classification']['Category3'][
                                                        'Score'])

            if json_response['Terms']:
                terms = json_response['Terms']
                term_objects = []
                for term in terms:
                    term_objects.append(Term(term=term['Term'], view_review=view_review))

                Term.objects.bulk_create(term_objects)
