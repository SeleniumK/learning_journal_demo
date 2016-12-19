def includeme(config):
    """Set up all routes for config to find."""
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
