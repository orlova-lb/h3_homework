"""Добавьте сущность Review.
Review имеет текст, автора (Customer), оценку от 1 до 5, статус (по умолчанию, "Moderation").
Customer может создать Review.
Admin может одобрить Review (статус меняется на "Published").
"""

import uuid
from customer import Customer


class Review:
    def __init__(self, header, text, marker, customer, status='Moderation'):
        self._id = uuid.uuid4()
        self._header = header
        self._text = text
        self._marker = marker
        self._customer = customer
        self._status = status

    def __str__(self):
        return f"{self._header} ( {self._marker} ) - {self._status}"

    def __repr__(self):
        return f"{self._id} : {self._header} ( {self._marker} ) - {self._status}"

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def mark(self):
        return self._marker

    @mark.setter
    def mark(self, value):
        if value < 1:
            self._marker = 1
        elif value > 5:
            self._marker = 5
        else:
            self._marker = value

    @property
    def customer(self):
        return self._customer

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


