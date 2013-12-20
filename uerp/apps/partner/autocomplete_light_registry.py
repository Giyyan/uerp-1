import autocomplete_light
from uerp.apps.partner.models import Partner

autocomplete_light.register(Partner,
    # Just like in ModelAdmin.search_fields
    search_fields=['^name', 'ur_name'],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    autocomplete_js_attributes={'placeholder': 'Партнер',},
)