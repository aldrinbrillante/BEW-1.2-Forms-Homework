from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from wtforms.fields.core import FloatField
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Grocery Store Title', validators=[DataRequired()])
    address = StringField('Grocery Store Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    # TODO: Add the following fields to the form class:

# - name - StringField
    name = StringField('Name', validators=[DataRequired()])
# - price - FloatField
    price = FloatField('Price', validators=[DataRequired()])
# - category - SelectField (specify the 'choices' param)
    category = SelectField('Category', validators=[DataRequired()], choices=ItemCategory.choices())
# - photo_url - StringField
    photo_url = StringField('Photo', validators=[URL()])
# - store - QuerySelectField (specify the `query_factory` param)
    store = QuerySelectField('Grocery Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
# - submit button
    submit = SubmitField('Submit')
