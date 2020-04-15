from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status

from core.models import Collection, Figure


def sample_user():
    user = get_user_model().objects.create(
        name='test name',
        email='test@email.com'
    )
    return user


def create_collection(name, user):
    return Collection.objects.create(name=name, user=user)


def create_figure(name, user):
    return Figure.objects.create(name=name, user=user)


class CollectionDetailViewTests(TestCase):
    def test_no_figures(self):
        """
        If no figures exist, appropriate message is displayed.
        """
        collection = create_collection(
            'test collection',
            sample_user())

        response = self.client.get(
            reverse('collection:detail', args=(collection.pk,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['collection'].figures.all(),
            [])
        self.assertContains(
            response,
            'There are no figures in this collection.')

    def test_collection(self):
        """
        The detail view displays all figures in that collection.
        """
        user = sample_user()

        collection = create_collection(
            'test collection',
            user
        )

        figure1 = create_figure('testfig1', user)
        figure2 = create_figure('testfig2', user)
        collection.figures.add(figure1, figure2)

        response = self.client.get(reverse(
            'collection:detail',
            args=(collection.pk,)
        ))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context['figure_list'].count(), 2)
        self.assertContains(response, figure1)
        self.assertContains(response, figure2)
