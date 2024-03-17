from pyramid_html.views.default import home, about
from pyramid_html.views.notfound import notfound_view


def test_home(app_request):
    info = home(app_request)
    assert app_request.response.status_int == 200
    assert info['project'] == 'pyramid-html'


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}


def test_about(app_request):
    info = about(app_request)
    assert app_request.response.status_int == 200
    assert info['message'] == 'About pyramid.'