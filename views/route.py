from flask import Flask


class Route:
    def route(self, app: Flask):
        from views.user import signup, signin, mypage
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(signin.api.blueprint)
        app.register_blueprint(mypage.api.blueprint)

        from views.service import list, update
        app.register_blueprint(list.api.blueprint)
        app.register_blueprint(update.api.blueprint)

        from views.admin import upload, patch
        app.register_blueprint(upload.api.blueprint)
        app.register_blueprint(patch.api.blueprint)
