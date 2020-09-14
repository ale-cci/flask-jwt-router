# Changelog

### Changed

**Release 0.0.25** - 2019-12-10

-   Replaced the the `entity_type` kwarg to `table_name` in the public method `register_entity` [Issue #111](https://github.com/joegasewicz/Flask-JWT-Router/issues/111)
-   Renamed the `update_entity` public method to be called `update_token` [Issue #114](https://github.com/joegasewicz/Flask-JWT-Router/issues/114)
-   Renamed the `register_entity` public method to be called `create_token` [Issue #113](https://github.com/joegasewicz/Flask-JWT-Router/issues/113)
-   Add Models to JWTRoutes class & init_app method [Issue #119](https://github.com/joegasewicz/Flask-JWT-Router/issues/119)

**Release 0.0.26** - 2019-12-11

-   Preflight OPTIONS bug fix [Issue #125](https://github.com/joegasewicz/Flask-JWT-Router/issues/125)

## Unreleased

**Release 0.0.27** - 2020-09-14

-   Secret Key now must be set [Issue #137](https://github.com/joegasewicz/flask-jwt-router/issues/137)
-   Fixes ModuleNotFoundError: No module named 'dateutil' [Issue #138](https://github.com/joegasewicz/flask-jwt-router/issues/138)
-   Removes strategy design pattern from project [Issue #141](https://github.com/joegasewicz/flask-jwt-router/issues/141)
-   renamed extensions to Config [Issue #143](https://github.com/joegasewicz/flask-jwt-router/issues/143)
-   Added token expire duration option [Issue #44](https://github.com/joegasewicz/flask-jwt-router/issues/44)