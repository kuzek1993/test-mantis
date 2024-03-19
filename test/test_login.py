def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.logget_in_as("administrator")