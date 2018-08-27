from oscar import app

class Shop(app.Shop):
    def get_urls(self):
        urlpatterns = [
            url(r'^cart/', include(self.basket_app.urls)),
            # ...
            # Remianing urls here
        ]
        return urlpatterns

application = Shop()
